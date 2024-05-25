import json
import logging

logging.basicConfig(filename="lab_4//report.log", filemode="a", level=logging.INFO)


def save_number(result: str, save_path: str) -> None:
    try:
        with open(save_path, "w", encoding="UTF-8") as f:
            json.dump({"card_number":  result}, f)
    except Exception as e:
        logging.error(f"Error writing to file {e}")




