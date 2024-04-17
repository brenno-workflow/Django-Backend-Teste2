from modules.mylogger.mylogger import MyLogger
from modules.mysql.mysql import MySQL

class TestesTestes():
        
    def __init__(self, 
                 user, password, host, database,
                 tabela_testes
                 ):

        # Variaveis gerais
        self.status = False
        self.sucesso = f'SUCESSO - {__name__}'
        self.falha = f'FALHA - {__name__}'
        self.erro = f'ERRO - {__name__}'

        # Instancias
        # Instanciar é uma boa prática e necessário
        # Não instaciar resulta na abertura de processo diferentes e erros
        self.my_logger = MyLogger()
        self.my_sql = MySQL()

        # Variaveis especificas
        self.user = user
        self.password = password
        self.host = host
        self.database = database

        # Valores
               
        # Colunas
                
        # Tabela SELECT
        self.tabela_testes = tabela_testes
    
    # Função para verificar se existem arquivos com extensão no caminho  
    def testes_join(self):

        # Variaveis

        # TryCtach
        try:

            # Buscar informações do banco de dados
            status_mysql_join = self.my_sql.mysql_join(
                self.user, 
                self.password,
                self.host, 
                self.database,
                self.tabela_testes
                )

            if status_mysql_join['status']:

                # Retorna a lista de resultados
                resultado = status_mysql_join['resultado']
                print(resultado)

                self.status = True
                print(self.sucesso)
        
            else:
                self.status = False
                print(self.falha)

            # Alimentar o log
            if self.status:
                self.my_logger.log_info(self.sucesso)

            else:
                self.my_logger.log_warn(self.falha)

        except Exception as aviso:
            self.status = False
            print(self.erro)
            print(aviso)

            # Alimentar o log
            self.my_logger.log_error(self.erro)
            self.my_logger.log_error(str(aviso))

        return{'status': self.status}