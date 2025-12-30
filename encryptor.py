import random
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()
key.remove(" ")
random.shuffle(key)

#Encryption

plain_text = input("Enter a Message to Encrypt: ")
cipher_text = ""
for letter in plain_text:
    indexes = chars.index(letter)
    cipher_text += key[indexes]
print(f"Encrypted Text: {cipher_text}")

#Decryption

cipher_text = input("Enter a Message to Decrypt: ")
plain_text = ""
for letter in cipher_text:
    indexes = key.index(letter)
    plain_text += chars[indexes]
print(f"Decrypted Text: {plain_text}")
