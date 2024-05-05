import logging

logging.basicConfig(filename="report.log", filemode="a", level=logging.INFO)


def write_file(path: str, data: bytes) -> None:
    """
    Writes data to a file

    Args:
        path (str): the path to the file where the data will be written
        data (bytes): the data to be written to the file
    """
    try:
        with open(path, "wb" ) as f:
            f.write(data)
    except Exception as e:
        logging.error(f"Error in write file {e}")


def read_file(path: str) -> bytes:
    """
    Reads data from a file

    Args:
        path (str): the path to the file to be read
    """
    try:
        with open(path, "rb") as f:
            data = f.read()
        return data
    except Exception as e:
        logging.error(f"Error in read file {e}")