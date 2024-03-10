import json
import logging
import os
import math


logging.basicConfig(filename="lab_2/report.log", filemode="a", level=logging.INFO)


def freq_bit_test(sequence: str) -> float:
    bits={'0':-1,'1':1}
    try:
        sum_value=sum(bits.get(bit,0) for bit in sequence)
        p_value=math.erfc(abs(sum_value)/(math.sqrt(2*len(sequence))))
    except Exception as e:
        logging.error(f'Problems in the frequency bit test: {e}')
    logging.info("Frequency bit test passed successfully")
    return p_value




def save_results(results, path: str) -> None:
    try:
        with open(path, "a+", encoding="utf-8") as f:
            f.write(str(results))
        logging.info('Results uploaded successfully')
    except Exception as e:
        logging.error(f'Error in saving results: {e}')


if __name__ == "__main__":
    with open(os.path.join("lab_2", "settings.json"), "r", encoding="utf-8") as json_f:
        settings = json.load(json_f)
    save_results(freq_bit_test(settings['genc']),os.path.join(settings["folder"],settings["file"]))
    save_results(freq_bit_test(settings['genj']),os.path.join(settings["folder"],settings["file"]))

