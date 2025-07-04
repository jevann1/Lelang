import cv2
import numpy as np
import os
from logic import *
from math import sqrt, ceil, floor

def create_collage(image_paths):
    images = []
    for path in image_paths:
        image = cv2.imread(path)
        images.append(image)

    num_images = len(images)
    num_cols = floor(sqrt(num_images)) # Cari jumlah gambar secara horizontal
    num_rows = ceil(num_images/num_cols)  # Cari jumlah gambar secara vertikal
    # Membuat kolase kosong
    collage = np.zeros((num_rows * images[0].shape[0], num_cols * images[0].shape[1], 3), dtype=np.uint8)
    # Menempatkan gambar pada kolase
    for i, image in enumerate(images):
        row = i // num_cols
        col = i % num_cols
        collage[row*image.shape[0]:(row+1)*image.shape[0], col*image.shape[1]:(col+1)*image.shape[1], :] = image
    return collage


m = DatabaseManager(DATABASE)
info = m.get_winners_img("user_id")
prizes = [x[0] for x in info]
image_paths = os.listdir('img')
image_paths = [f'img/{x}' if x in prizes else f'hidden_img/{x}' for x in image_paths]
collage = create_collage(image_paths)

cv2.imshow('Collage', collage)
cv2.waitKey(0)
cv2.destroyAllWindows()