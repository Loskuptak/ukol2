# -*- coding: utf-8 -*-
def soucet(a, b):
    if any(isinstance(x, bool) for x in (a, b)) or \
       not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Nenene oba inputy by měli být číslo (ale ne bool).")
    return a + b

    
if __name__ == '__main__':
    a = float(input("první číslo: "))
    b = float(input("druhé číslo: "))
    vysledek = soucet(a, b)
    print("Výsledek je:", vysledek)
