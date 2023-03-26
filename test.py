import re
import komm
import random

# parametry początkowe dla kodu RS
n = 10
k = 4
t = 3
r = 6
mess = [55, 230, 2, 103]

# Encoder RS

# obliczona ręcznie postać wielomianu generującego, która
# zostanie przepuszczna prze odpowiednią fukcję która da nam wspłczyniki
row = "x6+x5(a1+a2+a3+a4+a5+a6)+x4(a3+a4+a7+a10+a11)+x3(a6+a7+a9+a10+a11+a12+a14+a15)+x2(a10+a11+a14+a17+a18)+x(" \
      "a15+a16+a17+a18+a19+a20)+a21 "

field = komm.FiniteBifield(8, modulus=0b100011101)  # zdefiniowanie GF(2^8) i wielomianu pierwotnego x^8+x^4+x^3+x^2+1
alpha = field.primitive_element
prim_elements = {256: 0b0}  # stworzenie słownika przechowującego warotści każdej alfy, wartość 256 to wartość
# specjalna która jest czystym zerem


# funkcja dostaje wartość przynależną dopewnej alfy i wyszukuje w słowniku jej stopnia
def find_alfa(value):
    for i in range(0, len(prim_elements)):
        if prim_elements[i] == value:
            return i


# pętla odpowiedzialna za tworzenie i dopisaywanie każdego elemtu do słowniaka
for i in range(0, 256):
    tmp = str(alpha ** i)
    tmp = tmp.replace('0b', '')
    prim_elements[i] = int(tmp, base=2)

# definiowanie tabliczki dodawania
add_tab = [[find_alfa(prim_elements[i] ^ prim_elements[j]) for j in range(257)] for i in range(257)]

# definiowanie tabliczki mnożenia
mul_tab = [[find_alfa(prim_elements[i] & prim_elements[j]) for j in range(257)] for i in range(257)]

# definiowanie tabliczki dzielenia
div_tab = [[find_alfa((255 ^ prim_elements[mul_tab[i][j]]) % 256) for j in range(257)] for i in range(257)]


# WIELOMIAN GENERATOROWY
def gen_fun_256(strum):
    tab = re.split(r'[+()*]', strum)

    gen_alfa_tab = [1]

    tab.remove("x6")
    while tab.__contains__(''):
        tab.remove('')

    i = 0
    while i < len(tab) - 2:
        try:
            if 'a' in tab[i] and 'a' in tab[i + 1]:
                if tab[i][0] == 'a' and tab[i + 1][0] == 'a':
                    num1 = tab[i].split("a")
                    num2 = tab[i + 1].split("a")
                    tab[i + 1] = "a" + str(add_tab[int(num1[1])][int(num2[1])])
                    tab.remove(tab[i])
                    i -= 1
            i += 1
        except IndexError:
            print("error")

    for k in range(0, len(tab)):
        if 'a' in tab[k]:
            gen_alfa_tab.append(int(tab[k].split('a')[1]))

    return gen_alfa_tab


gen_poly = gen_fun_256(row)


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
        leading_term = remainder[0]
        divisor = poly2[0]

        # Oblicz współczynnik do podzielenia
        quotient_coeff = div_tab[int(divisor)][int(leading_term)]

        # Pomnóż mianownik przez współczynnik -> term & quotient_coeff
        dividend = [mul_tab[term][quotient_coeff] for term in poly2]

        # Odejmij wynik mnożenia od reszty -> remainder[i] ^ dividend[i]
        remainder = [add_tab[remainder[i]][dividend[i]] for i in range(0, len(dividend) - 1)]

        # Dodaj wynik do ilorazu
        quotient[len(remainder) - 3] = quotient_coeff

    return remainder, quotient


couter_power = 0
help_mess = mess.copy()
while couter_power < 6:
    help_mess.append(0)
    couter_power += 1

encode, rest = div(help_mess, gen_poly)

full_mess = mess + encode

print(full_mess)

# prowizorycznyu kanał szumu


for i in range(0, t):
    error_to_change = random.randint(0, 255)
    error_index = random.randint(0, len(full_mess) - 1)
    full_mess[error_index] = error_to_change

print(full_mess)
print(gen_poly)

# Dekoder RS
