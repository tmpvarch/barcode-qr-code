import qrcode
from barcode import generate
from barcode.writer import ImageWriter

def generate_barcode(data, code_type, file_name: str):
    generate(code_type, data, output=file_name, writer=ImageWriter())

def generate_qr_code(data, filename: str):
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=2,
    )
    qr.add_data(data)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename + '.png')

def main():
    with open('data.txt', 'r') as f:
        data = f.read()
    generate_qr_code(data, 'qr_code')
    data = '4690228034183>'
    generate_barcode(data, 'code128', 'barcode')


if __name__ == '__main__':
    main()