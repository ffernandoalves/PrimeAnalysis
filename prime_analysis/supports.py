import re
import pathlib
import pandas as pd

from prime_analysis import ptypes


def get_prime_numbers(primes_file: pathlib.Path, ignore_lines: int=2) -> ptypes.ListPrime:
    """
    :primes_file: path to txt file\n
    :ignore_lines: number of lines to skip of the file
    """
    prime_list = []

    with open(primes_file, "r") as io_primesfile:
        lines = io_primesfile.readlines()[ignore_lines:]
        for line in lines:
            prime_in_line = line.split("\n")
            for p in range(len(prime_in_line)):
                _primes = re.split(r"(\d+)", prime_in_line[p])
                for p_num in _primes:
                    if p_num.isdigit():
                        prime_list.append(int(p_num))
    io_primesfile.close()

    return prime_list

def load_primes_txt(num: int):
    pass


def save_restos_to_csv(filedata: pathlib.Path, primos: list, resto: list, sep: str = "&"):
    if filedata.suffix == ".csv":
        dt = pd.DataFrame({"primo": primos, "resto": resto})
        dt.to_csv(filedata, sep=sep, index=False)
    else:
        raise Exception(f"Não foi possível encontrar o arquivo \'{filedata}\'.")
