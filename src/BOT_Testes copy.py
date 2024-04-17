import os

def listar_arquivos_e_pastas(caminho, nivel=0):
    with open('lista_de_arquivos_e_pastas.txt', 'w') as arquivo:
        for pasta_atual, subpastas, arquivos in os.walk(caminho):
            if nivel == 0:
                arquivo.write(f'{os.path.basename(pasta_atual)}\n')
            else:
                arquivo.write(f"{'  ' * nivel}{'|-'}{os.path.basename(pasta_atual)}\n")
            for arquivo_nome in arquivos:
                arquivo.write(f"{'  ' * (nivel+1)}{arquivo_nome}\n")
            for subpasta in subpastas:
                listar_arquivos_e_pastas(os.path.join(pasta_atual, subpasta), nivel + 1)


caminho_da_pasta = r'C:\Users\brossi.brenno\Desktop\Nova pasta\RPA'
listar_arquivos_e_pastas(caminho_da_pasta)
