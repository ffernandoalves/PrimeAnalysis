import math
from prime_analysis.ptypes import ListPrime, ListRest

def prime_residue(primos: ListPrime) -> ListRest:
    """
    Seja \'p\' primo, temos as seguinte equações:\n
        1. r = p, para todo p < 5\n
        2. r = p - 3*c, c>=0 para todo p >= 5.\n
    para todo r, c, p pertencentes a Z
    """
    resto = []
    c = 0
    for i in range(0, len(primos)):
        if primos[i] < 5:
            resto.append(primos[i])
            c=0
        else :
            resto.append(primos[i] - (3*c))
        c+=1
    return resto


def is_prime(num: int) -> bool:
    """
    Verifica se um número é primo
    """
    if num == 2:
        return True
    if num <= 1 or not num % 2:
        return False
    for div in range(3, int(math.sqrt(num)) + 1, 2):
        if not num % div:
            return False
    return True


def run_program(N: int):
    """:N: numero maximo para encontrar os primos"""
    lista = []
    for i in range(1, N+1):
        if is_prime(i):
            lista.append(i)
    prime_residue(lista)

