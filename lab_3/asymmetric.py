import logging
import os

from enum import Enum

from cryptography.hazmat.primitives import asymmetric, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key

from files import read_file, write_file

logging.basicConfig(filename="report.log", filemode="a", level=logging.INFO)


class Mode(Enum):
    """
    The class contains modes for encryption and decryption

    Modes:
        2 - generate key
        1 - encryption
        0 - decryption
    """
    GENERATE = 2
    ENCRYPTION = 1
    DECRYPTION = 0


def asymmetric_method(text: bytes, key: rsa.RSAPublicKey, mode: Mode) -> bytes:
    try:
        match mode:
            case Mode.ENCRYPTION:
                return key.encrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(), label=None))
            case Mode.DECRYPTION:
                return key.decrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(), label=None))
            case Mode.GENERATE:
                return key.encrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
            case _:
                logging.info("Incorrect mode")
    except Exception as e:
        logging.info(f"Error in asymmetric method {e}")