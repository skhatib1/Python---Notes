#############
# Getpass
#############

import getpass

username = getpass.getuser()
password = getpass.getpass()
pin = getpass.getpass(prompt="Pin: ")


#############
#BASE64
#############

import base64
text = "Data to be encoded"
hidden_text = base64.b64encode(text.encode())
plaintext = base64.b64decode(hidden_text).decode()


#############
#Fernet
#############

from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
plain_text = "My secret password"
cipher_text = cipher_suite.encrypt(plain_text.encode())
plain_text = cipher_suite.decrypt(cipher_text).decode()
