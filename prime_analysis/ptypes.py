"""
Types of PrimeAnalysis
"""

import typing


__all__ = ["PrimeType", "ListPrime", "Rest", "ListRest"]

PrimeType = typing.NewType("PrimeType", int)
ListPrime = typing.NewType("ListPrime", list[PrimeType])
Rest = typing.NewType("Rest", int)
ListRest = typing.NewType("ListRest", Rest)