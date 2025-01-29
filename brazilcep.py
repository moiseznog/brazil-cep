import sys
import requests
from PyQt5 import QtWidgets, QtGui, QtCore

class CepWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Buscador de CEP')
        self.setWindowIcon(QtGui.QIcon(r'C:\Users\User\Downloads\icons8-endereço-50.png'))  # Adicione o ícone aqui
        self.setGeometry(100, 100, 400, 300)

        layout = QtWidgets.QVBoxLayout()

        self.cep_label = QtWidgets.QLabel('Digite o CEP:')
        layout.addWidget(self.cep_label)

        self.cep_input = QtWidgets.QLineEdit()
        self.cep_input.setInputMask('00000-000')
        layout.addWidget(self.cep_input)

        self.search_button = QtWidgets.QPushButton('Buscar')
        self.search_button.setStyleSheet('background-color: blue; color: white;')
        self.search_button.clicked.connect(self.search_cep)
        layout.addWidget(self.search_button)

        self.result_area = QtWidgets.QWidget()
        self.result_layout = QtWidgets.QVBoxLayout(self.result_area)
        layout.addWidget(self.result_area)

        self.setLayout(layout)

        # Adiciona data e hora na parte inferior da janela
        self.time_label = QtWidgets.QLabel()
        layout.addWidget(self.time_label, alignment=QtCore.Qt.AlignBottom)
        self.update_time()

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        current_time = QtCore.QDateTime.currentDateTime().toString(QtCore.Qt.DefaultLocaleLongDate)
        self.time_label.setText(current_time)

    def search_cep(self):
        # Limpa o layout de resultados anterior
        self.clear_results()

        cep = self.cep_input.text().replace('-', '')
        try:
            response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            data = response.json()
            if 'erro' in data:
                self.display_error('CEP não encontrado.')
            else:
                self.display_result(
                    ('CEP', data['cep']),
                    ('Estado', data['uf']),
                    ('Cidade', data['localidade']),
                    ('Rua', data['logradouro']),
                    ('Bairro', data['bairro']),
                    ('Complemento', data.get('complemento', '-')),
                    ('Número', data.get('numero', '-'))
                )
        except Exception as e:
            self.display_error(f"Erro ao consultar CEP: {e}")

    def display_result(self, *lines):
        for i in reversed(range(self.result_layout.count())): 
            widget = self.result_layout.itemAt(i).widget()
            if widget is not None: 
                widget.deleteLater()

        for label_text, value_text in lines:
            hbox = QtWidgets.QHBoxLayout()
            label = QtWidgets.QLabel(f"{label_text}: {value_text}")
            copy_button = QtWidgets.QPushButton('Copiar')
            copy_button.setStyleSheet('background-color: #A9A9A9; color: white;')
            copy_button.clicked.connect(lambda _, t=value_text: self.copy_to_clipboard(t))
            hbox.addWidget(label)
            hbox.addWidget(copy_button)
            widget = QtWidgets.QWidget()
            widget.setLayout(hbox)
            self.result_layout.addWidget(widget)

    def display_error(self, message):
        self.clear_results()
        error_label = QtWidgets.QLabel(message)
        self.result_layout.addWidget(error_label)

    def clear_results(self):
        for i in reversed(range(self.result_layout.count())):
            widget = self.result_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def copy_to_clipboard(self, text):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(text)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CepWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
