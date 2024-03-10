import json
import logging
import os
import math

from mpmath import gammainc

logging.basicConfig(filename="lab_2/report.log", filemode="a", level=logging.INFO)

PI={'v1':0.2148,'v2':0.3672,'v3':0.2305,'v4':0.1875}


def freq_bit_test(sequence: str) -> float:
    bits={'0':-1,'1':1}
    try:
        sum_value=sum(bits.get(bit,0) for bit in sequence)
        p_value=math.erfc(abs(sum_value)/(math.sqrt(2*len(sequence))))
    except Exception as e:
        logging.error(f'Problems in the frequency bit test: {e}')
    logging.info("Frequency bit test passed successfully")
    return p_value


def search_identical_bits(sequence: str) -> float:
    try:
        share=sum(int(bit) for bit in sequence)/len(sequence)
        if abs(share-0.5)<(2/math.sqrt(len(sequence))):
            v=0
            for bit in range(len(sequence)-1):
                if sequence[bit] != sequence[bit+1]:
                    v+=1
                p_value=math.erfc((abs(v-2*len(sequence)*share*(1-share)))/(2*math.sqrt(2*len(sequence))*(1-share)))
        else: p_value=0
    except Exception as e:
        logging.error('Problem is in the test for identical bits')
    return p_value


def longest_sequence_test(sequence: str) -> float:
    try:
        blokcs=[sequence[i:i+8] for i in range(0,len(sequence), 8)]
        statistic={'v1':0,'v2':0,'v3':0,'v4':0}
        try:
            for block in blokcs:
                max_counter=0
                counter=0
                for bit in block:
                    if bit=='1':
                        counter+=1
                    else:
                        max_counter=max(max_counter,counter)
                match max_counter:
                    case 0,1:
                        statistic['v1']+=1
                    case 2:
                        statistic['v2']+=1
                    case 3:
                        statistic['v3']+=1
                    case _:
                        statistic['v4']+=1
            logging.info("Statistics collected")
        except Exception as e:
            logging.error("Statistics not collected")
        chi_squared_distribution=0
        for v in statistic:
            chi_squared_distribution += (pow(statistic[v]-16*PI[v],2))/(16*PI[v])
        p_value=gammainc(3/2,chi_squared_distribution/2)
    except Exception as e:
        logging.error(f"Problem calculating chi-square and gamma function: {e}")
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
    save_results(search_identical_bits(settings['genc']),os.path.join(settings["folder"],settings["file"]))
    save_results(search_identical_bits(settings['genj']),os.path.join(settings["folder"],settings["file"]))
    save_results(longest_sequence_test(settings['genc']),os.path.join(settings["folder"],settings["file"]))
    save_results(longest_sequence_test(settings['genj']),os.path.join(settings["folder"],settings["file"]))

