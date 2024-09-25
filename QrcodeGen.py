import qrcode as qr

image = qr.make("https://github.com/yashjhota")

image.save("yash_github.png")