import argparse
import json
import logging
import os

from funсtions import luna_algorithm, number_search

logging.basicConfig(filename="lab_4//report.log", filemode="a", level=logging.INFO)


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Options")
        parser.add_argument(
            "-option",
            "--opt",
            type=int,
            
            choices=range(3),
            help="Choose an option: 0 - Selection of card number by hash, 1 - Applying the Luhn algorithm")
        parser.add_argument("-json","--jpath",type=str, default=os.path.join("lab_4/settings.json"),help="Path to json_file")
        parser.add_argument("-hash", "--hash_value", type=str, help="hash cards")
        parser.add_argument("-sp", "--save_path", type=str, help="path to save card number")
        parser.add_argument("-l", "--list_iin", type=str,  help="list containing iin")
        parser.add_argument("-ln", "--last_numbers", type=str, help="card last numbers") 
        parser.add_argument("-card", "--card_number", type=str, help="Credit card number to apply Luhn algorithm")
        args = parser.parse_args()
        with open(args.jpath, mode="r", encoding="utf-8") as f:
                settings = json.load(f)
        parser.set_defaults(hash_value=settings["hash"])
        parser.set_defaults(save_path=os.path.join(settings["folder"],settings["file"]))
        parser.set_defaults(list_iin=settings["iins"])
        parser.set_defaults(last_numbers=settings["last_numbers"])
        match args.opt:
            case 0: 
                number_search(args.hash_value, args.last_numbers, args.save_path, args.list_iin)
            case 1:
                if (luna_algorithm(args.card_number)):
                    print("Luna algorithm is valid")
                else: 
                    print("Luna algorithm is invalid")
            case _:
                logging.error("Incorrect option")
    except Exception as e:
         logging.error(f'Problems in main {e}')