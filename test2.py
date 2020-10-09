from PIL import Image
from PIL import ImageSequence
import glob

pages = []
for infile in glob.glob("*.tif"):
    page = Image.open(infile)
    pages.append(page.convert("RGB"))
print("opened")
pages[0].save("out.pdf", save_all = True, append_images=pages[1:])