# import modules
import qrcode # for QR code
from PIL import Image #for image generation

QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

#paste the link of the document, make sure document will be on pulic
url = 'https://drive.google.com/file/d/1r-UOv8D-MN_EimgQruElpIC_8b7BrgiF/view?usp=sharing'

# adding URL
QRcode.add_data(url)

#make or generate QR code for document
QRcode.make()

#customize the color of the QR code
QRcolor = 'Blue'

#Add the color feature and background
QRimg = QRcode.make_image(
	fill_color=QRcolor, back_color="white").convert('RGB')

#Save the Image
QRimg.save('Research_Team.png')

#Print
print('QR code generated!')
