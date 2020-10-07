from PIL import Image
import numpy as np

img = Image.open('img1.tif')
data = np.array(img)

print(data) 