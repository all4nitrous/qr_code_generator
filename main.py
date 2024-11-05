import os
import qrcode

# Fetch URL from environment variable or use a default
url = os.getenv('QR_DATA_URL', 'https://github.com/all4nitrous')

# QR code generation settings
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Customize colors and file location
fill_color = os.getenv('FILL_COLOR', 'black')
back_color = os.getenv('BACK_COLOR', 'white')
output_dir = os.getenv('QR_CODE_DIR', 'qr_codes')
output_file = os.getenv('QR_CODE_FILENAME', 'my_qr_code.png')

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)
img_path = os.path.join(output_dir, output_file)

# Generate and save the QR code
img = qr.make_image(fill_color=fill_color, back_color=back_color)
img.save(img_path)
print(f"QR code saved to {img_path}")
