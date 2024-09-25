import qrcode

from PIL import Image

qr=qrcode.QRCode(version =1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,border=4)

qr.add_data("https://github.com/yashjhota") # add any thing like image, text wt ever 
qr.make(fit=True)

img=qr.make_image(fill_color= "Green" ,back_color= "white" )

img.save("jhota_github.png")