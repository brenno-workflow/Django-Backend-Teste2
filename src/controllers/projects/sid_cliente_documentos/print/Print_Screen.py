from modules.mylogger.mylogger import MyLogger
from controllers.projects.sid_cliente_documentos.web.sid.cliente import SID_Print
import datetime

class PrintScreen():
        
    def __init__(self, 
                 webdriver, user, password, host, database,
                 column_control_path, 
                 id_status, id_fluxos, 
                 table_status, table_fluxos, table_control, table_fluxoscontrol,
                 param_true, param_control_sid_cliente_sucesso, param_control_sid_cliente_falha, param_control_sid_cliente_erro,
                 extension_png
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

        # Variaveis especificas
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.webdriver = webdriver

        # Extensões
        self.extension_png = extension_png

        # Colunas
        self.column_control_path = column_control_path
        
        # ID
        self.id_fluxos = id_fluxos
        self.id_status = id_status
                
        # Tabela 
        self.table_fluxos = table_fluxos
        self.table_status = table_status
        self.table_control = table_control
        self.table_fluxoscontrol = table_fluxoscontrol

        # Parametros
        self.param_true = param_true
        self.param_control_sid_cliente_sucesso = param_control_sid_cliente_sucesso
        self.param_control_sid_cliente_falha = param_control_sid_cliente_falha
        self.param_control_sid_cliente_erro = param_control_sid_cliente_erro
    
    # Função para verificar se existem arquivos com extensão no caminho  
    def print_screen(self):

        # Variaveis
        file_name = datetime.datetime.now()
        folder_name = 'Falha'

        # TryCtach
        try:

            # Criar pasta de controle
            sid_print = SID_Print.SIDPrint(
                self.webdriver, self.user, self.password, self.host, self.database, 
                file_name, folder_name,
                self.column_control_path, 
                self.id_status, self.id_fluxos, 
                self.table_status, self.table_fluxos, self.table_control, self.table_fluxoscontrol,
                self.param_true, self.param_control_sid_cliente_sucesso, self.param_control_sid_cliente_falha, self.param_control_sid_cliente_erro,
                self.extension_png
            )

            status_sid_print = sid_print.print('falha')

            if status_sid_print['status']:
                self.status = True
                mensagem = f'Sucesso ao tirar o PRINT da tela de falha geral.'
                print(mensagem)

            else:
                self.status = False
                mensagem = f'Falha ao tirar o PRINT da tela de falha geral.'
                print(mensagem)

            # Alimentar o log
            if self.status:
                self.my_logger.log_info(self.sucesso)
                self.my_logger.log_info(mensagem)

            else:
                self.my_logger.log_warn(self.falha)
                self.my_logger.log_warn(mensagem)

        except Exception as aviso:
            self.status = False
            mensagem = f'Erro ao tirar o PRINT da tela de falha geral.'
            print(self.erro)
            print(mensagem)
            print(aviso)

            # Alimentar o log
            self.my_logger.log_error(self.erro)
            self.my_logger.log_error(mensagem)
            self.my_logger.log_error(str(aviso))

        return{'status': self.status}