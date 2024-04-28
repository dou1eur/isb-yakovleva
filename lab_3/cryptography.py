import logging
import os

from cryptography.hazmat.primitives import asymmetric
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization, padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key

from files import write_file, read_file

logging.basicConfig(filename="lab_3/report.log", filemode="a", level=logging.INFO)


class Cryptography:
    def __init__(self, symmetric_key: str, public_key: str, private_key: str) -> None:
        self.symmetric_key = symmetric_key
        self.public_key = public_key
        self.private_key = private_key
    
    def generate_keys(self, key_size: int) -> None:
        if (key_size < 32 | key_size > 442) & key_size % 8 != 0:
            logging.exception("Incorrect key_size")
        symmetric_key = os.random(key_size / 8)
        keys = asymmetric.rsa.generate_private_key(public_exponent=65537, key_size=2048)
        private_key=keys
        public_key = keys.public_key()
        write_file(self.public_key, public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,))
        write_file(self.private_key, private_key.private_bytes(encoding=serialization.Encoding.PEM,
              format=serialization.PrivateFormat.TraditionalOpenSSL,
              encryption_algorithm=serialization.NoEncryption()))
        #Шифрование симметричным алгоритмом + сохранение (Шифровка и расшифровка симметричным методом + асимметричный => 4 функции (по файлам?))
    
    def encryption(self, text_path: str, encryption_path: str) -> None:
        """ 1. decryption for symmetric
        2. encryption text with symmetric algorithm"""

    def decryption(self, encryption_path: str, decryption_path: str) -> None:
        """ 1. decryption for symmetric
        2. decryption text with symmetric algorithm"""
        
