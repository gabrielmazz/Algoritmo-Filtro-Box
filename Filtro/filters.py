import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def aplicar_filtro_box(imagem, i, j):
    
    # Obter as dimensões da imagem
    altura, largura = imagem.shape[:2]
    
    # Criar uma imagem de saída com as mesmas dimensões da imagem original
    imagem_suavizada = np.zeros_like(imagem)
    
    # Calcular o deslocamento para a vizinhança
    deslocamento_i = i // 2
    deslocamento_j = j // 2
    
    # Aplicar o filtro de média
    for x in range(altura):
        for y in range(largura):
            # Definir os limites da ROI
            x_inicio = max(x - deslocamento_i, 0)
            x_fim = min(x + deslocamento_i + 1, altura)
            y_inicio = max(y - deslocamento_j, 0)
            y_fim = min(y + deslocamento_j + 1, largura)
            
            # Extrair a região de interesse (ROI)
            roi = imagem[x_inicio:x_fim, y_inicio:y_fim]
            
            # Calcular a média da ROI
            media = np.mean(roi, axis=(0, 1))
            
            # Atribuir a média ao pixel central na imagem suavizada
            imagem_suavizada[x, y] = media
    
    return imagem_suavizada