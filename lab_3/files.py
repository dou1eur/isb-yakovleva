import logging

logging.basicConfig(filename="report.log", filemode="a", level=logging.INFO)


def write_file(path: str, data: bytes) -> None:
    try:
        with open(path, "wb") as f:
            f.write(data)
    except Exception as e:
        logging.error(f"Error in write file {e}")

def read_file(path: str) -> bytes:
    try:
        with open(path, "rb") as f:
            data = f.read()
        return data
    except Exception as e:
        logging.error(f"Error in read file {e}")