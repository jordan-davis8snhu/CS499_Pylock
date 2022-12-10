# Crypto contains the encrypt and decrypt functionality. Also contains the fernet key generation functions

import cryptography
from cryptography.fernet import Fernet


# Generate a fernet key
def gen_key(key_file: str):
    """

    :param key_file: key path
    :return:
    """
    key = Fernet.generate_key()

    with open(key_file, "wb") as f:
        f.write(key)
        f.close()


def read_key(key_file: str):
    """

    :param key_file: key path
    :return:
    """
    with open(key_file, "rb") as f:
        key = f.read()
        f.close()
    return key


class Crypto:

    def __init__(self, path: str, key_file: str):
        """

        :param path: password path
        :param key_file: key path
        """
        self.path = path
        self.key_file = key_file

    def encrypt(self):
        gen_key(self.key_file)

        key = read_key(self.key_file)

        with open(self.path, 'rb') as f:
            data = f.read()
            f.close()

        k = Fernet(key)

        try:
            enc_data = k.encrypt(data)

            with open(self.path, 'wb') as f:
                f.write(enc_data)
                f.close()

            response = 'file encrypted'
            return response

        except cryptography.fernet.InvalidToken:
            response = 'key is invalid'
            return response

    def decrypt(self):

        key = read_key(self.key_file)

        with open(self.path, 'rb') as f:
            data = f.read()

        k = Fernet(key)

        try:
            dec_data = k.decrypt(data)

            with open(self.path, 'wb') as f:
                f.write(dec_data)
                f.close()
            response = 'file decrypted'
            return response

        except cryptography.fernet.InvalidToken:
            response = 'key is invalid'
            return response


