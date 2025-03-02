import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def apply_box_filter(image, width, height, kernel_size):
    
    """Aplica um filtro de média (Box Filter) manualmente."""
    offset = kernel_size // 2
    new_image = [[0] * width for _ in range(height)]

    for y in range(offset, height - offset):
        for x in range(offset, width - offset):
            total = 0
            count = 0
            
            for ky in range(-offset, offset + 1):
                for kx in range(-offset, offset + 1):
                    total += image[y + ky][x + kx]
                    count += 1

            new_image[y][x] = total // count  # Média dos valores dentro do kernel

    return new_image