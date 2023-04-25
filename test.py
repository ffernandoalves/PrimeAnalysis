from prime_analysis.analysis import plot_normalizate
from prime_analysis.calcs import calc_primes
from prime_analysis.supports import get_prime_numbers, save_restos_to_csv



if __name__ == "__main__":
    primefile = "primos\\txt\\primes50.txt"
    listprimes = get_prime_numbers(primefile, ignore_lines=2)
    data_size = 150
    nprime = listprimes[:data_size]
    resto = calc_primes.prime_residue(nprime)
    plot_normalizate(nprime, resto)
