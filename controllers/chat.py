from controllers.sql import Banco

class Chat:
    def __init__(self, id_usuario=None, mensagem=None, imagem=None):
        self.id_usuario = id_usuario
        self.mensagem = mensagem
        self.imagem = imagem
        self.banco = Banco()

    def inserir_mensagem(self):
        try:
            dados = {
                'id_usuario': self.id_usuario,
                'mensagem': self.mensagem,
                'imagem': self.imagem  # pode ser None, se não houver imagem
            }
            self.banco.inserir('tb_chat', dados)
            print("Chat.py | Inserir Mensagem | Mensagem cadastrada com sucesso")
        except:
            print("Chat.py | Inserir Mensagem | Erro ao cadastrar mensagem:")

    def consultar_mensagens(self):
        try:
            self.banco.conectar()
            # Realiza um JOIN entre tb_chat e tb_usuarios para obter o nome do usuário
            sql = """
            SELECT tb_chat.id, tb_usuarios.nome_usuario, tb_chat.mensagem, tb_chat.imagem, tb_chat.data_hora 
            FROM tb_chat 
            JOIN tb_usuarios ON tb_chat.id_usuario = tb_usuarios.id 
            ORDER BY tb_chat.data_hora ASC
            """
            self.banco.cursor.execute(sql)
            resultado = self.banco.cursor.fetchall()
            self.banco.desconectar()
            print("Chat.py | Consultar Mensagens | Consultado com sucesso")
            return resultado
        except Exception as e:
            print("Chat.py | Consultar Mensagens | Erro ao consultar mensagens:", e)
            return None

