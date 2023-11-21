import qrcode
from barcode import generate
from barcode.writer import ImageWriter

def make_qr(text):
    qr_code = qrcode.QRCode(version=1, box_size=10, border=4,
                            error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr_code.add_data(text)
    qr_code.make(fit=True)
    img = qr_code.make_image(fill_color="black", back_color="white")
    img.save('qr_code.png')


if __name__ == "__main__":
    text = 'enter_your_text'
    make_qr(text)
    generate('code128', text, output='barcode', writer=ImageWriter())
