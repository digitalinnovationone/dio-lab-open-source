from pyzbar.pyzbar import decode 
from PIL import Image 

img = Image.open('C:/Users/gabriela.carro/Documents/Gabis/Challenge/myredqrcode.png')

result = decode(img)

print(result)