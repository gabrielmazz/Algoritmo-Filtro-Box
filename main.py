import matplotlib.pyplot as plt
import argparse
from rich.console import Console
from rich.prompt import Prompt
from rich.progress import Progress
import Filtro.filters as filters
import Utils.utils_imagem as ut_img
import Utils.utils_code as ut_code
import time
import Utils.library_checker as lib_checker

# Variáveis para passagem de argumentos via terminal
parser = argparse.ArgumentParser()

# Argumento para salvar a imagem na pasta de resultados
SAVE = parser.add_argument('--save', action='store_true', help='Salvar a imagem na pasta de resultados')
INFO = parser.add_argument('--info', action='store_true', help='Exibir o tempo de execução')
URL_IMAGE = parser.add_argument('--url', type=str, help='URL da imagem para usar no algoritmo')

def filtro_box(imagem_escolhida, tipo):
    
    # Inicializa o tempo de execução
    start_time = time.time()
    
    with Progress() as progress:
        
        # Atualiza o progresso
        task = progress.add_task("[cyan]Processando...", total=7)
        
        # Tamanhos do filtro
        progress.update(task, advance=1, description='[cyan]Definindo tamanhos do filtro...')
        tamanhos = [2, 3, 5, 7]
        
        time.sleep(1)
        
        # Dicionário para armazenar as imagens binarizadas
        Imagens_Binarias = {}
        
        # Leitura da imagem
        progress.update(task, advance=1, description='[cyan]Lendo a imagem...')
        Imagem_Original = ut_img.leitura_Imagem('./imagens/{}'.format(imagem_escolhida))    

        time.sleep(1)


        for tamanho in tamanhos:
            progress.update(task, advance=1, description='[cyan]Aplicando filtro Box {}x{}...'.format(tamanho, tamanho))
            Imagens_Binarias['{}'.format(tamanho)] = filters.aplicar_filtro_box(Imagem_Original, tamanho, tamanho)
        
        # Realiza a plotagem das imagens
        progress.update(task, advance=1, description='[green]Plotando as imagens...')
        ut_img.plotagem_imagem(Imagem_Original, Imagens_Binarias['2'], Imagens_Binarias['3'], Imagens_Binarias['5'], Imagens_Binarias['7'])
    
    # Salva a imagem na pasta de resultados
    if args.save:
        for tamanho in tamanhos:
            ut_img.salvar_imagem(Imagens_Binarias['{}'.format(tamanho)], './resultados/{}_box_{}x{}.png'.format(imagem_escolhida.split('.')[0], tamanho, tamanho))
        
    if args.info:
        ut_code.print_infos(time.time() - start_time, tipo, imagem_escolhida)
        
    if args.url:
        ut_img.deletar_imagem(imagem_escolhida)
    
    
if __name__ == '__main__':
    
    # Verifica se os argumentos foram passados corretamente
    args = parser.parse_args()
    
    # Verifica se as bibliotecas necessárias estão instaladas
    lib_checker.check_library()
    
    ut_code.clear_terminal()
    ut_code.print_title()
    
    if args.url:
        ut_img.download_imagem(args)
    
    # Inicializa a console
    console = Console()
    
    # Lista as imagens disponíveis na pasta
    imagens_disponiveis = ut_img.lista_imagens_pasta('./imagens', console)
    
    # Escolhe uma imagem para aplicar o método de Otsu
    imagem_escolhida = ut_img.escolher_imagens(imagens_disponiveis, console)
        
    filtro_box(imagem_escolhida, 'average')