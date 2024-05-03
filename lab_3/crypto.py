import logging
import os

from cryptography.hazmat.primitives import asymmetric, serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key

from asymmetric import asymmetric_method, Mode
from files import read_file, write_file
from symmetric import decryption_symmetric, encryption_symmetric

logging.basicConfig(filename="report.log", filemode="a", level=logging.INFO)


class Cryptography:

    def __init__(self, symmetric_key: str, public_key: str, private_key: str) -> None:
        self.symmetric_key = symmetric_key
        self.public_key = public_key
        self.private_key = private_key
    
    def generate_keys(self, key_size: int) -> None:
        if (key_size < 32 or key_size > 442) & key_size % 8 != 0:
            logging.exception("Incorrect key_size")
        symmetric_key = os.urandom(key_size // 8)
        keys = asymmetric.rsa.generate_private_key(public_exponent=65537, key_size=2048)
        private_key=keys
        public_key = keys.public_key()
        write_file(self.public_key, public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,))
        write_file(self.private_key, private_key.private_bytes(encoding=serialization.Encoding.PEM,
              format=serialization.PrivateFormat.TraditionalOpenSSL,
              encryption_algorithm=serialization.NoEncryption()))
        encrypted_symmetric_key = asymmetric_method(symmetric_key, public_key, Mode.GENERATE)
        write_file(self.symmetric_key, encrypted_symmetric_key)
    
    def encryption(self, text_path: str, encryption_path: str) -> None:
        key = read_file(self.symmetric_key)
        private_key=load_pem_private_key(read_file(self.private_key), password=None)
        decrypted_key=asymmetric_method(key, private_key, Mode.DECRYPTION)
        text = read_file(text_path)  
        encrypted_text = encryption_symmetric(text, decrypted_key)
        write_file(encryption_path, encrypted_text) 

    def decryption(self, encryption_path: str, decryption_path: str) -> None:
        key = read_file(self.symmetric_key)
        private_key=load_pem_private_key(read_file(self.private_key), password=None)
        decrypted_key=asymmetric_method(key, private_key, Mode.DECRYPTION)
        encrypted_text = read_file(encryption_path)  
        decrypted_text = decryption_symmetric(encrypted_text, decrypted_key)
        write_file(decryption_path, decrypted_text) 
        
