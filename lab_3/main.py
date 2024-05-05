import argparse
import json
import logging
import os

from crypto import Cryptography

from asymmetric import Mode

logging.basicConfig(filename="report.log", filemode="a", level=logging.INFO)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Options")
    parser.add_argument(
        "-json",
        "--jpath",
        type=str,
        default=os.path.join("settings.json"),
        help="Path to json_file")
    parser.add_argument(
        "-m",
        "--mode",
        type=int,
        default=Mode.DECRYPTION,
        choices=range(3),
        help="0 - Decryption, 1 - Encryption, 2 - Generate")
    args = parser.parse_args()
    try:
        with open(args.jpath, mode="r", encoding="utf-8") as f:
            settings = json.load(f)
    except Exception as e:
        logging.info(f"Error loading json file {e}")
    сryptography = Cryptography(
        os.path.join(settings["key_folder"], settings["symmetric_key"]),
        os.path.join(settings["key_folder"], settings["public_key"]),
        os.path.join(settings["key_folder"], settings["private_key"]))
    match args.mode:
        case Mode.DECRYPTION:
            сryptography.decryption(
                os.path.join(settings["text_folder"], settings["enc_text"]),
                os.path.join(settings["text_folder"], settings["dec_text"]))
        case Mode.ENCRYPTION:
            сryptography.encryption(
                os.path.join(settings["text_folder"], settings["text"]),
                os.path.join(settings["text_folder"], settings["enc_text"]))
        case Mode.GENERATE:
            сryptography.generate_keys(settings["key_size"])
        case _:
            logging.info("Incorrect mode")
