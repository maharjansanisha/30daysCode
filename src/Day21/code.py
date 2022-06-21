import pyqrcode
import png
from pyqrcode import QRCode

print("Enter url to convert")    #url to be converted
s = input(": ")
print("Enter image name to save")  # png file
n = input(": ")
d = n + ".png"                     #extension as .pnf
url = pyqrcode.create(s)           # Creating QR code
url.show()
url.png(d, scale=6)