import pyqrcode
qr = pyqrcode.create('Buraya Gitmek İstediğin Linki Alıyoruz')
qr.png('abc.png', scale=8)


