import argparse
import json
import logging
import os
from funсtions import number_search

logging.basicConfig(filename="lab_4//report.log", filemode="a", level=logging.INFO)


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Options")
        parser.add_argument(
            "-option",
            "--opt",
            type=int,
            choices=range(3),
            help="Choose an option: 0 - Selection of card number by hash")
        parser.add_argument("-json","--jpath",type=str, default=os.path.join("lab_4/settings.json"),help="Path to json_file")
        args = parser.parse_args()
        with open(args.jpath, mode="r", encoding="utf-8") as f:
            settings = json.load(f)
        match args.opt:
            case 0: 
                parser.add_argument("-hash", "--hash_value", type=str, default=settings["hash"], help="hash cards")
                parser.add_argument("-sp", "--save_path", type=str, default=os.path.join(settings["folder"],settings["file"]), help="path to save card number")
                parser.add_argument("-l", "--list_iin", type=str, default=settings["iins"], help="list containing iin")
                parser.add_argument("-ln", "--last_numbers", type=str, default=settings["last_numbers"], help="card last numbers") 
                args = parser.parse_args()
                number_search(args.hash_value, args.last_numbers, args.save_path, args.list_iin)
            case _:
                logging.error("Incorrect option")
    except Exception as e:
         logging.error(f'Problems in main {e}')