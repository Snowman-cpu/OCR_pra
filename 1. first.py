from PIL import Image
im_file = "G:\OCR\page_01.jpg"

im = Image.open(im_file)
im.rotate(180).show()
#save an image

# im.save("temp/page_01.png")