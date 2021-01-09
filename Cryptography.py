# cryptography library / module installed using pip
# You may turn-on Python CLI or simply run this program

# importing Fernet from cryptography
from cryptography.fernet import Fernet

# this key shall be used to encrypt and decrypt
key = Fernet.generate_key()

f = Fernet(key)

# encrypting the message
encrypted = f.encrypt(b"Thanks to God for everything.")

encrypted

# Here, your encoded message is printed , like ... 6uyfYn_v8b5bBzNTZj ....

# decrypting the message encrypted earlier with the same key
f.decrypt(encrypted)

# Message being decoded using the encrypted token
'Thanks to God for everything.'
