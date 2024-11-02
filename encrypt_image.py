from cryptography.fernet import Fernet
from PIL import Image
import io

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as 'key.key'")
    return key

def load_key():
    return open("key.key", "rb").read()

def encrypt_image(image_path):
    with open(image_path, "rb") as image_file:
        original_image_data = image_file.read()
    try:
        key = load_key()
    except FileNotFoundError:
        key = generate_key()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(original_image_data)
    with open("encrypted_image.enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print("Encryption complete. Encrypted image saved as 'encrypted_image.enc'.")

if __name__ == "__main__":
    image_path = input("Enter the path of the image to encrypt: ")
    encrypt_image(image_path)