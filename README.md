# Metamorfo Tatoo Api
### Controle seus agendamentos de tatoo e materiais.
> Status: Em Desenvolvimento ⚠️

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Brunoro811/teste-font-end-competi/blob/main/LICENSE)
# Sobre o Projeto
### Base url da api
https://metamorfo-tattoo.herokuapp.com/

**Metaformo Tattoo Api** é uma aplicação de serviço construida durante o capstone do Q3 no curso de Fullstack Developer na Kenzie Academy.Esta aplicação foi desenvolvida com o Python e Micro Framework Flask.

O Objetivo da aplicação é o usuário cliente marcar agendamentos de tatuagem com um tatuador de sua escolha. O tatuador pode ver seus agendamentos e organizar seu dia a dia para realizar tais atividades.

# Tecnologias Utilizadas
- Python
- Micro Framework Flask
- DB Postgress
- Deploy Heroku


# Bibliotecas Utilizadas
- Flask Migrate
- Flask SQLAlchemy
- Flask JWT Extended
- Postgresql
- Environs
- Python-dotenv ( para ambiente de Desenvolvimento)
- Psycopg2
- Pillow (Tratamento de imagens)
- Requests
- Gunicorn

# Como executar
pré-requisitos : python 3.9, biblioteca pip.
Executa: 
1 - Criar um ambiente vitual venv :
```bash
python -m venv venv 
 ``` 
 
2 - Ativar um ambiente vitual venv :
```bash
source venv/bin/activate
 ``` 
 
3 - Instalar as bibliotecas que estão no arquivo requirements.txt:
```bash
pip install -r requirements.txt
 ``` 

4 - Criar um arquivo .env com os dados de .env.example e subistituie pelos seus dados os campos:
- Bando de dados
- usuário do banco
- senha do banco

5 - Rodar o servidor
```bash
flask run
