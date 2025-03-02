import matplotlib.pyplot as plt
import argparse
from rich.console import Console
from rich.prompt import Prompt
import Filtro.filters as filters
import Utils.utils_imagem as ut_img

# Variáveis para passagem de argumentos via terminal
parser = argparse.ArgumentParser()

# Argumento para salvar a imagem na pasta de resultados
SAVE = parser.add_argument('--save', action='store_true', help='Salvar a imagem na pasta de resultados')

def filtro_box(imagem_escolhida, tipo):
    
    # Tamanhos do filtro
    tamanhos = [2, 3, 5, 7]
    
    # Dicionário para armazenar as imagens binarizadas
    Imagens_Binarias = {}
    
    # Leitura da imagem
    Imagem_Original = ut_img.leitura_Imagem('./imagens/{}'.format(imagem_escolhida))    

    for tamanho in tamanhos:
        Imagens_Binarias['{}'.format(tamanho)] = filters.aplicar_filtro_box(Imagem_Original, tamanho, tamanho)
    
    # Realiza a plotagem das imagens
    ut_img.plotagem_imagem(Imagem_Original, Imagens_Binarias['2'], Imagens_Binarias['3'], Imagens_Binarias['5'], Imagens_Binarias['7'])
    
    # Salva a imagem na pasta de resultados
    #if SAVE:
        #ut_img.salvar_imagem(Imagem_Binaria, './resultados/{}_{}_{}_{}x{}.png'.format(tipo,imagem,filtro,m,n))

if __name__ == '__main__':
    
    # Inicializa a console
    console = Console()
    
    # Lista as imagens disponíveis na pasta
    imagens_disponiveis = ut_img.lista_imagens_pasta('./imagens', console)
    
    # Escolhe uma imagem para aplicar o método de Otsu
    imagem_escolhida = ut_img.escolher_imagens(imagens_disponiveis, console)
        
    filtro_box(imagem_escolhida, 'average')