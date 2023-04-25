# source: https://setuptools.pypa.io/en/latest/userguide/quickstart.html

import re
import pathlib
from setuptools import setup, Extension, find_packages

# project dirs 
package_source = pathlib.Path("prime_analysis")

VERSION_FILE = package_source/"__init__.py"
getversion = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", open(VERSION_FILE, "rt").read(), re.M)
if getversion:
    new_version = getversion.group(1)
else:
    raise RuntimeError(f"Unable to find version string in {VERSION_FILE}.")

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


mod_calc_primes = Extension("prime_analysis.calcs.calc_primes",
                    sources=[str(package_source/"calcs/calc_primes.cpp"),], 
                    language='c++')

# primes_file = (str(pathlib.Path("primos/txt")), [str(pathlib.Path("primos/txt/primes50.txt")),])

# keywords: https://setuptools.pypa.io/en/latest/references/keywords.html
setup(name = "prime_analysis",
    version = new_version,
    author = "Fernando Ribeiro Alves",
    keywords = "primes, data analysis",
    python_requires = ">=3.10",
    install_requires = requirements,
    packages = find_packages(),
    include_package_data=True,
    exclude_package_data={"prime_analysis.calcs": ["*.cpp"]},
    # package_data = {"": [str(pathlib.Path("primos/txt/primes50.txt"))]}, # dict([primes_file]), # https://setuptools.pypa.io/en/latest/userguide/datafiles.html
    ext_modules = [mod_calc_primes],
    
)