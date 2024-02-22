import json
import logging
import os
import re


logging.basicConfig(filename="lab_1/report.log", filemode="a", level=logging.INFO)


def get_key(keyword: str, alphabet: str, path: str) -> dict:
    """The function receives a word, each letter
    of which is replaced by the corresponding
    number in the table"""
    key = {}
    for i, char in enumerate(keyword):
        key[i] = alphabet.index(char)
    get_dict(key, path)
    logging.info("func get_key work")
    return key


def vigenere_chipher(
    path: str, new_path: str, alphabet: str, key: dict, mode: bool
) -> str:
    """Encryption and decryption function using Vigenere method:
    mode = True  - encryption
    mode = False - decryption
    """
    text = read_file(path)
    chipher = ""
    try:
        for i, char in enumerate(text):
            if char in alphabet:
                char_idx = alphabet.index(char)
                keyword_idx = i % len(key)
                shift = key[keyword_idx]
                if mode == True:
                    chipher_idx = (char_idx + shift) % len(alphabet)
                elif mode == False:
                    chipher_idx = (char_idx - shift) % len(alphabet)
                chipher_char = alphabet[chipher_idx]
                chipher += chipher_char
            else:
                chipher += char
        logging.info(f"func vigenere_chipher work mode:{mode}")
    except Exception as e:
        logging.error(f"error in enc/decr {e}")
    write_file(new_path, chipher)
    return chipher


def read_file(path: str) -> str:
    """Function to read file contents"""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    logging.info("read_file")
    return text


def write_file(path: str, text: str) -> None:
    """Function for recording the result of the Vigenere method"""
    new_file = open(path, "w", encoding="utf-8")
    new_file.write(text)
    new_file.close()
    logging.info("write_file")


def formatting_text(path: str) -> None:
    """Function for formatting text"""
    try:
        text = read_file(path)
        upper_text = str.upper(text)
        format_text = re.sub("\W+", " ", upper_text)
        write_file(path, format_text)
        logging.info("formatting")
    except Exception as e:
        logging.error(f"error in formatting {e}")


def get_dict(dict: dict, path: str) -> None:
    with open(path, "w", encoding="utf-8") as json_f:
        json.dump(dict, json_f, ensure_ascii=False)


if __name__ == "__main__":
    with open(os.path.join("lab_1", "settings.json"), "r", encoding="utf-8") as json_f:
        settings = json.load(json_f)
    key = get_key(
        settings["keyword"],
        settings["alphabet"],
        os.path.join(settings["dir"], settings["keyword_dict"]),
    )
    vigenere_chipher(
        (os.path.join(settings["dir"], settings["txt"])),
        os.path.join(settings["dir"], settings["encryption"]),
        settings["alphabet"],
        key,
        settings["mode"],
    )
    vigenere_chipher(
        (os.path.join(settings["dir"], settings["encryption"])),
        os.path.join(settings["dir"], settings["decryption"]),
        settings["alphabet"],
        key,
        settings["mode"],
    )
