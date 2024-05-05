import os
import logging

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

logging.basicConfig(filename="report.log", filemode="a", level=logging.INFO)


def encryption_symmetric(text: bytes, key: rsa.RSAPublicKey) -> bytes:
    """
    Encrypts text using symmetric encryption

    Args:
        text (bytes): the text to be encrypted
        key (rsa.RSAPublicKey): the public key for encryption

    Returns:
        bytes: the encrypted text
    """
    try: 
        padder = padding.ANSIX923(64).padder()
        padded_text = padder.update(text) + padder.finalize()
        iv = os.urandom(8)
        cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text = iv + encryptor.update(padded_text) + encryptor.finalize()
    except Exception as e:
        logging.info(f"Error in enc symmetric {e}")
    return c_text


def decryption_symmetric(text: bytes, key: rsa.RSAPublicKey) -> bytes:
    """
    Decrypts text using symmetric decryption

    Args:
        text (bytes): the text to be decrypted
        key (rsa.RSAPublicKey): the public key for decryption

    Returns:
        bytes: the decrypted text
    """
    try:
        iv = text[:8]
        text = text[8:]
        cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(text) + decryptor.finalize()
        unpadder = padding.ANSIX923(64).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()
    except Exception as e:
        logging.info(f"Error in dec symmetric {e}")
    return unpadded_dc_text