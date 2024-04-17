from modules.mylogger.mylogger import MyLogger
from modules.mysql.mysql import MySQL
from controllers.access.simpliss.piracicaba import Simpliss_Access

class SimplissProcedimento():
        
    def __init__(self, 
                 webdriver, user, password, host, database, 
                 column_url, column_login, column_password,
                 id_fluxos, id_status,
                 table_fluxos, table_status, table_credentials, table_sites, table_fluxosweb,
                 param_simpliss, param_true, 
                 input_banner, input_banner_close,
                 input_user, input_password, button_entrar, button_sair
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

        # Metodo de 'INJEÇÃO DE DEPENDENCIA'
        # ref.: https://www.youtube.com/watch?v=5DBfVnQn1Ow

        # Variaveis especificas
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.webdriver = webdriver

        # Colunas
        self.column_url = column_url
        self.column_login = column_login
        self.column_password = column_password
        
        # ID
        self.id_fluxos = id_fluxos
        self.id_status = id_status
                
        # Tabela 
        self.table_fluxos = table_fluxos
        self.table_status = table_status
        self.table_credentials = table_credentials
        self.table_sites = table_sites
        self.table_fluxosweb = table_fluxosweb

        # Parametros
        self.param_true = param_true
        self.param_simpliss = param_simpliss

        # WEB
        self.input_banner = input_banner
        self.input_banner_close = input_banner_close
        self.input_user = input_user
        self.input_password = input_password
        self.button_entrar = button_entrar
        self.button_sair = button_sair
    
    # Função para verificar se existem arquivos com extensão no caminho  
    def procedimento(self):

        # TryCtach
        try:

           # Lista de colunas site e credenciais
            column_url = [self.table_sites, self.column_url]
            column_login = [self.table_credentials, self.column_login]
            column_password = [self.table_credentials, self.column_password]
            column_site_credential = [column_url, column_login, column_password]

            # Lista de filtros
            column_id_fluxos = [self.table_fluxos, self.id_fluxos]
            column_id_status = [self.table_status, self.id_status]
            column_filter_id = [column_id_fluxos, column_id_status]

            # Lista de colunas_filtro
            filter_id = [self.param_simpliss, self.param_true]
            
            # Buscar informações do banco de dados
            status_select_site_credenciais = self.my_sql.mysql_select(
                self.user,
                self.password, 
                self.host,
                self.database,
                self.table_fluxosweb,
                column_site_credential,
                column_filter_id,
                filter_id,
                True
                )

            if status_select_site_credenciais['status']:

                # Retorna a lista de resultados
                resultado = status_select_site_credenciais['resultado']
                print('resultado')
                print(resultado)

                # Atualizar variaveis
                url = resultado[0]
                login = resultado[1]
                password = resultado[2]
                
                print(url)
                print(login)
                print(password)

                for url_count, login_count, password_count in zip(url, login, password):

                    # Parametrizar as funções
                    simpliss_access = Simpliss_Access.SimplissAccess(
                        self.webdriver, self.user, self.password, self.host, self.database, 
                        url_count, login_count, password_count,
                        self.input_banner, self.input_banner_close,
                        self.input_user, self.input_password, self.button_entrar, self.button_sair
                    )

                    # Login
                    status_simpliss_login = simpliss_access.login()

                    if status_simpliss_login['status']:
                    
                        # Logoff
                        status_simpliss_logoff = simpliss_access.logoff()
                        
                        if status_simpliss_logoff['status']:
                            self.status = True
                            print(self.sucesso)

                        else:
                            self.status = False
                            print(self.falha)
                            break

                    else:
                        self.status = False
                        print(self.falha)
                        break
            
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