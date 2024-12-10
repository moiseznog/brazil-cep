Funcionalidades
Consulta de CEP: Realiza consultas detalhadas de CEP, retornando informações como Estado, Cidade, Bairro, Rua e Complemento.

Interface Gráfica: Desenvolvida com PyQt5, a interface permite fácil inserção do CEP e visualização dos resultados.

Data e Hora em Tempo Real: Exibe a data e hora atualizadas em tempo real na parte inferior da janela.

Tratamento de Erros: Exibe mensagens apropriadas quando um CEP inválido é consultado ou quando ocorre algum erro na consulta.

Tecnologias Utilizadas
Python

PyQt5: Para a construção da interface gráfica.

Requests: Para realizar chamadas à API ViaCEP.

Pré-requisitos
Python 3.x

Bibliotecas Python: PyQt5, Requests

Instalação
Passo 1: Clone o Repositório
sh
git clone https://github.com/seu-usuario/BuscadorCEP.git
cd BuscadorCEP
Passo 2: Instale as Dependências
sh
pip install pyqt5 requests
Passo 3: Execute a Aplicação
sh
python buscador_cep.py
Funcionamento
Abra a aplicação e insira um CEP válido no campo de entrada.

Clique no botão "Buscar" para realizar a consulta.

As informações do endereço relacionadas ao CEP inserido serão exibidas na área de resultados.

Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests. Seguem algumas maneiras de contribuir:

Reportar bugs.

Sugerir novas funcionalidades.

Melhorar a documentação.
