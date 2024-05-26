import hashlib
import logging
import multiprocessing as mp

from files import save_number

logging.basicConfig(filename="lab_4//report.log", filemode="a")


def checking_numbers(hash: str, last_numbers: str, middle_number: int, iins: list) -> str:
    try:
        for iin in iins:
            iin_hash = hashlib.sha384(f"{iin}{middle_number:0>6}{last_numbers:0>4}".encode()).hexdigest()
            if iin_hash == hash:
                logging.info('Number found')
                return f"{iin}{middle_number:0>6}{last_numbers:0>4}"
    except Exception as e:
        logging.error(f'Error when comparing hashes {e}')


def number_search(hash: str, last_numbers: str, save_path: str, iins: list) -> None:
    try:
        cores = mp.cpu_count()
        with mp.Pool(processes=cores) as p:
            for result in p.starmap(checking_numbers, [(hash, last_numbers, i, iins) for i in range(999999)]):
                if result:
                    save_number(result, save_path)
                    return result
        logging.info('Number not found')
    except Exception as e:
        logging.error(f'Error when searching number {e}')


def luna_algorithm(card_number: str) -> bool:
    try:
        reverse_card_number = card_number[::-1]
        sum = 0
        for i in range(len(reverse_card_number)):
            cur_pos = int(reverse_card_number[i])
            if i % 2 == 0:
                even_pos = cur_pos * 2
                if even_pos >= 10:
                    even_pos = even_pos - 9
                sum += even_pos
            else:
                sum += cur_pos
        control_digit = (10 - (sum % 10)) % 10 
        if control_digit == int(card_number[-1]): 
            logging.info('Luna algorithm passed')
            return True
        logging.info('Luna algorithm not passed')
    except Exception as e:
        logging.info(f'Error in luna algorithm {e}')