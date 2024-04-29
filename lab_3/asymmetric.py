import logging

from enum import Enum

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

logging.basicConfig(filename="lab_3/report.log", filemode="a", level=logging.INFO)


class Mode(Enum):
    """
    The class contains modes for encryption and decryption

    Modes:
        1 - encryption
        0 - decryption
    """
    ENCRYPTION = 1
    DECRYPTION = 0


def asymmetric_method(text: bytes, public_key: rsa.RSAPublicKey, mode: Mode) -> bytes:
    try:
        match mode:
            case Mode.ENCRYPTION:
                return public_key.encrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(), label=None))
            case Mode.DECRYPTION:
                return public_key.encrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(), label=None))
            case _:
                logging.info("Incorrect mode")
    except Exception as e:
        logging.info(f"Error in asymmetric method {e}")