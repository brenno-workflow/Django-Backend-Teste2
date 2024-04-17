from modules.mylogger.mylogger import MyLogger
from modules.mydriver.mydriver import MyDriver
from modules.myweb.myweb import MyWeb
from controllers.teste import Testes

# Variaveis gerais
status = False
sucesso = f'SUCESSO - {__name__}'
falha = f'FALHA - {__name__}'
erro = f'ERRO - {__name__}'

# Variaveis especificas
user = 'leonardo.vinci'
password = 'BI.ctg2023'
host = 'localhost'
database = 'vincibot_db'

# Valores

# Colunas

# Tabelas
tabela_testes = 'database_fluxosweb'

# Status procedimentos
status_procedimentos = False

# Instancias
# Instanciar é uma boa prática e necessário
# Não instaciar resulta na abertura de processo diferentes e erros
my_logger = MyLogger()
my_driver = MyDriver()

# Metodo de 'INJEÇÃO DE DEPENDENCIA'
# ref.: https://www.youtube.com/watch?v=5DBfVnQn1Ow
my_web = MyWeb(my_driver)
testes = Testes.TestesTestes(
    user, password, host, database, 
    tabela_testes
    )

# TryCtach
try:

    # Procedimentos
    # Testes
    testes_join = testes.testes_join

    # Criar lista de ações a serem executadas
    lista_procedimentos = [
        testes_join
    ]

    # Loop de procediemntos
    for procedimento in lista_procedimentos:

        # Pegar o nome do procedimento
        # VERIFICAR DE USAR O MYNAME PARA ISSO DEPOIS!!!!!!!!!
        procedimento_nome = getattr(procedimento, '__qualname__', str(procedimento))

        # Informar qual arquivo está sendo executado no momento
        my_logger.log_info(f'Iniciando o processo do bot: {procedimento_nome}')
        print(f'Iniciando o processo do bot: {procedimento_nome}')
        
        # Executar procedimentos em ordem
        status_procedimento = procedimento()

        if status_procedimento['status']:
            status = True
            print(sucesso)

        else:
            status = False
            print(falha)
        
        # Alimentar o log
        if status:
            my_logger.log_info(f'Sucesso ao rodar o bot {procedimento_nome}')
            print(f'Sucesso ao rodar o bot {procedimento_nome}')

        else:
            my_logger.log_warn(f'Falha ao rodar o bot {procedimento_nome}')
            print(f'Falha ao rodar o bot {procedimento_nome}')

    # Alimentar o log
    if status:
        my_logger.log_info(sucesso)

    else:
        my_logger.log_warn(falha)

except Exception as aviso:
    status = False
    print(erro)
    print(aviso)

    # Alimentar o log
    my_logger.log_error(erro)
    my_logger.log_error(str(aviso))

# Para fazer uma lista das bibliotecas utilizadas até o momento:
# Abrir um novo terminal
# selecionar o __main__ (bot principal)
# digitar: pip freeze > requirements.txt
# Ira criar um arquivo txt de requerimentos