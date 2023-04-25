Version using [Python/C API](https://docs.python.org/3/c-api/index.html) aka CPython.

## INSTALL

Usando o ambiente virtual do Python, execute: 

1. no **Windows**:
```
cd PrimeAnalysis
python3.10 -m venv env
.\env\Scripts\activate
.\env\Scripts\python.exe -m pip install build
.\env\Scripts\python.exe -m build
.\env\Scripts\python.exe -m pip install .\dist\prime_analysis-0.1.0-cp310-cp310-win_amd64.whl
.\env\Scripts\python.exe -m prime_analysis
```

1. 1 com `setuptools` no **Windows** (**old**):
```
cd PrimeAnalysis
python3.10 -m venv env
.\env\Scripts\activate
.\env\Scripts\python.exe setup.py install
.\env\Scripts\python.exe .\test.py
```

2. no **Linux**:
```
cd PrimeAnalysis
virtualenv -p /usr/bin/python3.10 venv 
source venv/bin/activate
venv/bin/python3 setup.py install
venv/bin/python3 test.py
```

_Obs 1: Os nomes após a versão (ex: `prime_analysis-0.1.0-`__`cp310-cp310-win_amd64`__`.whl`) vai depender da arquitetura do seu computador._

_Obs 2: Os arquivos gerados pelo comando `python -m build` vão estar na raiz do diretório __PrimeAnalysis__, caso tenha seguidos os mesmos passos._

## TO USE

```venv/bin/python3 src/test.py```

## Comments

Os arquivos na pasta `primos` com os números primos foram tirados do site [t5k.com](https://t5k.org/lists/small/millions/).


<!-- The `confirmed_prime_numbers()` function tests `is_prime()` in [`isprime.cpp`](src/calc_primes.cpp) using the prime numbers from the `10000.txt` files, taken from [link](https://primes.utm.edu/lists/small/10000.txt). -->