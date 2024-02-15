import os
import logging
import json
from chipher import write_file,read_file,get_dict

logging.basicConfig(filename="lab_1/report.log", filemode="a", level=logging.INFO)

def get_freq(path: str, new_path: str) -> dict:
    text=read_file(path)
    freq_dict = dict()
    try:
        for i in text:
            freq_dict[i]=text.count(i)/len(text)
        sorted_freq_dict= dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))
        get_dict(sorted_freq_dict,new_path)
        logging.info("freq_dict created")
    except Exception as e:
        logging.error(f"Error freq_dict {e}")
    return sorted_freq_dict


def replace_letters(text: str, freq_dict: dict, old_letter: str, new_letter: str, path_dict) -> str:
    try:
        text=text.replace(old_letter,new_letter)
        freq_dict[old_letter]=new_letter
        get_dict(freq_dict,path_dict)
        logging.info("replace_letters work")
    except Exception as e:
        logging.error(f"Error replace_letters {e}")
    return text

def decryption(text_path: str, result_path: str, dict_path: str) -> None:
    try:
        text=read_file(text_path)
        with open(dict_path, 'r', encoding='utf-8') as f:
            dict=json.load(f)
        for char, freq in dict.items():
            text=text.replace(char,freq)
        write_file(result_path, text)
    except Exception as e:
        logging.error(f"Error decryption {e}")

if __name__ == "__main__":
    with open(os.path.join("lab_1", "settings.json"), 'r', encoding='utf-8') as json_f:
        settings = json.load(json_f)
    text_path = os.path.join(settings["dir"], settings["folder"], settings["text"])
    freq_dict_path = os.path.join(settings["dir"], settings["folder"], settings["freq_dict"])
    """with open(text_path, 'r', encoding='utf-8') as text_file:
        text = text_file.read()
    freq_dict = get_freq(text_path, freq_dict_path)
    while True:
        print(text)
        old_letter = input("Enter the letter to replace\n")
        new_letter = input('Enter the new letter: ')
        text = replace_letters(text, freq_dict, old_letter, new_letter, freq_dict_path)"""
    decryption(text_path, os.path.join(settings["dir"], settings["folder"], settings["result"]),freq_dict_path)