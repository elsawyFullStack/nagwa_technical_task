import qrcode

img = qrcode.make("https://github.com/elsawyFullStack")

img.save('mygithub.jpg')
