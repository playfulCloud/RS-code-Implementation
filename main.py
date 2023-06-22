from coder import Coder
from simplifiedDecoder import SimplifiedDecoder
from generatingPolynomial import GeneratingPolynomial
from primeElements import PrimeElements

#PARAMETRY KODU:
n = 10
k = 4
t = 3
r = 6


mesage = [1,2,3,4]
coder = Coder()
generatingPolynomial = GeneratingPolynomial()
simplifiedDecoder = SimplifiedDecoder()
primeElements = PrimeElements()

print("Wielomian generujacy")
print(generatingPolynomial.gen_poly)


print("Oryginalna Wiadomosc po zakodowaniu")
full_mess = coder.encode_message(mesage)
print(full_mess)

#Reczne stworzenie bledu
full_mess[0] = 2


print("Zmiana")
print(full_mess)

print("Wiadomosc Zdekodowana")
#Stworzenie wektora rozszczerzonego lewo i prawo stronnie zerami potrzebnego do procesu dekodowania
zero_right_left_extented_vector = full_mess + simplifiedDecoder.big_vector
decoded_message = simplifiedDecoder.simplified_decoder(zero_right_left_extented_vector,generatingPolynomial.gen_poly,k,t)
print(decoded_message)


