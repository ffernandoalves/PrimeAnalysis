import re
import math

import matplotlib.pyplot as plt
import pandas as pd

def get_prime_numbers(primes_file: str, size_ignore: int=2):
    PRIMES = []

    with open(primes_file, "r") as io_primesfile:
        lines = io_primesfile.readlines()[size_ignore:]
        for line in lines:
            prime_in_line = line.split("\n")
            for p in range(len(prime_in_line)):
                _primes = re.split(r"(\d+)", prime_in_line[p])
                for p_num in _primes:
                    if p_num.isdigit():
                        PRIMES.append(int(p_num))
    io_primesfile.close()

    # for i in PRIMES:
    #     get_primes(i) 
    return PRIMES


def graphPrimes(x, y, saveimg=False):
    u = []
    v = []
    increment = 50
    ant_int = 0
    part = int(len(x) / increment)
    path = "imagens/"
    # fignames = []
    for i in range(part):
        # fignames.append(path + f"x[{ant_int}:{increment}]&y[{ant_int}:{increment}].png")                   
        u.append(x[ant_int:increment])
        v.append(y[ant_int:increment])
        
        if (i == part - 1) and (x[increment:]):
            # fignames.append(path + f"x[{increment}:]&y[{increment}:].png")
            u.append(x[increment:])
            v.append(y[increment:])

        ant_int = increment
        increment += 50

    # if saveimg:
    #     for i in range(len(u)):
    #         fig, ax = plt.subplots()
    #         plt.plot(u[i], v[i])   #, marker='+'
    #         plt.xticks(u[i], fontsize=4, rotation=70)
    #         plt.yticks(v[i], fontsize=4)
    #         ax.set(xlabel='Primos', ylabel='Restos', title='Dispersão dos Primos em Relação aos Restos')
    #         plt.grid()
    #         plt.savefig(fignames[i], dpi=1000)
    #         print(f"Imagem {fignames[i]} salva.")
    #         plt.close()
    # else:
    #     fig, ax = plt.subplots()
    #     ax.plot(u[0], v[0])   #, marker='+'
    #     plt.xticks(u[0], fontsize=5, rotation=70)
    #     ax.set(xlabel='Primos', ylabel='Restos', title='Dispersão dos Primos em Relação aos Restos')
    #     ax.grid()
    #     plt.show()

def AlgoDivisao(primos, saveimg=False, filedata=None, sep="&"):
    resto = []
    c = 0
    for i in range(0, len(primos)):
        if primos[i] < 5:
            resto.append(primos[i])
            c=0
        else :
            resto.append(primos[i] - (3*c))
        c+=1
    
    if filedata is not None:
        dt = pd.DataFrame({"primo": primos, "resto": resto})
        dt.to_csv(filedata, sep=sep, index=False)
    # graphPrimes(primos, resto, saveimg=saveimg)

def is_prime(num):
    if num == 2:
        return True
    if num <= 1 or not num % 2:
        return False
    for div in range(3, int(math.sqrt(num)) + 1, 2):
        if not num % div:
            return False
    return True

def run_program(N, saveimg=False, filedata=None, sep="&"):
    lista = []
    for i in range(1, N+1):
        if is_prime(i):
            lista.append(i)
    AlgoDivisao(lista, saveimg=saveimg, filedata=filedata, sep=sep)


if __name__ == '__main__':
    # N = 100000
    # filedata = "C:\\Users\\UFMA\\Documents\\docs\\Nova pasta (2)\\primes&restos.csv"
    # run_program(N, filedata=filedata)

    primefile = "C:\\Users\\UFMA\\Documents\\docs\\primes50\primes50.txt"
    listprimes = get_prime_numbers(primefile, size_ignore=2)
    print(listprimes[:50])

