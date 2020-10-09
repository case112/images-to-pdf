from PIL import Image
image = Image.open('img1.tif')
print(image)
image.save("out.pdf", save_all=True)