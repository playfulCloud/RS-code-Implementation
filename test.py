import re
import komm
import random

# parametry początkowe dla kodu RS
n = 10
k = 4
t = 3
r = 6
mess = [1,2,3,4] # zapis alf -> alfa 255 to wektor 0 a alfa 0 to wektor 1

big_vector = []

for i in range(0,244):
    big_vector.append(255)

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
mul_tab = [[( (i + j) % 255 ) for j in range(256)] for i in range(256)]


# WIELOMIAN GENERATOROWY - zapis alf
def gen_fun_256(strum):
    tab = re.split(r'[+()*]', strum)

    gen_alfa_tab = [0]

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

def div(poly1, poly2, isSyndrome):

    tmp_zero = []

    for k in range(0,10):
        tmp_zero.append(255)

    if len(poly2) > len(poly1):
        return [], poly1

    remainder = poly1.copy()
    i = 0
    while len(remainder) >= len(poly2) and i < len(poly1):
        if remainder[i] != 255: #jezeli sprawdzany znak jest rowny pierwszemu znakowy
            temp = mul_poly(remainder, poly2, i)
            wynik = xor_poly(remainder, poly2, temp, i)
            remainder, i = delete_if_zero_in_result(wynik, remainder, i, poly2)
        else:
            i += 1

    if isSyndrome:
        tmp_len = len(tmp_zero) - 1
        if len(remainder) > 0:
            rem_len = len(remainder) - 1
            while rem_len >= 0:
                tmp_zero[tmp_len] = remainder[rem_len]
                rem_len -= 1
                tmp_len -= 1
        return tmp_zero
    else:
        return remainder




def mul_poly(remainder, gen, i):
    temp = []
    for j in range(len(gen)):
        temp.append(mul_tab[remainder[i]][gen[j]])

    return temp
def xor_poly(remainder, gen, temp, i):
    wynik = []
    for j in range(len(gen)):
        wynik.append(add_tab[remainder[i+j]][temp[j]])
    return wynik
def delete_if_zero_in_result(wynik, poly1,i,poly2):
    while wynik and wynik[0] == 255 :
        wynik.pop(0)

    num_of_last_num = len(poly1) - (len(poly2)+ i)
    while num_of_last_num > 0:

            num = len(poly1) - num_of_last_num
            wynik.append(poly1[num])
            num_of_last_num -= 1


    return wynik , 0


# couter_power = 0
# help_mess = mess.copy()
# while couter_power < 6:
#     help_mess.append(255)
#     couter_power += 1
#
# encode = div(help_mess, gen_poly)
#
# full_mess = mess + encode
# print(encode)
#
# print(full_mess)

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
#sydnromes_group = cal_syndroms(full_mess)
#print(sydnromes_group)

#print(div(full_mess,gen_poly))
print(gen_poly)
msg_a = [3,255,255,255]
msg_b = [255,2,255,255]
msg_c = [255,255,1,255]
msg_target = [3,2,1,255]


couter_power = 0
help_mess = msg_a.copy()
while couter_power < 6:
    help_mess.append(255)
    couter_power += 1

encode = div(help_mess, gen_poly, False)

full_mess_a = msg_a + encode

# print("Wiadomosc a: " + str(msg_a))
# print("Wiadomosc a po zakodowaniu : " + str(full_mess_a))



couter_power = 0
help_mess2 = msg_b.copy()
while couter_power < 6:
    help_mess2.append(255)
    couter_power += 1

encode = div(help_mess2, gen_poly, False)

full_mess_b = msg_b + encode

# print("Wiadomosc b: " + str(msg_b))
# print("Wiadomosc b po zakodowaniu : " + str(full_mess_b))



couter_power = 0
help_mess3 = msg_c.copy()
while couter_power < 6:
    help_mess3.append(255)
    couter_power += 1

encode = div(help_mess3, gen_poly, False)

full_mess_c = msg_c + encode

print("Wiadomosc c: " + str(msg_c))
print("Wiadomosc c po zakodowaniu : " + str(full_mess_c))



couter_power = 0
help_mess4 = msg_target.copy()
while couter_power < 6:
    help_mess4.append(255)
    couter_power += 1

encode = div(help_mess4, gen_poly, False)

full_mess_target = msg_target + encode

print("Wiadomosc targetu: " + str(msg_target))
print("Wiadomosc target po zakodowaniu : " + str(full_mess_target))

full_mess_do_por = []

for i in range(len(full_mess_a)):
    full_mess_do_por.append(add_tab[full_mess_c[i]][add_tab[full_mess_a[i]][full_mess_b[i]]])



print("Wiadomosc xorowana po zakodowaniu : " + str(full_mess_do_por))

# full_mess_c[2] = 2
# full_mess_c[9] = 90
# full_mess_c[3] = 152
full_mess_c[3] = 8
print(full_mess_c)
big_vector += full_mess_c
print(len(big_vector))

def shift(direction, polly):
    result = []
    if(direction == True): #shift right
        polly.insert(0, polly[len(polly) - 1])
        polly.pop()
        return polly
    else:   #left
        polly.append(polly[0])
        polly.pop(0)
        return polly

def calculate_wage(polly):
    w = 0
    for i in range(0, len(polly)):
        if polly[i] != 255:
            w+=1
    return w

def xor_polly(polly1, polly2):
    polly3 = []
    for i in range(0, len(polly2)):
        polly3.append(add_tab[polly1[i]][polly2[i]])
    return polly3

def shift_n_times(n, polly, direction):
        for i in range(0,n):
            shift(direction,polly)
        return polly


def simplified_decoder(big_vector,gen,k,t):
    tmp_syndrom = []
    result = []
    i = 0
    while(True):
        tmp_syndrom = div(big_vector[-10:],gen,True)
        w = calculate_wage(tmp_syndrom)
        if w <= t:
            big_vector = xor_polly(big_vector[-10:],tmp_syndrom)
            result = shift_n_times(i,big_vector,False)
            return result
            break
        else:
            if i != k:
                big_vector = shift(True,big_vector)
                i+= 1
            else:
                print("Cant decode message")
                break


print(simplified_decoder(big_vector,gen_poly,k,t))
# full_mess_c[9] = 90
print(str(div(full_mess_c,gen_poly, True)))