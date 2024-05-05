import enum
import logging

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

logging.basicConfig(filename="report.log", filemode="a", level=logging.INFO)


class Mode(enum.Enum):
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
    """
    Performs asymmetric encryption, decryption, or key generation using RSA public key

    Args:
        text (bytes): the data to be processed
        key (rsa.RSAPublicKey): the RSA public key used for encryption, decryption, or key generation
        mode (Mode): an enum representing the operation mode (ENCRYPTION, DECRYPTION, or GENERATE)

    Returns:
        bytes: result of the method
    """
    try:
        match mode:
            case Mode.ENCRYPTION:
                return key.encrypt(
                    text,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None))
            case Mode.DECRYPTION:
                return key.decrypt(
                    text,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None))
            case Mode.GENERATE:
                return key.encrypt(
                    text,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None))
            case _:
                logging.info("Incorrect mode")
    except Exception as e:
        logging.info(f"Error in asymmetric method {e}")
