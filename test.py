import re
import komm
import random

# parametry początkowe dla kodu RS
n = 10
k = 4
t = 3
r = 6
mess = [0,0,0,1] # zapis alf -> alfa 255 to wektor 0 a alfa 0 to wektor 1

# Encoder RS

# obliczona ręcznie postać wielomianu generującego, która
# zostanie przepuszczna prze odpowiednią fukcję która da nam wspłczyniki
row = "x6+x5(a1+a2+a3+a4+a5+a6)+x4(a3+a4+a7+a10+a11)+x3(a6+a7+a9+a10+a11+a12+a14+a15)+x2(a10+a11+a14+a17+a18)+x(" \
      "a15+a16+a17+a18+a19+a20)+a21 "

field = komm.FiniteBifield(8, modulus=0b100011101)  # zdefiniowanie GF(2^8) i wielomianu pierwotnego x^8+x^4+x^3+x^2+1
alpha = field.primitive_element
prim_elements = {255: 0b0}  # stworzenie słownika przechowującego warotści każdej alfy, wartość 256 to wartość
# specjalna która jest czystym zerem


# funkcja dostaje wartość przynależną dopewnej alfy i wyszukuje w słowniku jej stopnia
def find_alfa(value):
    for i in range(0, len(prim_elements)):
        if prim_elements[i] == value:
            return i


# pętla odpowiedzialna za tworzenie i dopisaywanie każdego elemtu do słowniaka
for i in range(0, 255):
    tmp = str(alpha ** i)
    tmp = tmp.replace('0b', '')
    prim_elements[i] = int(tmp, base=2)

for i in range(len(prim_elements)):
    print(str(i) + " " + str(prim_elements[i]))


# definiowanie tabliczki dodawania - zapis alf
add_tab = [[find_alfa(prim_elements[i] ^ prim_elements[j]) for j in range(256)] for i in range(256)]

# definiowanie tabliczki mnożenia - zapis alf
mul_tab = [[find_alfa( (i + j) % 255 ) for j in range(256)] for i in range(256)]


# WIELOMIAN GENERATOROWY - zapis alf
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
# for i in range(len(mul_tab)):
#     print(mul_tab[i])

print(mul_tab[0][0])

def div(poly1, poly2): #- zapis alf/wektorowy, ciężko określić
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

    remainder = poly1.copy()

    index = 0
    temp = []
    wynik = []
    while len(remainder) >= len(poly2):
        for i in range(len(poly2)):
            if remainder[i] != 0: #jezeli sprawdzany znak jest rowny pierwszemu znakowy
                temp = mul_poly(remainder,poly2, i)
                wynik = xor_poly(remainder, poly2, temp, i)
                remainder = delete_if_zero_in_result(wynik, remainder, i)
            else:
                continue



    return remainder
def mul_poly(remainder, gen, i):
    temp = []
    for j in range(len(gen)):
        temp.append(mul_tab[remainder[i] - 1 ][gen[j]])
    return temp
def xor_poly(remainder, gen, temp, i):
    wynik = []
    for j in range(len(gen)):
        #wynik.append(add_tab[prim_elements.get(remainder[i]-1)][prim_elements.get(temp[j])])
        wynik.append(add_tab[remainder[i]-1][temp[j]])
    return wynik
def delete_if_zero_in_result(wynik, poly1,i):

    while wynik[0] == 255:
        wynik.pop(0)

    wynik.append(poly1[(len(poly1)-1)-i])

    return wynik


couter_power = 0
help_mess = mess.copy()
while couter_power < 6:
    help_mess.append(0)
    couter_power += 1

# encode = div(help_mess, gen_poly)
#
# full_mess = mess + encode
# print(encode)

#print(full_mess)

# prowizorycznyu kanał szumu


# for i in range(0, t):
#     error_to_change = random.randint(0, 255)
#     error_index = random.randint(0, len(full_mess) - 1)
#     full_mess[error_index] = error_to_change

# print(full_mess)
# print(gen_poly)

# Dekoder RS

def cal_syndroms(encrypt_mess):

    sydroms = []

    for i in range(1,7):
        power = []
        for a in range(0,len(encrypt_mess)-1):
            power.append(mul_tab[encrypt_mess[a]][((i * ((len(encrypt_mess) - a)-1)) % 255)]) # jezeli a to indeks  to len(A)-1 to najwyzsza potega
            # czyli zeby policzyc kolejne potegi od lewej do praewj to len(a) - a to potęga na odpowiednim miejscu
            # przykład dla x^9  -> ((len(encrypt_mess) - a)-1)
            # 0 - > 9
            # 1 - > 8

        power.append(encrypt_mess[-1])
        temp_sum = power[0]

        for i in range(1,len(power)):
            temp_sum = add_tab[temp_sum][power[i]]

        sydroms.append(temp_sum)

    return sydroms

# sydnromes_group = cal_syndroms(full_mess)
# #print(sydnromes_group)
#
# #
# #
#
#
# for i in range(len(div_tab)):
#     print(div_tab[i])
#
# print("tablica mnozenia")
#
# for i in range(len(mul_tab)):
#     print(mul_tab[i])
#
#
# print("dzielenieprzez wielomian generujacy")
# print(div(full_mess , gen_poly))
#
# print("Wiadmosc")
# print(mess)
# print("Wiadomosc po przekodowaniu")
# print(full_mess)
# print("Generator")
# print(gen_poly)
# print("Zrobiony przez bilbioteke")
# #print(int_array)
# print("dzielenie wiadomosci ktora kodujemy")
# print(div(full_mess,gen_poly))
# sekwenncja = [255,255,255,0,255,255,255,255,255,255]
# print("Sekwencja przez generujacy")
# print(div(sekwenncja,gen_poly))