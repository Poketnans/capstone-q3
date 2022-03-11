# Metamorfo Tattoo Api

### Controle seus agendamentos de tatoo e materiais.

> Status: Em Desenvolvimento ⚠️
> [![NPM](https://img.shields.io/npm/l/react)](https://github.com/Poketnans/metamorfo-tattoo/blob/development/LICENSE)

# Sobre o Projeto

### Base url da api

https://metamorfo-tattoo.herokuapp.com/

**Metaformo Tattoo Api** é uma aplicação de serviço construida durante o capstone do Q3 no curso de Fullstack Developer na Kenzie Academy. Esta aplicação foi desenvolvida com o Python e o Micro Framework Flask.

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
<table textAlign="center" style="margin: 0 auto;">
  <tr>
  <td align="center" title="BeatrixFox"><a href="https://github.com/BeatrixFox"><img src="https://avatars.githubusercontent.com/u/72284689?v=4" width="100px;" alt=""/><br />
    </td>
    <td align="center" title="Bruno"><a href="https://github.com/Brunoro811"><img src="https://avatars.githubusercontent.com/u/82813383?v=4" width="100px;" alt=""/><br />
    </td>
    <td align="center" title="Ricardo Lima"><a href="https://github.com/cricardolima"><img src="https://avatars.githubusercontent.com/u/81661730?v=4" width="100px;" alt=""/><br />
    </td>
     <td align="center" title="Pedro Henrique"><a href="https://github.com/pedromenimen"><img src="https://avatars.githubusercontent.com/u/77471145?v=4" width="100px;" alt=""/><br />
    </td>
    <td align="center" title="Etnan"><a href="https://github.com/Poketnans"><img src="https://avatars.githubusercontent.com/u/82735052?v=4" width="100px;" alt=""/><br />
    </td>
    <td align="center" title="Luiz Victor"><a href="https://github.com/BaiduAV"><img src="https://avatars.githubusercontent.com/u/82685528?v=4" width="100px;" alt=""/><br />
    </td>    
  </tr>
</table>
<hr/>

# Endpoints

| Endpoints | Methods | Rule |
| :--- | :--- | :--- |
| clients.post_create | POST | /clients |
| clients.post_login | POST | /clients/login |
| tattooists.post_create | POST | /tattoists |
| tattooists.post_login | POST | /tattooists/login |
| clients.get_all | GET | /clients |
| clients.get_specific | GET | /client |
| clients.get_image | GET | /client/image/<image_hash> |
| clients.update | PATCH | /clients |
| clients.delete | DELETE | /clients |
| clients.logout | DELETE | /clients/logout |
| clients.to_recover_password | POST | /clients/to_recover |
| tattooists.get_all | GET | /tattooists |
| tattooists.get_specific | GET | /tattooists/<id_tattooist> |
| tattoists.get_image | GET | /tattooists/image/<image_hash> |
| tattoists.update | PATCH | /tattooists |
| tattooists.delete | DELETE | /tattooists |
| tattooists.logout | DELETE | /tattooists/logout |
| tattooists.to_recover_password | POST | /tattooists/to_recover |
| tattoos.post_create | POST | /tattoos |
| tattoos.get_all | GET | /tattoos |
| tattoos.get_specific | GET | /tattoos/<id_tattoo> |
| tattoos.get_image | GET | /tattoos/image/<image_hash> |
| tattoos.update | PATCH | /tattoos/<id_tattoo> |
| storage.post | POST | /storage |
| storage.get_all | GET | /storage |
| storage.update | PATCH | /storage/<id> |


<style>
  .post{
    color: #23b72f;
    border-radius:5px;
    padding: 0px 0px 0px 7px;
  }
   .get{
    color: #b25d90;
    border-radius:5px;
    padding: 0px 0px 0px 7px
  }
  .path{
    color: #e5e838;
    border-radius:5px;
    padding: 0px 0px 0px 7px
  }
  .delete{
    color: #e2010a;
    border-radius:5px;
    padding: 0px 0px 0px 7px
  }
</style>

## Rotas que não precisam de autenticação

### Rotas de Cliente
<br>
<details>
  <summary class="post"><b>POST /clients - Essa rota cria o cliente</b></summary>

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

`CREATED - FORMATO DA RESPOSTA - STATUS 201`

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
	"msg": "required fields missing ['phone', 'street', 'number', 'city']"
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
</details>
<br>
<details>
  <summary class="post"><b>POST /clients/login - Essa rota faz o login do cliente na plataforma</b></summary>

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
</details>
<br>

### Rota Tattooist
<br>
<details>
  <summary class="post">
    <b>POST /tattooists - Essa rota cria o tatuador</b>
  </summary>

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
</details>
<br>
<details>
  <summary class="post">
    <b>POST /tattooists/login - Essa rota faz o login do tatuador na plataforma</br>
  </summary>

`POST /tattooists/login - FORMATO DA REQUISIÇÃO`

```json
{
  "email": "name@email.com",
  "password": "s3J#"
}
```

Caso dê tudo certo, a resposta será assim:

`OK - FORMATO DA RESPOSTA - STATUS 201`

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
</details>
<br>

## Rotas que precisam de autenticação atraves do token

### Rota do Cliente
<br>
<details>
<summary class="get">GET /clients - Essa rota retorna todos os clientes cadastrados no banco</summary>

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

Caso o token tenha expirado será lançado um erro:

`UNAUTHORIZED - FORMATO DA RESPOSTA - STATUS 401`

```JSON
{
	"msg": "Token has expired"
}
```
</details>
<br>
<details>
<summary class="get"><b>GET /client - Essa rota retorna os dado do cliente logado</b></summary>

`GET /client - FORMATO DA REQUISIÇÃO`

Não necessita um campo de JSON.

`OK - FORMATO DA RESPOSTA - STATUS 200`

Caso o cliente exista será retornado seus dados:

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
  "city": "fortaleza",
  "url_image": "http://linkdata/clients/profile_image/None"
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

Caso não esteja autenticado será lançado um erro:

`UNPROCESSABLE ENTITY - FORMATO DA RESPOSTA - STATUS 422`

```JSON
{
	"msg": "Bad Authorization header. Expected 'Authorization: Bearer <JWT>'"
}
```
</details>
<br>
<details>
  <summary class="get">
    <b>GET /client/image/&ltimage_hash> - Essa rota captura dados de imagem de um cliente</b>
  </summary>

`GET /client/image/<image_hash> - FORMATO DA REQUISIÇÃO`

Não necessita corpo de requisição. Precisa do nome do imagem como parametro na URL

`OK - FORMATO DA RESPOSTA - STATUS 200`

Caso dê tudo certo, a resposta será renderização da imagem

Erro:

Caso não tenha imagem:

`NOT_FOUND - FORMATO DA RESPOSTA - STATUS 404`
```json
{
  "msg": "image client not found"
}
```
</details>
<br>
<details>
  <summary class="path">
    <b>PATCH /clients - Essa rota atualiza as informações do cliente</b>
  </summary>

`PATCH /clients - FORMATO DA REQUISIÇÃO`

Atualiza os dados do cliente que estiver logado.
Todos os parametros são opicionais e os demais que não constam nessa relação são ignorados.

> O birth_date não pode ser alterado.

Corpo de requisição

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

`OK - FORMATO DA RESPOSTA - STATUS 200`

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
</details>
<br>
<details>
  <summary class="delete">
    <b>DELETE /clients - Essa rota "desativa" a conta de cliente</b>
  </summary>

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

Caso o cliente já tenha sido desativado e seja feita uma nova tentativa com o mesmo token:

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
</details>
<br>
<details>
  <summary class="delete">
    <b>DELETE /clients/logout - Essa rota revoga o token do cliente</b>
  </summary>

`DELETE /clients/logout - FORMATO DA REQUISIÇÃO`

Sem corpo de requisição

Caso tudo dê certo, a resposta será assim:

`OK - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "msg": "JWT revoked"
}
```
</details>
<br>
<details>
  <summary class="post">
    <b>POST /clients/to_recover - Essa rota "recupera" a senha do cliente</b>
  </summary>

Obs.: Essa rota só pode se alcançada se o token de autenticação for do tatuador do tipo admin

`POST /clients/to_recover - FORMATO DA REQUISIÇÃO`

campo de requisição

```json
{
  "id": "b7fedafa-9c9c-4c16-902c-b80175608e1b",
  "password": "s2#S"
}
```

o id que deve ser passado deve ser referente ao cliente na qual será recuperado a conta.
</details>
<br>

### Rota Tattooists
<br>
<details>
  <summary class="get">
    <b>GET /tattoists - Essa rota retorna todos os tatuadores</b>
  </summary>

`GET /tattooists - FORMATO DA REQUISIÇÃO`

Não necessita um campo de JSON.

`OK - FORMATO DA RESPOSTA - STATUS 200`

Caso tenha dados no banco será apresentado um lista:

```JSON
[
	{
		"id": "b1f681d0-f0e3-4219-b6cc-871c7e478e9d",
		"name": "John",
		"email": "johnwickII@gmail.com",
		"general_information": "male, 23 years",
		"admin": true,
		"url_image": "None/tatooists/image/None"
	},
	{
		"id": "58a1e4e9-02a0-49b6-a450-8082eebe26b0",
		"name": "Jonas",
		"email": "nsk@email.com",
		"general_information": "",
		"admin": true,
		"url_image": "None/tatooists/image/None"
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

Caso o token tenha expirado será lançado um erro:

`UNAUTHORIZED - FORMATO DA RESPOSTA - STATUS 401`

```JSON
{
	"msg": "Token has expired"
}
```
</details>
<br>
<details>
  <summary class="get">
    <b>GET /tattooists/&ltid_tattooist> - Retorna dados de um tatuador</b>
  </summary>

`GET /tattooists/<id_tattooist> - FORMATO DA REQUISIÇÃO`

Não necessita um campo de JSON. Porem deve ser passado o id do tatuador como parametro na URL.

`OK - FORMATO DA RESPOSTA - STATUS 200`

Caso o tatuador exista será retornado seus dados:

```JSON
{
	"id": "b1f681d0-f0e3-4219-b6cc-871c7e478e9d",
	"name": "John",
	"email": "johnwickII@gmail.com",
	"general_information": "male, 23 years",
	"admin": true,
	"url_image": "None/tatooists/image/None"
}

```

Erros:

Caso o tatuador buscado não exista:

`NOT FOUND - FORMATO DA RESPOSTA - STATUS 404`

```JSON
{
	"msg": "not found"
}

```

Caso não esteja autenticado será lançado um erro:

`UNPROCESSABLE ENTITY - FORMATO DA RESPOSTA - STATUS 422`

```JSON
{
	"msg": "Bad Authorization header. Expected 'Authorization: Bearer <JWT>'"
}
```
</details>
<br>
<details>
  <summary class="get">
    <b>GET /tattooists/image/&ltimage_hash> - Essa rota captura dados de imagem de um dos tatuadores</b>
  </summary>

`GET /tattooists/image/<image_hash> - FORMATO DA REQUISIÇÃO`

Não necessita corpo de requisição. Precisa do nome do imagem como parametro na URL

`OK - FORMATO DA RESPOSTA - STATUS 200`

Caso dê tudo certo, a resposta será renderização da imagem

Erro:

Caso não tenha imagem:

`NOT_FOUND - FORMATO DA RESPOSTA - STATUS 404`
```json
{
  "msg": "image tattooists not found"
}
```
</details>
<br>
<details>
  <summary class="path">
    <b>PATCH /tattooists - Essa rota atualiza os dados de um tatuador</b>
  </summary>

`PATCH /tattooists - FORMATO DA REQUISIÇÃO`

Atualiza os dados do tatuador que estiver logado.
Todos os parametros são opicionais e os demais que não constam nessa relação são ignorados.
O birth_date não pode ser alterado.

corpo de requisição

```json
{
  "name": "New name",
  "email": "new_email@email.com",
  "password": "s4N#",
  "general_information": "< descriptions >"
}
```

Caso dê tudo certo, a resposta será assim:

`OK- FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "id": "58a1e4e9-02a0-49b6-a450-8082eebe26b0",
  "name": "New name",
  "email": "new_email@email.com",
  "general_information": "< descriptions >",
  "admin": true,
  "url_image": "https://metamorfo-tattoo.herokuapp.com/tatooists/image/<image_name>"
}
```

Erros :

Caso algum dado passado esteja em outro tipo que não seja string será lançado o seguinte erro:
Exemplo: email passado como lista

`BAD REQUEST - FORMATO DA RESPOSTA - STATUS 400`

```JSON
{
   "msg": "invalid keys values ['email']"
}
```

Caso o password passado esteja em formato fora do padrão aceito será lançado o seguinte erro:

`BAD REQUEST - FORMATO DA RESPOSTA - STATUS 400`

```JSON
{
	"error": "password in format incorrect",
	"should be": "Password must contain at least one letter uppercase, one lowercase, one number and one special character"
}
```

Caso algum dado passado esteja em formato fora do padrão aceito será lançado o seguinte erro:
Exemplo : email passado faltando o ".com" no final

`BAD REQUEST - FORMATO DA RESPOSTA - STATUS 400`

```JSON
{
	"error": "email in format incorrect"
}
```
</details>
<br>
<details>
  <summary class="delete">
    <b>DELETE /tattooists - Essa rota "desativa" a conta de um tatuador</b>
  </summary>

`DELETE /tattooists - FORMATO DA REQUISIÇÃO`

Não necessita um campo de JSON.

`OK - FORMATO DA RESPOSTA - STATUS 200`

Caso dê certo será exibida a seguinte mensagem:

```JSON
{
	"msg": "JWT revoked"
}
```

Erros:

Caso o tatuador buscado não exista:

`NOT FOUND - FORMATO DA RESPOSTA - STATUS 404`

```JSON
{
	"msg": "tattooist not found"
}

```

Caso o tatuado já tenha sido desativado e seja feita uma nova tentativa com o mesmo token:

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
</details>
<br>
<details>
  <summary class="delete">
    <b>DELETE /tattooists/logout - Essa rota revoga o token do tatuador</b>
  </summary>

`DELETE /tattooists/logout - FORMATO DA REQUISIÇÃO`

Sem corpo de requisição

Caso tudo dê certo, a resposta será assim:

`OK - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "msg": "JWT revoked"
}
```
</details>
<br>
<details>
  <summary class="post">
    <b>POST /tattooist/to_recover - Essa rota "recupera" a senha do tatuador</b>
  </summary>

> Obs.: Essa rota só pode ser alcançada se o token de autenticação for do tatuador do tipo "admin"

`POST /tattooist/to_recover - FORMATO DA REQUISIÇÃO`

Campo de requisição

```json
{
  "id_tattoist": "b7fedafa-9c9c-4c16-902c-b80175608e1b",
  "new_password": "s2#S"
}
```
Resposta sem corpo.

Caso tattooist não seja um admin :

` UNAUTHORIZED - FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "msg": "not unauthorized"
}
```

Caso não encontre o tattooist :

`NOT_FOUND - FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "msg": "tattooist not found"
}
```
Caso não encontre o client :

` NOT_FOUND - FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "msg": "client not found"
}
```
</details>
<br>

### Rota Tattoos
<br>
<details>
  <summary class="post">
    <b>POST /tattoos - Essa rota cria uma tatuagem</b>
  </summary>

`POST /tattoos - FORMATO DA REQUISIÇÃO`

Registra uma tatuagem no banco.

#### Registrando sem fornecer imagens modelo:

> **Content-Type:** `application/json`

```json
{
  "size": "M",
  "colors": true,
  "body_parts": "Antebraço",
  "tattoo_schedule": {
    "start": "Wed, 05 Oct 2022 15:00:00 GMT",
    "end": "Wed, 05 Oct 2022 16:00:00 GMT"
  },
  "id_tattooist": "1f1d0760-e2ca-4acd-a0ea-0cff41f64d89"
}
```

Caso dê tudo certo, a resposta será assim:

`CREATED - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": "a10be1b3-425d-4081-9782-343d5fc18641",
  "size": "M",
  "colors": true,
  "body_parts": "Antebraço",
  "id_client": "c8e84ea4-4cd1-4fc6-bbcb-9bc034f6dbc4",
  "image_models": [],
  "tattooist": {
    "id": "1f1d0760-e2ca-4acd-a0ea-0cff41f64d89",
    "name": "Cricardo",
    "email": "teste_ric@email.com",
    "general_information": "",
    "admin": true,
    "url_image": "http://localhost:5000/tatooists/image/None"
  },
  "tattoo_schedule": {
    "id": "fb3af2c0-7289-4138-a956-13f66b6066e4",
    "start": "Wed, 05 Oct 2022 15:00:00 GMT",
    "end": "Wed, 05 Oct 2022 16:00:00 GMT",
    "finished": false
  }
}
```

Erros:

`BAD REQUEST - FORMATO DA RESPOSTA- STATUS 400`

Indica a falta de algum campo obrigatório. Os campos nessas condições são listados na mensagem de erro.

_Retorno_ :

```json
{
  "msg": "required fields missing <list>"
}
```

`BAD REQUEST - FORMATO DA RESPOSTA- STATUS 400`

Algum campo foi passado com o tipo de valor errado. Os campos nessas condições são listados na mensagem de erro.

_Retorno_:

```json
{
  "msg": "invalid keys values <list>"
}
```

`CONFLICT - FORMATO DA RESPOSTA - STATUS 409`

Não foi encontrado um cliente com o ID informado no Bearer Token.

_Retorno_:

```json
{
  "msg": "id_client not found"
}
```

`CONFLICT - FORMATO DA RESPOSTA - STATUS 409`

Não foi encontrado um tatuador com o ID informado

_Retorno_:

```json
{
  "msg": "id_tattooist not found"
}
```
</details>
<br>
<details>
  <summary class="get">
    <b>GET /tattoos - Essa rota retorna todas as tatuagens cadastradas</b>
  </summary>
- **Listar dados das tatuagens feitas**

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

Caso o token tenha expirado será lançado um erro:

`UNAUTHORIZED - FORMATO DA RESPOSTA - STATUS 401`

```JSON
{
	"msg": "Token has expired"
}
```
</details>
<br>
<details>
  <summary class="get">
    <b>GET /tattoos/&ltid_tattoo> - Essa rota retorna informações sobre uma tatuagem específica</b>
  </summary>

`GET /tattoos/<id_tattoo> - FORMATO DA REQUISIÇÃO`

Não necessita de um campo de requisição apenas é necessário passar como parametro o id na url.

`OK - FORMATO DA RESPOSTA - STATUS 200`

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
</details>
<br>
<details>
  <summary class="get">
    <b>GET /tattoos/image/&ltimage_hash> - Essa rota captura dados de imagem de uma tatuagem</b>
  </summary>

`GET /tattoos/image/<image_hash> - FORMATO DA REQUISIÇÃO`

Não necessita corpo de requisição. Precisa do nome do imagem como parametro na URL

`OK - FORMATO DA RESPOSTA - STATUS 200`

Caso dê tudo certo, a resposta será renderização da imagem

Erro:

Caso não tenha imagem:

`NOT_FOUND - FORMATO DA RESPOSTA - STATUS 404`
```json
{
  "msg": "tattoo image not found"
}
```
</details>
<br>
<details>
  <summary class="path">
    <b>PATCH /tattoos/&ltid_tattoo> - Essa rota atualiza informações de tatuagens</b>
  </summary>

`PATCH /tattoos/<id_tattoo> - FORMATO DA REQUISIÇÃO`

Para atualizar dados da tatuage, passe os campos que quer atualizar.
Todos os parametros são opcionais e os demais que não constam nessa relação são ignorados.

corpo de requisição

```json
{
  "size": ["Small", "Medium", "Large"],
  "colors": true,
  "body_parts": "Arm",
  "tattoo_schedule": {
      "start": "15/03/2022 21:00:00",
			"end": "15/03/2022 22:00:00"
	},
	"id_tattooist": "1f1d0760-e2ca-4acd-a0ea-0cff41f64d89",
	"materials": [
	    {
		    "id_item": "66c9bd2d-0923-44ca-a2f7-cd485fbc7f89",
		    "quantity": 3
	    }
    ],
}
```

Caso dê tudo certo, a resposta será assim:

`OK - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "id": "a7da8f04-ad0d-4b1b-8d5f-45885e525b54",
  "size": ["Small", "Medium", "Large"],
  "colors": true,
  "id_client": "aadb0d9b-70bc-44c4-afac-0771edba8bd9",
  "body_parts": "Arm",
  "image_models": [],
	"tattooist": {
		"id": "1f1d0760-e2ca-4acd-a0ea-0cff41f64d89",
		"name": "Cricardo",
		"email": "teste_ric@email.com",
		"general_information": "",
		"admin": true,
		"url_image": "http://localhost:5000/tatooists/image/None"
	},
	"tattoo_schedule": {
		"id": "fb3af2c0-7289-4138-a956-13f66b6066e4",
		"start": "Wed, 05 Oct 2022 15:00:00 GMT",
		"end": "Wed, 05 Oct 2022 16:00:00 GMT",
		"finished": false
	},
  "materials": [
		{
			"id": "cad66967-3bbd-4d44-8cf9-1ee3f61ba3bd",
			"id_item": "76506511-1d29-4e24-81f9-35d2d13e1d93",
			"id_tattoo": "51032eab-fa71-43ed-9871-f4fa3581296c",
			"quantity": 3
		}
	]
}
```
Erros Possíveis:

`400 - BAD_REQUEST`

Indica a falta de algum campo obrigatório. Os campos nessas condições são listados na mensagem de erro.

Retorno

``` json
{
	"msg": "required fields missing <list>"
}
```

`400 - BAD_REQUEST`

Algum campo foi passado com o tipo de valor errado. Os campos nessas condições são listados na mensagem de erro.

Retorno

``` json
{
  "msg": "invalid keys values <list>"
}
```

`404 - NOT FOUND`

Não foi encontrado uma tatuagem ou um item com o id informado.

Retorno

``` json
{
  "msg": "<tattoo||item> not found"
}
```

`409 - CONFLICT`

Erro relacionado ao cadastro de materiais.
A quantidade a ser retirada excede o que tem no estoque.
Retorno

``` json
{
  "msg": "unavaliable item quantity",
  "item": {
    "id": "66c9bd2d-0923-44ca-a2f7-cd485fbc7f89",
    "name": "Tinta preta",
    "description": "Serve para furar! ;-)",
    "remaining_quantity": 2
  }
}
```
</details>
<br>

### Rotas referente ao estoque
<br>
<details>
  <summary class="post">
    <b>POST /storage - Essa rota cria um item no estoque</b>
  </summary>

`POST /storage - FORMATO DA REQUISIÇÃO`

> Deve ser realizado por um tatuador **admin**.

Campo de requisição

```json
{
  "name": "Tinta azul",
  "quantity": 50,
  "description": "Tintimento",
  "validity": "07/03/2023"
}
```

Caso dê tudo certo, a resposta será assim:

`CREATED - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": "2d75ef2c-77bb-4ab3-838a-c7325118ac84",
  "name": "Tinta azul",
  "quantity": 50,
  "description": "Tintimento",
  "validity": "Tue, 07 Mar 2023 00:00:00 GMT"
}
```

_Erros_:

`BAD REQUEST - FORMATO DA RESPOSTA- STATUS 400`

Indica a falta de algum campo obrigatório. Os campos nessas condições são listados na mensagem de erro.

_Retorno_:

```json
{
  "msg": "required fields missing <list>"
}
```

`BAD REQUEST - FORMATO DA RESPOSTA- STATUS 400`

Algum campo foi passado com o tipo de valor errado. Os campos nessas condições são listados na mensagem de erro.

_Retorno_:

```json
{
  "msg": "invalid keys values <list>"
}
```

`BAD REQUEST - FORMATO DA RESPOSTA- STATUS 400`

A data de validade informada está em um formato incorreto

_Retorno_:

```json
{
  "msg": "Invalid date format. Try DD/MM/YYY"
}
```

`UNAUTHORIZED - FORMATO DA RESPOSTA - STATUS 401`

O tatuador com id informado no Bearer Token não possui funciolalidade de administrador.

_Retorno_

```json
{
  "msg": "not unauthorized"
}
```

`CONFLICT - FORMATO DA RESPOSTA - STATUS 409`

Não foi encontrado um tatuador com o ID informado no Bearer Token

_Retorno_

```json
{
  "msg": "id_tattooist not found"
}
```
</details>
<br>
<details>
  <summary class="get">
    <b>GET /storage - Essa rota retorna todos os itens no estoque</b>
  </summary>

`GET /storage - FORMATO DA REQUISIÇÃO`

Não necessita de um campo de JSON

`OK - FORMATO DA RESPOSTA - STATUS 200`

Caso exista dados no estoque será retornado um lista:

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
</details>
<br>
<details>
  <summary class="path">
    <b>PATCH /storage/&ltid> - Atualiza os dados de um item</b>
  </summary>

- **Atualiza dados de um item do estoque**

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

`OK- FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "name": "Ink",
  "quantity": 30,
  "description": "Blue ink",
  "validity": "Fri, 20 May 2022 00:00:00 GMT"
}
```
</details>
