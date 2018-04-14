import pytesseract
try:
    import Image
except ImportError:
    from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Kingsley\\Dropbox\\Kingsley\\Project\\Scraper'

print(pytesseract.image_to_string(Image.open('testImage.jpg')))
