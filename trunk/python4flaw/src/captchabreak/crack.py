from PIL import Image

def crackCaptcha(file):
    img = Image.open(file)
    #convert it to black and white
    img = img.convert("L")
    
    #pixdata = img.load()
    # Clean the background noise, if color != black, then set to white.
    #for y in xrange(img.size[1]):
    #    for x in xrange(img.size[0]):
    #        if pixdata[x, y] != (255, 255, 255, 255): #by condition :if not white ,then set it to black
    #            pixdata[x, y] = (0, 0, 0, 0)
    
    img.save("input-black.gif", "GIF")
    
    #&nbsp;&nbsp; Make the image bigger (needed for OCR)
    im_orig = Image.open('input-black.gif')
    big = im_orig.resize((116, 56), Image.NEAREST)
    
    ext = ".tif"
    big.save("input-NEAREST" + ext)
    
    #&nbsp;&nbsp; Perform OCR using pytesser library
    from pytesser import image_to_string
    im = Image.open('input-NEAREST.tif')
    text = image_to_string(im)
    text = text.rstrip()
    print text
    return text

if __name__ == "__main__":
    crackCaptcha("code.jpg")
