# Chat em Flask

Este repositório contém um **sistema de chat em Flask**, desenvolvido utilizando **Python, HTML, CSS e JavaScript**, com banco de dados **SQLite**. O projeto foi criado para fins educacionais e pode ser utilizado como base para aprendizado e implementações futuras.

## Capturas de Tela

### Tela de Login
![Login](https://github.com/Petinelson/chat1.0-python/blob/main/login.png)

### Tela do Chat
![Chat](https://github.com/Petinelson/chat1.0-python/blob/main/chat.png)


## Tecnologias Utilizadas

- **Flask**: Framework web para Python.
- **Flask-SocketIO**: Permite comunicação em tempo real com WebSockets.
- **SQLite**: Banco de dados leve e eficiente.
- **HTML, CSS, JavaScript**: Interface do chat e interações dinâmicas.
- **Bootstrap**: Estilização responsiva.

## Estrutura do Projeto

```
│   run.py
│
├───controllers
│   │   chat.py
│   │   sql.py
│   │   usuarios.py
│   └───__pycache__
│
├───models
│       banco.db
│       banco.sqbpro
│
├───static
│   ├───scripts
│   │       script.js
│   └───styles
│           estilo.css
│
└───templates
        cadastro.html
        chat.html
        consulta.html
        erro.html
        index.html
```

## Como Usar

### 1. Clonar o repositório
```bash
git clone https://github.com/seu_usuario/seu_projeto.git
cd seu_projeto
```

### 2. Criar um ambiente virtual e instalar dependências
```bash
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Executar o projeto
```bash
python run.py
```
O chat ficará acessível em `http://127.0.0.1:80/`

## Funcionalidades

- **Cadastro e login de usuários**
- **Consulta de usuários cadastrados**
- **Envio de mensagens em tempo real**
- **Sistema de logout**



## Licença

Este projeto é de código aberto e pode ser utilizado livremente para fins educacionais e aprimoramentos.

## Reflexão

> "A comunicação é a chave para conectar o mundo. E na programação, cada linha de código é uma ponte para novas interações."
