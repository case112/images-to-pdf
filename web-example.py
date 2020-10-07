from PIL import Image
import reportlab
import reportlab.lib.pagesizes as pdf_sizes
from io import StringIO
#logging.info("TIFF2PDF")
import numpy as np


def TIFF2PDF(tiff_str, max_pages = 200):
  '''
  Convert a TIFF Image into a PDF.

  tiff_str: The binary representation of the TIFF.
  max_pages: Break after a number of pages. Set to None to have no limit.
  '''

  # Open the Image in PIL
  tiff_img = Image.open('img1.tif')
  #tiff_img = data = np.array(tiff_img)

  # Get tiff dimensions from exiff data. The values are swapped for some reason.
  height, width = tiff_img.tag[0x101][0], tiff_img.tag[0x100][0]

  # Create our output PDF
  out_pdf_io = StringIO()
  c = reportlab.pdfgen.canvas.Canvas(out_pdf_io, pagesize = pdf_sizes.letter)

  # The PDF Size
  pdf_width, pdf_height = pdf_sizes.letter

  # Iterate through the pages
  page = 0
  while True:
    try:
        tiff_img.seek(page)
    except EOFError:
        break
    #logging.info("Converting tiff page: %s"%page)
    # Stretch the TIFF image to the full page of the PDF
    if pdf_width * height / width <= pdf_height:
      # Stretch wide
      c.drawInlineImage(tiff_img, 0, 0, pdf_width, pdf_width * height / width)
    else:
      # Stretch long
      c.drawInlineImage(tiff_img, 0, 0, pdf_height * width / height, pdf_height)
    c.showPage()
    if max_pages and page > max_pages:
      #Slogging.error("Too many pages, breaking early")
      break
    page += 1

  #logging.info("Saving tiff image")
  c.save()
  return out_pdf_io.getvalue()

tiff_img2 = Image.open('img1.tif')
tiff_img2 = np.array(tiff_img2)
TIFF2PDF(tiff_img2)
  