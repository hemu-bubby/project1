from cryptography.fernet import Fernet

def load_key():
    return open("key.key", "rb").read()

def decrypt_image(encrypted_image_path):
    with open(encrypted_image_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    key = load_key()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open("decrypted_image.png", "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
    print("Decryption complete. Decrypted image saved as 'decrypted_image.png'.")

if __name__ == "__main__":
    encrypted_image_path = input("Enter the path of the encrypted image to decrypt: ")
    decrypt_image(encrypted_image_path)