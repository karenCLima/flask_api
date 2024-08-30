# flask_api
## :paperclips: Sobre
Uma API em Flask com autenticação JWT

## :pushpin: Funcionalidades principais
- Registro do usuario
- Login usuario
- Logout do usuario
- Refresh do token

## :man_technologist: Conhecimentos aplicados
- Python
- Flask
- PostegreeSQL
- SQLALchemy
- JWT

## ⚙️ Como Executar
1. Clone o repositório
```bash
git clone https://github.com/karenCLima/flask_api.git 
cd flask_api
```

2. Instale o arquivo requirements.txt
```bash
pip install requirements.txt
```

3. Crie um arquivo `.env` e defina as variáveis
```
FLASK_SECRET_KEY=<your-secret-key>
FLASK_DEBUG=<your-debug-boolean-value>
FLASK_SQLALCHEMY_DATABASE_URI=<your-sqlalchemy-db-uri>
FLASK_SQLALCHEMY_ECHO=<your-sqlalchemy-echo-value>
```

4. Crie uma variável de ambiente `FLASK_APP`. 
```bash
export FLASK_APP=src/
```

5. Crie um banco de dados rodando
```bash
flask shell
```

6. No shell interativo rode os seguintes comandos
```
Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
App: main
Instance: C:\Users\jod35\Documents\coding\JWT Auth flask\instance
>>> from models import User
>>> db.create_all()
```

7. Finalmente rode a aplicação
```flask run```
