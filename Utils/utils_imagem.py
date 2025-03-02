import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from rich.console import Console
from rich.prompt import Prompt
import os
import cv2

# Leitura da imagem
def leitura_Imagem(nome):
    
    imagem = mpimg.imread(nome)
    
    return imagem

# Realiza a plotagem das imagens com o matplotlib
def plotagem_imagem(Imagem_Original, Imagem_Binaria2x2, Imagem_Binaria3x3, Imagem_Binaria5x5, Imagem_Binaria7x7):
    
    # Cria a figura com os subplots
    fig, axs = plt.subplots(1, 5, figsize=(20, 10))
    
    # Adiciona as imagens nos subplots
    axs[0].imshow(Imagem_Original, cmap='Greys')
    axs[0].set_title('Imagem Original')
    
    axs[1].imshow(Imagem_Binaria2x2, cmap='Greys')
    axs[1].set_title('Filtro Box 2x2')
    
    axs[2].imshow(Imagem_Binaria3x3, cmap='Greys')
    axs[2].set_title('Filtro Box 3x3')
    
    axs[3].imshow(Imagem_Binaria5x5, cmap='Greys')
    axs[3].set_title('Filtro Box 5x5')
    
    axs[4].imshow(Imagem_Binaria7x7, cmap='Greys')
    axs[4].set_title('Filtro Box 7x7')
    
    # Remove os eixos dos subplots
    for ax in axs.flat:
        ax.set(xticks=[], yticks=[])
    
    # Mostra a figura com os subplots
    plt.show()
    
def salvar_imagem(Imagem_Binaria, nome):
    
    plt.imsave(nome, Imagem_Binaria, cmap='Greys')
    
def lista_imagens_pasta(pasta, console):
    
    # Lista as imagens disponíveis na pasta
    imagens = [f for f in os.listdir(pasta)]
    
    # Printa as imagens
    for i, imagem in enumerate(imagens):
        console.print('{}. {}'.format(i+1, imagem))
        
    return imagens

def escolher_imagens(imagens, console):
    
    # Escolhe uma imagem para aplicar o filtro Box
    while True:
        escolha = int(Prompt.ask('Escolha uma imagem para aplicar o [bold purple]Filtro Box[/bold purple]:', console=console))
        
        if escolha > 0 and escolha <= len(imagens):
            return imagens[escolha-1]
        else:
            console.print('Escolha inválida. Tente novamente.')
    