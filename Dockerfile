# Base image with Python
FROM python:3.9-slim

# Set working directory
WORKDIR /qr_code_generator

# Copy app file to working directory
COPY main.py .

# Install dependencies
RUN pip install qrcode[pil]

# Set environment variables (if needed)
ENV QR_DATA_URL="https://github.com/all4nitrous"
ENV QR_CODE_DIR="qr_codes"
ENV QR_CODE_FILENAME="my_qr_code.png"
ENV FILL_COLOR="black"
ENV BACK_COLOR="white"

# Execute Python script
CMD ["python", "main.py"]

