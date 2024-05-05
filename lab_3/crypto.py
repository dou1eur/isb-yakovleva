import logging
import os

from cryptography.hazmat.primitives import asymmetric, serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key

from asymmetric import asymmetric_method, Mode
from files import read_file, write_file
from symmetric import decryption_symmetric, encryption_symmetric

logging.basicConfig(filename="report.log", filemode="a", level=logging.INFO)


class Cryptography:
    """
    A class for handling encryption and decryption using symmetric and asymmetric algorithms

    Methods:
        generate_keys (self, key_size: int) -> None
        encryption (self, text_path: str, encryption_path: str) -> None
        decryption(self, encryption_path: str, decryption_path: str) -> None
    """

    def __init__(self, symmetric_key: str, public_key: str, private_key: str) -> None:
        """
        Initialize the Cryptography object with the provided key file paths

        Args:
            symmetric_key (str): the path to the file storing the symmetric key
            public_key (str): the path to the file storing the public key
            private_key (str): the path to the file storing the private key
        """
        self.symmetric_key = symmetric_key
        self.public_key = public_key
        self.private_key = private_key

    def generate_keys(self, key_size: int) -> None:
        """
        Generate symmetric and asymmetric keys of the specified size and store them in files

        Args:
            key_size (int): the size of the key to be generated
        """
        if (key_size < 32 | key_size > 442) & key_size % 8 != 0:
            logging.exception("Incorrect key_size")
        symmetric_key = os.urandom(key_size // 8)
        keys = asymmetric.rsa.generate_private_key(public_exponent=65537, key_size=2048)
        private_key = keys
        public_key = keys.public_key()
        write_file(
            self.public_key,
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo))
        write_file(
            self.private_key,
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()))
        encrypted_symmetric_key = asymmetric_method(symmetric_key, public_key, Mode.GENERATE)
        write_file(self.symmetric_key, encrypted_symmetric_key)

    def encryption(self, text_path: str, encryption_path: str) -> None:
        """
        Encrypt a text file using the stored keys and store the encrypted text in a file

        Args:
            text_path (str): the path to the text file to be encrypted
            encryption_path (str): the path to store the encrypted text
        """
        key = read_file(self.symmetric_key)
        private_key = load_pem_private_key(read_file(self.private_key), password=None)
        decrypted_key = asymmetric_method(key, private_key, Mode.DECRYPTION)
        text = read_file(text_path)
        encrypted_text = encryption_symmetric(text, decrypted_key)
        write_file(encryption_path, encrypted_text)

    def decryption(self, encryption_path: str, decryption_path: str) -> None:
        """
        Decrypt an encrypted text file using the stored keys and store the decrypted text in a file

        Args:
            encryption_path (str): the path to the encrypted text file
            decryption_path (str): the path to store the decrypted text
        """
        key = read_file(self.symmetric_key)
        private_key = load_pem_private_key(read_file(self.private_key), password=None)
        decrypted_key = asymmetric_method(key, private_key, Mode.DECRYPTION)
        encrypted_text = read_file(encryption_path)
        decrypted_text = decryption_symmetric(encrypted_text, decrypted_key)
        write_file(decryption_path, decrypted_text)
