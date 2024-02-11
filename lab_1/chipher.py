import os
import logging
import json

logging.basicConfig(filename="report.log",filemode="a",level=logging.INFO)

ALPHABET="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
KEYWORD="ГРАНАТ"

def get_key(keyword: str, alphabet: str) -> dict:
    """The function receives a word, each letter
    of which is replaced by the corresponding 
    number in the table"""
    key={}
    for i, char in enumerate(keyword):
        key[i]=alphabet.index(char)
    logging.info("func get_key work")
    return key


def vigenere_chipher(alphabet: str, key: dict, text: str, mode: bool) -> str:
    """Encryption and decryption function using Vigenere method:
    mode = True  - encryption
    mode = False - decryption
    """
    chipher=str()
    for i, char in enumerate(text):
        if char in alphabet:
            char_idx=alphabet.index(char)
            keyword_idx=i%len(key)
            shift=key[keyword_idx]
            if mode == True:
                chipher_idx=(char_idx+shift)%len(alphabet)
            elif mode == False:
                chipher_idx=(char_idx-shift)%len(alphabet)
            chipher_char=alphabet[chipher_idx]
            chipher+=chipher_char
        else: chipher +=char
    logging.info("func vigenere_chipher work, encryption done")
    return chipher


if __name__=="__main__":
    k=get_key(KEYWORD,ALPHABET)
    print(k)
    t="ЭТО ТЕКСТ ДЛЯ ПРОВЕРКИ"
    enc=vigenere_chipher(ALPHABET,k,t,True)
    print(enc)
    dec=vigenere_chipher(ALPHABET,k,enc,False)
    print(dec)