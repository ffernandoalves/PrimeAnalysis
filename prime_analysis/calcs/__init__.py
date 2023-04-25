try:
    from . import calc_primes
except:
    from . import calc_primes_py as calc_primes


__all__ = ["calc_primes"]


