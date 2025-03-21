from flask import Flask, render_template, redirect, request, session
from controllers.usuarios import Usuario
from controllers.sql import Banco
from flask_socketio import SocketIO
from datetime import datetime
from controllers.chat import Chat

app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = 'chat'

# Rotas
# ------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

# ------------------------------------------------------
@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        usuario = Usuario(
            request.form.get('nome_login_reg'),
            request.form.get('senha_reg'),
            request.form.get('nome_usuario'),
            request.form.get('email_reg')
        )
        
        try:
            usuario.inserir_dados()
            socketio.emit('novo_usuario')
            return redirect('/')  
        except Exception as e:
            return render_template('erro.html', erro="Impossível cadastrar o usuário")
    return render_template('cadastro.html')

# ------------------------------------------------------
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        usuario = Usuario()
        verificar = usuario.validar_login(request.form.get('username'), request.form.get('password'))
        if verificar:            
            session['usuario'] = verificar 
                         
            return redirect('/chat')
        else:
            return render_template('erro.html', erro="Usuário ou senha incorretos")
    return render_template('index.html')

# ------------------------------------------------------
@app.route('/consulta', methods=['POST', 'GET'])
def consulta():
    usuario = Usuario()
    return render_template('consulta.html', usuarios=usuario.consultar_dados())

# ------------------------------------------------------
@app.route('/chat')
def chat():
    if 'usuario' not in session:
        return redirect('/')
    usuario = session.get('usuario', [])
    chat_obj = Chat()
    todas_mensagens = chat_obj.consultar_mensagens()    
    return render_template('chat.html', mensagens=todas_mensagens, usuario=usuario)

# ------------------------------------------------------
@app.route('/enviar_chat', methods=['POST'])
def enviar_chat():
    usuario_data = session.get('usuario', [])
    if usuario_data:
        id_usuario = usuario_data[0]
        nome_usuario = usuario_data[3]
    else:
        id_usuario = request.form.get('id_usuario')
        nome_usuario = request.form.get('nome_usuario', 'Anônimo')
    
    mensagem = request.form.get('mensagem')
    
    
    chat = Chat(id_usuario=id_usuario, mensagem=mensagem)
    chat.inserir_mensagem()
    
    
    data = {
        'sender': nome_usuario,
        'message': mensagem,
        'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    
    socketio.emit('nova_mensagem', data)
    
    return redirect('/chat')

# ------------------------------------------------------
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect('/')

# ------------------------------------------------------
if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=80, debug=True)
