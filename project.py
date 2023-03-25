from pyfinite import ffield
import numpy as np
import re


row = "x6+x5(a1+a2+a3+a4+a5+a6)+x4*a3+x3(a6+a7+a8+a9)+x2*a10+x(a15+a16)+a21"
messeg = [30,20,31,60] #30x^3 + 20x^2 + 31x + 60 -> *x^6 -> 30x^9 + 20x^8 + 31x^7 + 60x^6
#m(x)* x^(n-k) mod g(x)

def create_div_table():
    # Inicjalizacja pola GF(256)
    F = ffield.FField(8)

    # Utworzenie tablicy mnożenia w polu GF(256)
    div_table = []
    for i in range(256):
        row = []
        for j in range(256):
            row.append(255 - (F.Multiply(i, j)))
        div_table.append(row)

    return div_table


# Znalezienie elementów pierwotnych w polu GF(256)
def find_primitive_elements():
    p = 257  # liczba pierwsza taka, że p > 2 i p dzieli 2^8-1
    primitive_elements = []
    for a in range(1, 256):
        is_primitive = True
        ap = pow(a, p, 256)  # obliczenie a^p mod 256
        if ap == 1:
            is_primitive = False
        for i in range(1, 255):
            ap = pow(ap, 2, 256)  # obliczenie a^(2^i) mod 256
            if ap == 1:
                is_primitive = False
                break
        if is_primitive:
            primitive_elements.append(a)
    return primitive_elements


def create_multiplication_table():
    # Inicjalizacja pola GF(256)
    F = ffield.FField(8)

    # Utworzenie tablicy mnożenia w polu GF(256)
    mul_table = []
    for i in range(256):
        row = []
        for j in range(256):
            row.append(F.Multiply(i, j))
        mul_table.append(row)

    return mul_table

def create_addition_table():
    # Inicjalizacja pola GF(256)
    F = ffield.FField(8)

    # Utworzenie tablicy dodawania w polu GF(256)
    add_table = []
    for i in range(256):
        row = []
        for j in range(256):
            row.append(F.Add(i, j))
        add_table.append(row)

    return add_table

#stworzenie tablicy elementów pierwotnych oraz tabel dodania i mnożenia
primitive_elements = find_primitive_elements()
add_table = create_addition_table()
mul_table = create_multiplication_table()
div_table = create_div_table()





#WIELOMIAN GENERATOROWY
def gen_fun_256(strum):
    tab = re.split(r'[+()*]',strum)

    gen_alfa_tab = []
    gen_alfa_tab.append(1)

    tab.remove("x6")
    tab.remove('')
    tab.remove('')
    tab.remove('')

    i = 0
    while i < len(tab)-2:
        try:
            if('a' in tab[i] and 'a' in tab[i+1]):
                if(tab[i][0] == 'a' and tab[i+1][0] == 'a'):
                    num1 = tab[i].split("a")
                    num2 = tab[i+1].split("a")
                    tab[i+1] = "a"+ str(add_table[int(num1[1])][int(num2[1])])
                    tab.remove(tab[i])
                    i -= 1
            i += 1
        except IndexError:
            print("error")

    for k in range(0,len(tab)):
        if('a' in tab[k]):
            gen_alfa_tab.append(int(tab[k].split('a')[1]))


    return gen_alfa_tab



gen_pol = gen_fun_256(row)
print(gen_pol)

p = np.array(messeg + [0,0,0,0,0,0])
q = np.array(gen_pol)

quotient, remainder = np.polydiv(p, q)
print("Iloraz:", quotient)
print("Reszta:", remainder)

print(mul_table[10][10])
print(div_table[10][10])


def div(poly1, poly2):
    """
    Funkcja wykonująca dzielenie wielomianów w ciele gf(256) na podstawie tabeli dzielenia.
    Argumenty:
    poly1 (list): pierwszy wielomian (dzielnik)
    poly2 (list): drugi wielomian (dzielnik)
    Zwraca:
    tuple: reszta i iloraz wielomianów
    """
    if len(poly2) > len(poly1):
        return [], poly1

    quotient = [0] * (len(poly1) - len(poly2) + 1)
    remainder = poly1.copy()

    while len(remainder) >= len(poly2):
        # Wybierz najwyższą potęgę wielomianu mianownika
        leading_term = remainder[-1]
        divisor = poly2[-1]

        # Oblicz współczynnik do podzielenia
        quotient_coeff = div_table[mul_table[int(divisor)][int(leading_term)]]

        # Pomnóż mianownik przez współczynnik
        factor = [0] * (len(remainder) - len(poly2)) + [quotient_coeff]
        dividend = [term * quotient_coeff for term in poly2]

        # Odejmij wynik mnożenia od reszty
        remainder = [remainder[i] ^ dividend[i] for i in range(len(remainder))]

        # Dodaj wynik do ilorazu
        quotient[len(remainder)] = quotient_coeff

    return remainder, quotient


print(div( [30,20,31,60,0,0,0,0,0,0],gen_pol))



