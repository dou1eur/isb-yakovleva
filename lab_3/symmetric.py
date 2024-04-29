import os
import logging

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

logging.basicConfig(filename="lab_3/report.log", filemode="a", level=logging.INFO)


def encryption_symmetric(text: bytes, key: bytes) -> bytes:
    iv = os.urandom(8)
    try: 
        cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        padder = padding.ANSIX923(len(key) * 8).padder()
        padded_text = padder.update(text) + padder.finalize()
        c_text = iv + encryptor.update(padded_text) + encryptor.finalize()
    except Exception as e:
        logging.info(f"Error in enc symmetric {e}")
    return c_text

def decryption_symmetric(text: bytes, key: bytes) -> bytes:
    iv = text[:8]
    text = text[8:]
    try:
        cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(text) + decryptor.finalize()
        unpadder = padding.ANSIX923(len(key) * 8).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()
    except Exception as e:
        logging.info(f"Error in dec symmetric {e}")
    return unpadded_dc_text