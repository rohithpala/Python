import pyqrcode
import png

url = input("Enter the URL: ")

if ("http://" in url) or ("https://" in url):
   # creating qr code
   qr = pyqrcode.create(url)

   # save the qr code as a png file
   try:
      qr.png("qrcode.png", scale=5)
      print("QR code is saved as qrcode.png")
   except:
      print("Error Occurred while creating QR Code")
else:
   print("Invalid URL")
