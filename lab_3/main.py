import argparse
import json
import logging
import os

from crypto import Cryptography

logging.basicConfig(filename="report.log", filemode="a", level=logging.INFO)


def generate_keys(cryptography: Cryptography, key_size: int) -> None:
    """
    Generate encryption keys of the specified size using the provided Cryptography object

    Args:
        cryptography (Cryptography): an object of the Cryptography class
        key_size (int): the size of the encryption key to be generated
    """
    cryptography.generate_keys(key_size)


def encrypt_text(cryptography: Cryptography, text_path: str, encrypted_path: str) -> None:
    """
    Encrypts text from a file and saves it to a given path

    Args:
        cryptography (Cryptography): an object of the Cryptography class
        text_path (str): the path to the text file to be encrypted
        encrypted_text_path (str): the path to store the encrypted text
    """
    cryptography.encryption(text_path, encrypted_path)


def decrypt_text(cryptography: Cryptography, encrypted_path: str, decrypted_path: str) -> None:
    """
    Decrypts the ciphertext at the given path and stores it at the transmitted path for decryption

    Args:
        cryptography (Cryptography): an object of the Cryptography class
        encrypted_path (str): the path to store the encrypted text
        decrypted_path (str): the path to store the decrypted text
    """
    cryptography.decryption(encrypted_path, decrypted_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Options")
    parser.add_argument(
        "-sk",
        "--symmetric_key",
        type=str,
        help="Path to the symmetric key file")
    parser.add_argument(
        "-pk",
        "--public_key",
        type=str,
        help="Path to public key file")
    parser.add_argument(
        "-prk",
        "--private_key",
        type=str,
        help="Path to private key file")
    parser.add_argument(
        "-json",
        "--jpath",
        type=str,
        default=os.path.join("settings.json"),
        help="Path to json_file")
    parser.add_argument(
        "-option",
        "--opt",
        type=int,
        choices=range(3),
        help="Choose an option: 0 - Encrypt text, 1 - Generate keys, 2 - Decrypt text")
    parser.add_argument(
        "-t",
        "--text",
        type=str,
        help="Path to the text file")
    parser.add_argument(
        "-et",
        "--encrypted_text",
        type=str,
        help="Path to encrypted text file")
    parser.add_argument(
        "-dt",
        "--decrypted_text",
        type=str,
        help="Path to decrypted text file")
    parser.add_argument(
        "-ks",
        "--key_size",
        type=int,
        help="Size of the key to be generated")
    args = parser.parse_args()
    try:
        with open(args.jpath, mode="r", encoding="utf-8") as f:
            settings = json.load(f)
    except Exception as e:
        logging.info(f"Error loading json file {e}")
    cryptography = Cryptography(args.symmetric_key, args.public_key, args.private_key)
    match args.opt:
        case 0:
            encrypt_text(cryptography, args.text, args.encrypted_text)
        case 1:
            generate_keys(cryptography, args.key_size)
        case 2:
            decrypt_text(cryptography, args.encrypted_text, args.decrypted_text)
        case _:
            logging.info("Incorrect option")