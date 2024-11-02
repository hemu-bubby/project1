# Image Encryption Project

This project provides simple Python based tool for encrypting and decrypting of an image using crytography.
You can use it to securely encrypt the image so only user with correct key can decrypt it and view it.

#Feature
Encrypt Image: Transform an image file into an encrypted format.
Decrypt Image: Restore an encrypted image back to its original form using a correct key.

#Requirements
Pillow
cryptography

#How to use
Run the encrypt_image code:
type: python encypt_image.py
It will ask to enter the image file path, enter the name of the image with extension.
Make sure the image should be in same directory.
This converts the file into encrypted format.
And produces a key.key file

To decrypt:
Run the decrypt_image.py
type:python decrypt_image.py
It will ask to enter the encrypted image file path, enter the name of the image with extension.
Make sure the encrypted image and key.key file should be in same directory.
This restores the image back to its original form.

**Note**: It requires key (key.key) to decrypt the encrypted image

Project was developed by Hemanth R
https://github.com/hemu-bubby
