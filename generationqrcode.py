import qrcode

data = 'Black'
img = qrcode.make(data)
img.save('C:/Users/gabriela.carro/Documents/Gabis/Challenge/myqrcode.png')

