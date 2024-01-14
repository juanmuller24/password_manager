import base64
import json
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

path = os.getcwd()


def encrypt_aes(username, password):
    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padder.update(password) + padder.finalize()) + encryptor.finalize()
    credentials = {
        "key": base64.b64encode(key).decode('utf-8'),
        "iv": base64.b64encode(iv).decode('utf-8'),
        "ciphertext": base64.b64encode(ciphertext).decode('utf-8')
    }
    credentials_json = json.dumps(credentials, separators=(',', ':'))
    with open(path + f"/data/{username}.json", "w") as f:
        f.write(credentials_json)
    return "Credentials Stored"


def decrypt_aes(key, iv, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    return unpadded_data.decode('utf-8')


class PasswordManager:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def store_data(self, count=0):
        data = [filename for filename in os.listdir(path + "/data")]
        if not data:
            result = encrypt_aes(username=self.username, password=self.password)
            return result
        else:
            for i in data:
                if os.path.splitext(i)[0] == self.username:
                    count += 1
            if count == 1:
                return "Username already exist!!\nUse different Username"
            else:
                result = encrypt_aes(self.username, self.password)
                return result

    def access_password(self):
        count = 0
        data = [filename for filename in os.listdir(path + "/data")]
        for i in data:
            if os.path.splitext(i)[0] == self.username:
                count += 1
        if count == 1:
            with open(path + f"/data/{self.username}.json", "r") as f:
                file_json = json.load(f)
            key_bytes = base64.b64decode(file_json["key"])
            iv_bytes = base64.b64decode(file_json["iv"])
            ciphertext_bytes = base64.b64decode(file_json["ciphertext"])
            result = decrypt_aes(key_bytes, iv_bytes, ciphertext_bytes)

            return f"The password for {self.username} is : {result}"
        else:
            return "Enter valid Username!!"

