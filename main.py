import matplotlib.pyplot as plt
import argparse
from rich.console import Console
from rich.prompt import Prompt
import filters
import Utils.utils_imagem as ut_img

# Variáveis para passagem de argumentos via terminal
parser = argparse.ArgumentParser()

# Argumento para salvar a imagem na pasta de resultados
SAVE = parser.add_argument('--save', action='store_true', help='Salvar a imagem na pasta de resultados')

def filtro_box(imagem_escolhida, tipo):
    
    # Leitura da imagem
    Imagem_Original = ut_img.leitura_Imagem('./imagens/{}'.format(imagem_escolhida))    

    # Binarização da imagem com o método do filto box
    Imagem_Binaria2x2 = filters.apply_box_filter(Imagem_Original, 2, 2, 2)
    Imagem_Binaria3x3 = filters.apply_box_filter(Imagem_Original, 3, 3, 3)
    Imagem_Binaria5x5 = filters.apply_box_filter(Imagem_Original, 5, 5, 5)
    Imagem_Binaria7x7 = filters.apply_box_filter(Imagem_Original, 7, 7, 7)
    
    print(f"Contents of Imagem_Binaria3x3: {Imagem_Binaria3x3}")

    print(f"Contents of Imagem_Binaria5x5: {Imagem_Binaria5x5}")
    
    
    # Realiza a plotagem das imagens
    #ut_img.plotagem_imagem(Imagem_Original, Imagem_Binaria2x2, Imagem_Binaria3x3, Imagem_Binaria5x5, Imagem_Binaria7x7)
    
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