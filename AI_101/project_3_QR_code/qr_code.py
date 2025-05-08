import qrcode
from PIL import Image
import cv2

# Function to encode data into a QR code
def generate_qr(data, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR Code generated and saved as {filename}")

# Function to decode QR code from image
def decode_qr(filename):
    img = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, vertices_array, _ = detector.detectAndDecode(img)

    if vertices_array is not None:
        print("Decoded data:", data)
        return data
    else:
        print("QR Code not detected")
        return None

# Example usage
if __name__ == "__main__":
    # Encoding
    data_to_encode = "https://openai.com"
    generate_qr(data_to_encode, "my_qr.png")

    # Decoding
    decode_qr("my_qr.png")
    
