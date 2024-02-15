import os
import logging
from chipher import write_file,read_file

logging.basicConfig(filename="lab_1/report.log", filemode="a", level=logging.INFO)

def get_freq(path: str, new_path: str) -> None:
    text=read_file(path)
    freq_dict={}
    for i in freq_dict:
        freq_dict[i]=text.count(i)/len(text)
    sorted_freq_dict=dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))
    with open(new_path, 'w') as f:
        for char, freq in sorted_freq_dict.items():
            f.write(f"{char} - {freq}\n")

def replace_letters(text: str, freq_dict: dict, old_letter: str, new_letter: str, path_dict) -> str:
    text=text.replace(old_letter,new_letter)
    freq_dict[old_letter]=new_letter
    with open(path_dict,'w') as f:
        for char, freq in freq_dict.items():
            f.write(f"{char} - {freq}")
    return text


if __name__ == "__main__":
    