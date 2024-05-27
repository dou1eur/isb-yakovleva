import hashlib
import logging
import multiprocessing as mp
import time

from matplotlib import pyplot as plt

from files import save_number

logging.basicConfig(filename="lab_4//report.log", filemode="a")


def checking_numbers(hash: str, last_numbers: str, middle_number: int, iin: str) -> str:
    """
    The function iterates through the numbers and compares them with the desired hash

    Args:
        hash (str): hash for comparison
        last_numbers (str): last 4 digits of card number
        middle_number (int): central digit
        iin (str): the individual identification number

    Returns:
        str: card number
    """
    try:
        iin_hash = hashlib.sha384(
            f"{iin}{middle_number:0>6}{last_numbers:0>4}".encode()).hexdigest()
        if iin_hash == hash:
            logging.info("Number found")
            return f"{iin}{middle_number:0>6}{last_numbers:0>4}"
    except Exception as e:
        logging.error(f"Error when comparing hashes {e}")


def number_search(hash: str, last_numbers: str, save_path: str, iins: list) -> None:
    """
    The function loops through the numbers and compares them with the given hash

    Args:
        hash (str): hash for comparison
        last_numbers (str): last 4 digits of card number
        save_path (str): path where you need to save the card number
        iins (list): list of individual identification numbers
    """
    try:
        cores = mp.cpu_count()
        with mp.Pool(processes=cores) as p:
            for iin in iins:
                results = p.starmap(checking_numbers, [(hash, last_numbers, i, iin) for i in range(999999)])
                for result in results:
                    if result:
                        save_number(result, save_path)
                        return result
        logging.info("Number not found")
    except Exception as e:
        logging.error(f"Error when searching number {e}")


def luna_algorithm(card_number: str) -> bool:
    """
    The function checks the correctness of the card number

    Args:
        card_number (str): card number

    Returns:
        bool: True if the card number is valid, False otherwise
    """
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
            logging.info("Luna algorithm passed")
            return True
        logging.info("Luna algorithm not passed")
    except Exception as e:
        logging.info(f"Error in luna algorithm {e}")


def collision_search(hash: str, last_numbers: str, iins: list) -> None:
    """
    The function collects the hash determination time when dividing the number of processes

    Args:
        hash (str): hash for comparison
        last_numbers (str): last 4 digits of card number
        iin (list): lsit of individual identification number
    """
    try:
        results = []
        cores = mp.cpu_count()/2
        for num_core in range(1, int(1.5 * cores)):
            start_time = time.time()
            with mp.Pool(processes=num_core) as p:
                p.starmap(
                    checking_numbers,
                    [(hash, last_numbers, i, iin) for iin in iins for i in range(0, 999999)],)
                total_time = time.time() - start_time
                results.append(total_time)
        logging.info("Statistics collected")
        plt.title("Collision search")
        plt.xlabel("num processes")
        plt.ylabel("search time")
        plt.plot(
            range(1, int(1.5 * cores)),
            results,
            color="navy",
            linestyle="--",
            marker="x",
            linewidth=1,
            markersize=4,)
        plt.show()
    except Exception as e:
        logging.error(f"Error during collision search {e}")
