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

Caso o tipo de um ou mais campos esteja incorreto com relação ao tipo de dado esperado , será lançado um erro com uma lista desses campos. Por exemplo:

O campo name foi enviado como número.

`BAD REQUEST - FORMATO DA RESPOSTA- STATUS 400`

```JSON
{
  "msg": "invalid keys values ['name']"
}
```

Caso um ou mais campos esteja faltando será lançado um erro com uma lista desses campos. Por exemplo:

Os campos phone , street , number , city não foram passados. Obs.: O campo general_information é opcional.

`BAD REQUEST - FORMATO DA RESPOSTA- STATUS 400`

```JSON
{
	"msg": "required fields missing ['phone', 'general_information', 'street', 'number', 'city']"
}
```

Caso o dado passado não esteja no formato correto será lançado um erro. Por exemplo:

Os campos phone foi passado com mais de 11 numeros.

`BAD REQUEST - FORMATO DA RESPOSTA- STATUS 400`

```JSON
{
	"error": "phone in format incorrect"
}
```

Caso o password passado não esteja no formato correto será lançado um erro.

`BAD REQUEST - FORMATO DA RESPOSTA- STATUS 400`

```JSON
{
	"error": "password in format incorrect",
	"should be": "Password must contain at least one letter uppercase, one lowercase, one number and one special character"
}
```

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

Caso o cliente não exista:

`NOT FOUND - FORMATO DA RESPOSTA - STATUS 404`

```JSON
{
	"msg": "user not found"
}
```

Caso o password passado seja de outro tipo que não seja string:

`BAD REQUEST - FORMATO DA RESPOSTA - STATUS 400`

```JSON
{
	"msg": "invalid keys values ['password']"
}
```

Caso o email exista porem foi usado o password errado:

`NOT FORBIDDEN - FORMATO DA RESPOSTA - STATUS 403`

```JSON
{
	"msg": "wrong password"
}
```

### Rota do Tattuador

#### **Tattoists POST - Essa rota cria o Tatuador**

Nessa aplicação o usuário profissional(Tatuador) não registrado pode se cadastrar na plataforma por JSON ou Multipart-form.

Aqui conseguimos ver os parametros para o cadastro:

`POST /tattooists - FORMATO DA REQUISIÇÃO`

**JSON**
Neste tipo de cadastro o tatuador não faz upload de foto.

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

Caso um ou mais campos esteja faltando será lançado um erro com uma lista desses campos. Por exemplo:

Os campos admin não foram passados. Obs.: O campo general_information é opcional.

`BAD REQUEST - FORMATO DA RESPOSTA- STATUS 400`

```JSON
{
	"msg": "required fields missing ['admin']"
}
```

Caso o tipo de um ou mais campos esteja incorreto com relação ao tipo de dado esperado , será lançado um erro com uma lista desses campos. Por exemplo:

O campo name foi enviado como número.

`BAD REQUEST - FORMATO DA RESPOSTA- STATUS 400`

```JSON
{
  "msg": "invalid keys values ['name']"
}
```

Caso o password passado não esteja no formato correto será lançado um erro.

`BAD REQUEST - FORMATO DA RESPOSTA- STATUS 400`

```JSON
{
	"error": "password in format incorrect",
	"should be": "Password must contain at least one letter uppercase, one lowercase, one number and one special character"
}
```

Caso o email passado não esteja no formato correto será lançado um erro.

`BAD REQUEST - FORMATO DA RESPOSTA- STATUS 400`

```JSON
{
	"error": "email in format incorrect"
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

Caso o tatuador ainda não tenha cadastro:

`NOT FOUND - FORMATO DA RESPOSTA - STATUS 404`

```JSON
{
	"msg": "user not found"
}
```

Caso o password passado seja de outro tipo que não seja string:

`BAD REQUEST - FORMATO DA RESPOSTA - STATUS 400`

```JSON
{
	"msg": "invalid keys values ['password']"
}
```

Caso o email exista porem foi usado o password errado:

`NOT FORBIDDEN - FORMATO DA RESPOSTA - STATUS 403`

```JSON
{
	"msg": "wrong password"
}
```

## Rotas que precisam de autenticação atraves do token

### Rota do Cliente

Listar todos os Clientes

`GET /clients - FORMATO DA REQUISIÇÃO`

Não necessita um campo de JSON.

`OK - FORMATO DA RESPOSTA - STATUS 200`

Caso tenha dados no banco será apresentado um lista:

```JSON
[
	{
		"id": "695fd874-3699-4ef5-9d20-9ff696b1b516",
		"name": "Beny",
		"email": "beny@gmail.com",
		"birth_date": "Sun, 24 Sep 2000 00:00:00 GMT",
		"phone": "231444542332",
		"general_information": null,
		"street": "louvre street",
		"number": 2,
		"city": "london",
		"url_image": "None/client/image/None"
	},
	{
		"id": "47969aba-1f76-406c-870a-5615959b000b",
		"name": "Ciclano",
		"email": "ciclano@email.com",
		"birth_date": "Tue, 24 Apr 1990 00:00:00 GMT",
		"phone": "88999999995",
		"general_information": "Nenhuma",
		"street": "Av. Bordo Amour",
		"number": 254,
		"city": "Cidade Verde"
	},
	{
		"id": "b7fedafa-9c9c-4c16-902c-b80175608e1b",
		"name": "Beto",
		"email": "beto@email.com",
		"birth_date": "Tue, 24 Apr 1990 00:00:00 GMT",
		"phone": "85912345678",
		"general_information": null,
		"street": "Av. Bordo Amour",
		"number": 254,
		"city": "Cidade Verde"
	}
]
```

Caso não exista dados :

`OK - FORMATO DA RESPOSTA - STATUS 200`

```JSON
[]

```

Erros:

Caso não esteja autenticado será lançado um erro:

`UNPROCESSABLE ENTITY - FORMATO DA RESPOSTA - STATUS 422`

```JSON
{
	"msg": "Bad Authorization header. Expected 'Authorization: Bearer <JWT>'"
}
```

Capturar dados de um Cliente

`GET /client - FORMATO DA REQUISIÇÃO`

Não necessita um campo de JSON.

`OK - FORMATO DA RESPOSTA - STATUS 200`

Caso o cliente exista será retornado os dados do cliente:

```JSON
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

Caso o cliente buscado não exista:

`NOT FOUND - FORMATO DA RESPOSTA - STATUS 404`

```JSON
{
	"msg": "client not found"
}

```

Erros:

Caso não esteja autenticado será lançado um erro:

`UNPROCESSABLE ENTITY - FORMATO DA RESPOSTA - STATUS 422`

```JSON
{
	"msg": "Bad Authorization header. Expected 'Authorization: Bearer <JWT>'"
}
```

Captura dado de imagem de um Cliente

`GET /client/image/<image_name> - FORMATO DA REQUISIÇÃO`

Atualiza dados do Cliente

`PATCH /clients - FORMATO DA REQUISIÇÃO`

Atualiza os dados do cliente que estiver logado.
Todos os parametros são opicionais e os demais que não constam nessa relação são ignorados.
O birth_date não pode ser alterado.

corpo de requisição

```json
{
  "name": "name",
  "email": "email@email.com",
  "password": "1234",
  "phone": "85912345678",
  "general_information": "",
  "street": "rua",
  "number": 1234,
  "city": "fortaleza"
}
```

Caso dê tudo certo, a resposta será assim:

`POST /update - FORMATO DA RESPOSTA - STATUS 200`

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

Desativar Cliente

`DELETE /clients - FORMATO DA REQUISIÇÃO`

Não necessita um campo de JSON.

`OK - FORMATO DA RESPOSTA - STATUS 200`

Caso dê certo será exibida a seguinte mensagem:

```JSON
{
	"msg": "JWT revoked"
}
```

Erros:

Caso o cliente buscado não exista:

`NOT FOUND - FORMATO DA RESPOSTA - STATUS 404`

```JSON
{
	"msg": "client not found"
}

```

Caso o cliente já tenha sido deletado e seja feita uma nova tentativa com o mesmo token:

`UNAUTHOIZED - FORMATO DA RESPOSTA - STATUS 401`

```JSON
{
	"msg": "Token has been revoked"
}
```

Caso não esteja autenticado será lançado um erro:

`UNPROCESSABLE ENTITY - FORMATO DA RESPOSTA - STATUS 422`

```JSON
{
	"msg": "Bad Authorization header. Expected 'Authorization: Bearer <JWT>'"
}
```

Reativar Cliente - Recuperar senha. Obs.: Essa rota só pode se alcançada se o token for do tatuador

`POST /clients/to_recover - FORMATO DA REQUISIÇÃO`

### Rota do Tattuador

Listar todos os Tattuadores

`GET /tattooists - FORMATO DA REQUISIÇÃO`

Capturar dados de um Tattuadores

`GET /tattooists/<id_tattooist> - FORMATO DA REQUISIÇÃO`

Atualiza dados do Tattuador

`PATCH /tattooists - FORMATO DA REQUISIÇÃO`

Nessa aplicação o usuário logado pode atualizar a tatuagem na plataforma dessa forma:
Todos os parametros são opcionais e os demais que não constam nessa relação são ignorados.

corpo de requisição

```json
{
	"size": ["Small", "Medium", "Large"],
	"colors": True,
	"body_parts": "Arm",
	"id_tattoist": "20d097d1-0d53-4b10-9ebb-2b91e262d270"
}
```

Caso dê tudo certo, a resposta será assim:

`POST /update - FORMATO DA RESPOSTA - STATUS 200`

```json
{
	"id": "a7da8f04-ad0d-4b1b-8d5f-45885e525b54",
	"size": ["Small", "Medium", "Large"],
	"colors": True,
	"id_client": "aadb0d9b-70bc-44c4-afac-0771edba8bd9",
	"body_parts": "Arm",
	"id_tattoist": "20d097d1-0d53-4b10-9ebb-2b91e262d270"
}
```

Desativar Tattuador

`DELETE /tattooists - FORMATO DA REQUISIÇÃO`

### Rotas referente a Tatuagem

Criar uma tatuagem

`POST /tattoos - FORMATO DA REQUISIÇÃO`

Listar dados das tatuagens feitas

`GET /tattoos - FORMATO DA REQUISIÇÃO`

Não necessita de um campo de requisição

`GET /tattoos - FORMATO DA RESPOSTA - STATUS 200`

Caso tenha dados de tatuagem no banco será mostrada em uma lista:

```json
[
  {
    "id": "958783de-8f55-4613-a2eb-0522abbb5b66",
    "size": "Big",
    "colors": false,
    "body_parts": "Perna",
    "id_client": "958783de-8f55-4613-a2eb-0522abbb5b66",
    "tattoo_schedule": {
      "id": "958783de-8f55-4613-a2eb-0522abbb5b66",
      "start": "Sun, 06 Mar 2022 00:00:00 GMT",
      "end": "Sun, 06 Mar 2022 00:00:00 GMT",
      "finished": false
    },
    "tattoist": {
      "id": "d7ed6f88-b29e-4826-afd8-d572f50ace14",
      "name": "Pedron",
      "email": "elcabron@email.com",
      "general_information": "",
      "admin": true,
      "url_image": "http://localhost:5000/tattooists/profile_image/None"
    }
  }
]
```

Caso não tenha

Capturar dados de uma tatuagem especifica

`GET /tattoos/<id_tattoo> - FORMATO DA REQUISIÇÃO`

Não necessita de um campo de requisição apenas é necessário passar como parametro o id na url.

`GET /tattoos - FORMATO DA RESPOSTA - STATUS 200`

Caso tatto seja encontrada:

```json
{
  "id": "958783de-8f55-4613-a2eb-0522abbb5b66",
  "size": "Big",
  "colors": false,
  "body_parts": "Perna",
  "id_client": "958783de-8f55-4613-a2eb-0522abbb5b66",
  "tattoo_schedule": {
    "id": "958783de-8f55-4613-a2eb-0522abbb5b66",
    "start": "Sun, 06 Mar 2022 00:00:00 GMT",
    "end": "Sun, 06 Mar 2022 00:00:00 GMT",
    "finished": false
  },
  "tattoist": {
    "id": "d7ed6f88-b29e-4826-afd8-d572f50ace14",
    "name": "Pedron",
    "email": "elcabron@email.com",
    "general_information": "",
    "admin": true,
    "url_image": "http://localhost:5000/tattooists/profile_image/None"
  }
}
```

Error:

Caso o id da tatuagem não seja encontrada

`NOT FOUND - FORMATO DA RESPOSTA - STATUS 404`

```JSON
{
  "msg": "tattoo not found"
}

```

Caso o id esteja em formato incorreto:

`NOT FOUND - FORMATO DA RESPOSTA - STATUS 404`

```JSON
{
  "msg": "wrong id format"
}

```

---

Atualiza dados de uma tatuagem

`PATCH /tattoos/<id_tattoo> - FORMATO DA REQUISIÇÃO`

### Rotas referente ao estoque

Criar um item no estoque

`POST /storage - FORMATO DA REQUISIÇÃO`

Listar dados do estoque

`GET /storage - FORMATO DA REQUISIÇÃO`

Não necessita corpo de requisição

`GET /storage - FORMATO DA RESPOSTA - STATUS 200`

Caso a requisição dê certa será retornada uma lista:

```json
[
  {
    "id": "727282140-3a69-41f9-9127-d4c4c43bea8a",
    "name": "ink",
    "description": "yellow ink",
    "quantity": 20,
    "validity": "Tue, 10 Oct 2025 00:00:00 GMT"
  }
]
```

Atualiza dados de um item do estoque

`PATCH /storage/<id> - FORMATO DA REQUISIÇÃO`

Necessario passar um id do produto para poder efetuar a atualização de dados.
Todos os parametros são opcionais e os demais que não constam nessa relação são ignorados.

corpo de requisição

```json
{
  "name": "Ink",
  "quantity": 30,
  "description": "Blue ink",
  "validity": "20-05-2022"
}
```

Caso dê tudo certo, a resposta será assim:

`POST /update - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "name": "Ink",
  "quantity": 30,
  "description": "Blue ink",
  "validity": "Fri, 20 May 2022 00:00:00 GMT"
}
```

# capstone-q3

Projeto Capstone Q3 na Kenzie Academy
