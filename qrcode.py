
#simple qrcode
import qrcode as qr
img = qr.make('My name is akash')
img.save('myself.jpeg')
***change the commit message successfully***

#advance qrcode with beautiful editing 
# second pull request for testing purpose.
import qrcode
from PIL import Image
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=4)

qr.add_data('My name is akash')
qr.make(fit=True)
#in make_image you can set background color,you can set qrcode color and also length and width of image
img = qr.make_image()
img.save('yourself.jpg')
