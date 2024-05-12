"""
Prime generation and factoring tools

Developed by Expedition Technology Inc 

"""

# Standard Library Imports
import itertools as it
from collections import
# External Library Imports


def primes_list( ):
    #This is based on the ERAT3, found on StackExchange
    #
    D = { 9: 3, 25: 5 }
    yield 2
    yield 3
    yield 5
    MASK= 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    MODULOS = frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )

    for q in it.compress(
            it.islice(it.count(7,2), 0, None, 1),
            it.cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in D or (x%30) not in MODULOS:
                x += 2*p
            D[x] = p
plst = {}            

def decompose(n):
    for p in primes_list():
        if p*p > n: break
        while n % p == 0:
            yield p
            n //=p
    if n > 1:
        yield n
        
def isprime(n):
    for pf in decompose(n):
        if pf<n:
            return False
    return True

def factor_int(a):
    return [b for b in decompose(a)]