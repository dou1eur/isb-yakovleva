import hashlib
import logging
import multiprocessing as mp

from files import save_number

logging.basicConfig(filename="lab_4//report.log", filemode="a")


def checking_numbers(hash: str, last_numbers: str, middle_number: int, iin: str) -> str:
    try:

        iin_hash = hashlib.sha384(f"{iin}{middle_number:0>6}{last_numbers:0>4}".encode()).hexdigest()
        if iin_hash == hash:
            logging.info('Number found')
            return f"{iin}{middle_number:0>6}{last_numbers:0>4}"
    except Exception as e:
        logging.error(f'Error when comparing hashes {e}')


def number_search(hash: str, last_numbers: str, save_path: str, iins: list) -> None:
    try:
        cores = mp.cpu_count()
        logging.info('In number_search')
        with mp.Pool(processes=cores) as p:
            for result in p.starmap(checking_numbers, [(hash, last_numbers, i, iins) for i in range(999999)]):
                if result:
                    save_number(result, save_path)
                    return result
    except Exception as e:
        logging.error(f'Error when searching number {e}')