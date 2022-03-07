# Metamorfo Tattoo Api
### Controle seus agendamentos de tatoo e materiais.
> Status: Em Desenvolvimento ⚠️

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Poketnans/metamorfo-tattoo/blob/development/LICENSE)
# Sobre o Projeto
### Base url da api
https://metamorfo-tattoo.herokuapp.com/

**Metaformo Tattoo Api** é uma aplicação de serviço construida durante o capstone do Q3 no curso de Fullstack Developer na Kenzie Academy.Esta aplicação foi desenvolvida com o Python e Micro Framework Flask.

O Objetivo da aplicação é o usuário cliente marcar agendamentos de tatuagem com um tatuador de sua escolha. O tatuador pode ver seus agendamentos e organizar seu dia a dia para realizar tais atividades.

# Tecnologias Utilizadas
- Python
- Micro Framework Flask
- DB PostgreSQL
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
Pré-requisitos : python 3.9, biblioteca pip.

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
```


## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table textAlign="center">
  <tr>
  <td align="center"><a href="https://github.com/BeatrixFox"><img src="https://avatars.githubusercontent.com/u/72284689?v=4" width="100px;" alt=""/><br />
    </td>
    <td align="center"><a href="https://github.com/Brunoro811"><img src="https://avatars.githubusercontent.com/u/82813383?v=4" width="100px;" alt=""/><br />
    </td>
    <td align="center"><a href="https://github.com/cricardolima"><img src="https://avatars.githubusercontent.com/u/81661730?v=4" width="100px;" alt=""/><br />
    </td>
     <td align="center"><a href="https://github.com/pedromenimen"><img src="https://avatars.githubusercontent.com/u/77471145?v=4" width="100px;" alt=""/><br />
    </td>
    <td align="center"><a href="https://github.com/Poketnans"><img src="https://avatars.githubusercontent.com/u/82735052?v=4" width="100px;" alt=""/><br />
    </td>
    <td align="center"><a href="https://github.com/BaiduAV"><img src="https://avatars.githubusercontent.com/u/82685528?v=4" width="100px;" alt=""/><br />
    </td>
    
  </tr>
</table>
<hr/>

# Endpoints

## Rotas que precisam de autenticação

###  Client Endpoint Post

<h2 align ='center'> Essa rota cria o tatuador</h2>
Nessa aplicação o usuário não registrado pode se cadastrar na plataforma por JSON ou Multipart-form.
Aqui conseguimos ver os parametros para o cadastro:
**JSON**
Neste tipo de cadastro o usuário não faz upload de foto.
```json
{
	"name": "name",
	"email": "email@email.com",
	"password": "1234",
	"birth_date": "10/10/1995",
	"phone": "85912345678",
	"general_information": "",
	"street": "rua",
	"number": 1234,
	"city": "fortaleza"
}
```
Caso dê tudo certo, a resposta será assim:

`POST /create -  FORMATO DA RESPOSTA - STATUS 201`
```json
{
  "id": "72162140-3a69-41f9-9127-d4c4c43bea8a",
  "name": "name",
  "email": "email@email.com",
  "birth_date": "Tue, 10 Oct 1995 00:00:00 GMT",
  "phone": "85912345678",
  "general_information": null,
  "street": "rua",
  "number": 1234,
  "city": "fortaleza"
}
```

**Multipart-form ou Form**
Neste tipo de cadastro o usuário não faz upload de foto.
Array com chaves em string.
```
['data'] = "{
	"name": "Ciclano 2 ",
	"email": "ciclano3@email.com",
	"password": "123456",
	"birth_date": "24/4/1990",
	"phone": "88997998995",
	"general_information": "Nenhuma",
	"street": "Av. Bordo Amour",
	"number": 254,
	"city": "Cidade Verde"
}" 
['file] = FileStorage
```
**Recomendado usar JavaScript, com o objeto da Class FormData**
```js

 const formdata = new FormData();
 formdata.append("file", product.file[0]);
 formdata.append("data", JSON.stringify(objectClient));
 
```

   

