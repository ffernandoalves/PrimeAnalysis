Version using [Python/C API](https://docs.python.org/3/c-api/index.html) aka CPython.

## INSTALL

Usando o ambiente virtual do Python, execute: 

1. no **Windows**:
```
cd calc_primes
python3.10 -m venv env
.\env\Scripts\activate
.\env\Scripts\python.exe -m pip install -r .\requirements.txt
.\env\Scripts\python.exe .\game.py
```

2. no **Linux**:
```
cd calc_primes
virtualenv -p /usr/bin/python3.10 venv 
source venv/bin/activate
venv/bin/python3 setup.py install
```

## TO USE

```venv/bin/python3 src/test.py```

## Comments

Os arquivos na pasta `primos` com os números primos foram tirados do site [t5k.com](https://t5k.org/lists/small/millions/).


The `confirmed_prime_numbers()` function tests `is_prime()` in [`isprime.cpp`](src/calc_primes.cpp) using the prime numbers from the `10000.txt` files, taken from [link](https://primes.utm.edu/lists/small/10000.txt).