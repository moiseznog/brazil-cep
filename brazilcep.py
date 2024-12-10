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

        self.result_area = QtWidgets.QTextEdit()
        self.result_area.setReadOnly(True)
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
        cep = self.cep_input.text().replace('-', '')
        try:
            response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            data = response.json()
            if 'erro' in data:
                self.result_area.setText('CEP não encontrado.')
            else:
                resultado = (
                    f"CEP: {data['cep']}\n"
                    f"Estado: {data['uf']}\n"
                    f"Cidade: {data['localidade']}\n"
                    f"Bairro: {data['bairro']}\n"
                    f"Rua: {data['logradouro']}\n"
                    f"Complemento: {data.get('complemento', '-')}\n"
                    f"Número: {data.get('numero', '-')}\n"
                )
                self.result_area.setText(resultado)
        except Exception as e:
            self.result_area.setText(f"Erro ao consultar CEP: {e}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CepWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
