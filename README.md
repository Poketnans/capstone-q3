# capstone-q3

Projeto Capstone Q3 na Kenzie Academy

# Metamorfo Tattoo Api

### Controle seus agendamentos de tatoo e materiais.

> Status: Em Desenvolvimento ⚠️
> [![NPM](https://img.shields.io/npm/l/react)](https://github.com/Poketnans/metamorfo-tattoo/blob/development/LICENSE)

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

## Rotas que não precisa de autenticação

### Rotas de Cliente

#### **Client POST - Essa rota cria o Cliente**

Nessa aplicação o usuário não registrado pode se cadastrar na plataforma por JSON ou Multipart-form.

Aqui conseguimos ver os parametros para o cadastro:

`POST /clients - FORMATO DA REQUISIÇÃO`

**JSON**
Neste tipo de cadastro o usuário não faz upload de foto.

```json
{
  "name": "name",
  "email": "email@email.com",
  "password": "sd33NT#",
  "birth_date": "10/10/1995",
  "phone": "85912345678",
  "general_information": "",
  "street": "rua",
  "number": 1234,
  "city": "fortaleza"
}
```

Caso dê tudo certo, a resposta será assim:

`POST /clients - FORMATO DA RESPOSTA - STATUS 201`

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
  "name": "name",
  "email": "email@email.com",
  "password": "sd33NT#",
  "birth_date": "10/10/1995",
  "phone": "85912345678",
  "general_information": "",
  "street": "rua",
  "number": 1234,
  "city": "fortaleza"
}"
['file] = FileStorage
```

**Recomendado usar JavaScript, com o objeto da Class FormData**

```js
const formdata = new FormData();
formdata.append("file", product.file[0]);
formdata.append("data", JSON.stringify(objectClient));
```

Errors:

Caso já exista:

`CONFLICT - FORMATO DA RESPOSTA - STATUS 409`

```JSON
{
  "msg": "email already registered"
}
```

Caso o tipo de um ou mais campos esteja incorreto será lançado um erro com uma lista desses campos. Por exemplo:

O campo name foi enviado como número.

`BAD REQUEST - FORMATO DA RESPOSTA- STATUS 400`

````JSON
{
  "msg": "invalid keys values ['name']"
}
```# capstone-q3
Projeto Capstone Q3 na Kenzie Academy
````

#### **Client/login POST - Essa rota faz o login do cliente na plataforma**

`POST /clients/login - FORMATO DA REQUISIÇÃO`

```json
{
  "email": "email@email.com",
  "password": "sd33NT#"
}
```

Caso dê tudo certo, a resposta será assim:

`POST /clients/login - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "access token": "token gerado apartir de dados codificados"
}
```

Erros :

### Rota do Tattuador

#### **Tattoists POST - Essa rota cria o Tattuador**

Nessa aplicação o usuário profissional não registrado pode se cadastrar na plataforma por JSON ou Multipart-form.

Aqui conseguimos ver os parametros para o cadastro:

`POST /tattooists - FORMATO DA REQUISIÇÃO`

**JSON**
Neste tipo de cadastro o tattuador não faz upload de foto.

```json
{
  "name": "name",
  "email": "name@email.com",
  "password": "s3J#",
  "general_information": "",
  "admin": false
}
```

Caso dê tudo certo, a resposta será assim:

`POST /tattooists - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": "f83465aa-a57d-47c4-b018-fe049ded6c17",
  "name": "name",
  "email": "name@email.com",
  "general_information": "",
  "admin": false
}
```

**Multipart-form ou Form**
Neste tipo de cadastro o tattuador faz upload de foto.
Array com chaves em string.

```
['data'] = "{
  "name": "name",
  "email": "name@email.com",
  "password": "s3J#",
  "general_information": "",
  "admin": false
}"
['file] = FileStorage
```

**Recomendado usar JavaScript, com o objeto da Class FormData**

```js
const formdata = new FormData();
formdata.append("file", product.file[0]);
formdata.append("data", JSON.stringify(objectTattoist));
```

Errors:

Caso já exista o email:

`CONFLICT - FORMATO DA RESPOSTA - STATUS 409`

```JSON
{
  "msg": "email already registered"
}
```

#### **Tattooists/login POST - Essa rota faz o login do tattuador na plataforma**

`POST /tattooists/login - FORMATO DA REQUISIÇÃO`

```json
{
  "email": "name@email.com",
  "password": "s3J#"
}
```

Caso dê tudo certo, a resposta será assim:

`POST /tattooists/login - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "access token": "token gerado apartir de dados codificados"
}
```

Erros :

## Rotas que precisam de autenticação

### Rota do Cliente

Listar Clientes

`GET /clients - FORMATO DA REQUISIÇÃO`

Capturar dados de um Cliente

`GET /client - FORMATO DA REQUISIÇÃO`

Captura dado de imagem de um Cliente

`GET /client/image/<image_name> - FORMATO DA REQUISIÇÃO`

Atualiza dados do Cliente

`PATCH /clients - FORMATO DA REQUISIÇÃO`

Desativar Cliente

`DELETE /clients - FORMATO DA REQUISIÇÃO`

### Rota do Tattuador

Listar Tattuadores

`GET /tattooists - FORMATO DA REQUISIÇÃO`

Capturar dados de um Tattuadores

`GET /tattooists/<id_tattooist> - FORMATO DA REQUISIÇÃO`

Atualiza dados do Tattuador

`PATCH /tattooists - FORMATO DA REQUISIÇÃO`

Desativar Tattuador

`DELETE /tattooists - FORMATO DA REQUISIÇÃO`

### Rotas referente a Tatuagem

Criar uma tatuagem

`POST /tattoos - FORMATO DA REQUISIÇÃO`

Listar dados das tatuagens feitas

`GET /tattoos - FORMATO DA REQUISIÇÃO`

Capturar dados de uma tatuagem especifica

`GET /tattoos/<id_tattoo> - FORMATO DA REQUISIÇÃO`

Atualiza dados de uma tatuagem

`PATCH /tattoos/<id_tattoo> - FORMATO DA REQUISIÇÃO`

### Rotas referente ao estoque

Criar um item no estoque

`POST /storage - FORMATO DA REQUISIÇÃO`

Listar dados do estoque

`GET /storage - FORMATO DA REQUISIÇÃO`

Atualiza dados de um item do estoque

`PATCH /storage/<id> - FORMATO DA REQUISIÇÃO`
