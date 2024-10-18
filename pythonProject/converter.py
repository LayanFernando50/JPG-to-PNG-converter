import os
import sys
from PIL import Image


path = sys.argv[1]
direction = sys.argv[2]

if not os.path.exists(direction):
    os.makedirs(direction)

for names in os.listdir(path):
    img = Image.open(f'{path}{names}')
    clean = os.path.splitext(names)[0]
    img.save(f'{direction}/{clean}.png','png')
    print('all Done Nicely')