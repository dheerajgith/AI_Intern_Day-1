import numpy as np
def create_image(rows, cols):
    return np.random.randint(0, 256, (rows, cols))

def brighten_image(img, increase=50):
    return np.clip(img + increase, 0, 255)

def normalize_image(img):
    return img / 255

def rotate_image(img):
    return np.rot90(img)

def flip_vertical(img):
    return np.flipud(img)

def flip_horizontal(img):
    return np.fliplr(img)

img1=np.random.randint(0,255,(2,2))
img2=np.random.randint(0,255,(5,5))
img3=np.random.randint(0,255,(512,512))
img4= create_image(4,4)

print("Image 1:\n",img1)
# print("Image 2:\n",img2)
# print("Image 3:\n",img3)