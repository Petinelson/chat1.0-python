from controllers.sql import Banco

class Usuario:
    def __init__(self, usuario = None, senha = None, nome_usuario = None, email = None, ):
        self.usuario = usuario
        self.email = email
        self.senha = senha
        self.nome_usuario = nome_usuario
        self.banco = Banco()

    def inserir_dados(self):
        try:
            dados = {
                'usuario' : self.usuario,
                'email': self.email,
                'senha' : self.senha,
				'nome_usuario' : self.nome_usuario
            }
            self.banco.inserir('tb_usuarios', dados)
            print("Usuario.py | Inserir Dados | Cadastrado com sucesso")
        except:
            print("Usuario.py | Inserir Dados | Erro ao cadastrar")
    
    def consultar_dados(self):
        try:
            dados = self.banco.consultar('tb_usuarios')
            print("Usuario.py | Consultar Dados | Consultado com sucesso")
            return dados
        except:
            print("Usuario.py | Consultar Dados | Erro ao consultar")
    
    def validar_login(self, usuario, senha):
        try:
            resultado = self.banco.consultar_login('tb_usuarios', usuario, senha)
            if resultado:
                print("Usuario.py | Validar Login | Login realizado com sucesso")
                return resultado  # Retorna os dados completos do usuário
            else:
                print("Usuario.py | Validar Login | Credenciais inválidas")
                return None
        except:
            print("Usuario.py | Validar Login | Erro ao validar login:")
            return None

