from modules.mylogger.mylogger import MyLogger
import requests
from bs4 import BeautifulSoup

class MyRequest:
        
    def __init__(self):

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
        self.request = None
        self.resultado = None
        self.lista_resultado = None

    # Função para buscar os valores da URL
    def requests_get(self, url, tag):

        """
        Módulo para fazer um REQUEST de uma pagina da web.
        Sempre irá retornar uma lista de resultados por coluna -> resultado = [[lista1], [lista2]]

        Args:
            url (str/list): Nome(s) da(s) url(s) para realizar o request.
            filtro (str): Elemento para filtrar no resultado do(s) reuqet(s).
        """

        # Variaveis
        url_list = isinstance(url, list)
        tag_list = isinstance(tag, list)

        # TryCtach
        try:

            # Verificar se existe uma lista de urls
            if url_list:
                urls = url

            else:
                urls = [url]

            if tag_list:
                tags = tag

            else:
                tags = [tag]

            # Gerar lista em branco para resultados
            self.resultado = []

            for elemento in urls:

                # Fazer o request
                self.request = requests.get(elemento)
                print('request - request')
                print(self.request)

                if self.request.status_code == 200:

                    # Obter o conteudo do request
                    resultado = self.request.text
                    print('resultado - request')                
                    print(resultado)

                    # Usar BeautifulSoup para fazer o parsing do HTML
                    # 'html.parser', especifica o parser a ser usado pelo BeautifulSoup para analisar o HTML (padrão do Python para HTML)
                    soup = BeautifulSoup(resultado, 'html.parser')

                    # Localizar a TAG
                    tag_search = soup.find_all(tags[0])
                    print('tag_localizar')
                    print(tag_search)

                    for tag_search_count in tag_search:

                        self.lista_resultado = tag_search_count.text
                        self.resultado.append(self.lista_resultado)

                    self.status = True
                    print(self.sucesso)

                else:
                    self.status = False
                    print(self.falha)

            # Alimentar o log
            if self.status:
                self.my_logger.log_info(self.sucesso)
                self.my_logger.log_info('Sucesso ao fazer o REQUEST GET')

            else:
                self.my_logger.log_warn(self.falha)
                self.my_logger.log_warn('Falha ao fazer o REQUEST GET')

        except Exception as aviso:
            self.status = False
            print(self.erro)
            print(aviso)

            # Alimentar o log
            self.my_logger.log_error(self.erro)
            self.my_logger.log_error('Erro ao fazer o REQUEST GET')
            self.my_logger.log_error(str(aviso))
            
        return{'status': self.status, 'resultado': self.resultado}
    
    # Função para buscar os valores da URL
    def requests_get_old(self, url, filtro):

        """
        Módulo para fazer um REQUEST de uma pagina da web.
        Sempre irá retornar uma lista de resultados por coluna -> resultado = [[lista1], [lista2]]

        Args:
            url (str/list): Nome(s) da(s) url(s) para realizar o request.
            filtro (str): Elemento para filtrar no resultado do(s) reuqet(s).
        """

        # Variaveis
        url_list = isinstance(url, list)

        # TryCtach
        try:

            # Verificar se existe uma lista de urls
            if url_list:

                # Atuvalizar valor da variavel
                urls = url

            else:

                # Criar lista unica
                urls = [url]

            # Gerar lista em branco para resultados
            self.resultado = []

            for elemento in urls:

                # Fazer o request
                self.request = requests.get(elemento)
                print('request - request')
                print(self.request)

                if self.request.status_code == 200:

                    # Obter o conteudo do request
                    resultado = self.request.text
                    print('resultado - request')                
                    print(resultado)

                    # Usar BeautifulSoup para fazer o parsing do HTML
                    # 'html.parser', especifica o parser a ser usado pelo BeautifulSoup para analisar o HTML (padrão do Python para HTML)
                    soup = BeautifulSoup(resultado, 'html.parser')

                    # Localizar a TAG
                    tag_localizar = soup.find_all(filtro)
                    print('tag_localizar')
                    print(tag_localizar)

                    # Lista com os valores das TAGs
                    self.lista_resultado = [count.text for count in tag_localizar]
                    print('self.lista_resultado')
                    print(self.lista_resultado)

                    if self.lista_resultado != []:
                        
                        # Atualizar variavel de resultado
                        self.resultado.append(self.lista_resultado)
                        print('resultado_filtro - request')                
                        print(self.resultado)

                        self.status = True
                        print(self.sucesso)

                    else:
                        self.status = False
                        print(self.falha)

                else:
                    self.status = False
                    print(self.falha)

            # Alimentar o log
            if self.status:
                self.my_logger.log_info(self.sucesso)
                self.my_logger.log_info('Sucesso ao fazer o REQUEST GET')

            else:
                self.my_logger.log_warn(self.falha)
                self.my_logger.log_warn('Falha ao fazer o REQUEST GET')

        except Exception as aviso:
            self.status = False
            print(self.erro)
            print(aviso)

            # Alimentar o log
            self.my_logger.log_error(self.erro)
            self.my_logger.log_error('Erro ao fazer o REQUEST GET')
            self.my_logger.log_error(str(aviso))
            
        return{'status': self.status, 'resultado': self.resultado}
    
     # Função para buscar os valores da URL
    def requests_get_old_2(self, url, tag):

        """
        Módulo para fazer um REQUEST de uma pagina da web.
        Sempre irá retornar uma lista de resultados por coluna -> resultado = [[lista1], [lista2]]

        Args:
            url (str/list): Nome(s) da(s) url(s) para realizar o request.
            filtro (str): Elemento para filtrar no resultado do(s) reuqet(s).
        """

        # Variaveis
        url_list = isinstance(url, list)
        tag_list = isinstance(tag, list)

        # TryCtach
        try:

            # Verificar se existe uma lista de urls
            if url_list:
                urls = url

            else:
                urls = [url]

            if tag_list:
                tags = tag

            else:
                tags = [tag]

            # Gerar lista em branco para resultados
            self.resultado = []

            for elemento in urls:

                # Fazer o request
                self.request = requests.get(elemento)
                print('request - request')
                print(self.request)

                if self.request.status_code == 200:

                    # Obter o conteudo do request
                    resultado = self.request.text
                    print('resultado - request')                
                    print(resultado)

                    # Usar BeautifulSoup para fazer o parsing do HTML
                    # 'html.parser', especifica o parser a ser usado pelo BeautifulSoup para analisar o HTML (padrão do Python para HTML)
                    soup = BeautifulSoup(resultado, 'html.parser')

                    # Começar com a página HTML como o contexto inicial
                    current_context = [soup]

                    # Loop das tags
                    for tag_count in tags:
                        
                        # Contexto dinamico
                        next_context = []

                        # Buscar cada tag na sequência dentro do contexto atual
                        for context_count in current_context:
                            next_context.extend(context_count.find_all(tag_count))

                        # Atualizar o contexto para a próxima iteração
                        current_context = next_context

                    for tag in current_context:

                        resultado_temp = tag.get_text(strip=True)
                        self.resultado.append(resultado_temp)

                        self.status = True
                        print(self.sucesso)

                else:
                    self.status = False
                    print(self.falha)

            # Alimentar o log
            if self.status:
                self.my_logger.log_info(self.sucesso)
                self.my_logger.log_info('Sucesso ao fazer o REQUEST GET')

            else:
                self.my_logger.log_warn(self.falha)
                self.my_logger.log_warn('Falha ao fazer o REQUEST GET')

        except Exception as aviso:
            self.status = False
            print(self.erro)
            print(aviso)

            # Alimentar o log
            self.my_logger.log_error(self.erro)
            self.my_logger.log_error('Erro ao fazer o REQUEST GET')
            self.my_logger.log_error(str(aviso))
            
        return{'status': self.status, 'resultado': self.resultado}