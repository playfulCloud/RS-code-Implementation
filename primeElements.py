import komm
class PrimeElements:
    def __init__(self):
        self.field = komm.FiniteBifield(8,modulus=0b100011101)  # zdefiniowanie GF(2^8) i wielomianu pierwotnego x^8+x^4+x^3+x^2+1
        self.alpha = self.field.primitive_element
        self.prim_elements = {255: 0b0}  # stworzenie słownika przechowującego warotści każdej alfy, wartość 256 to wartość
        self.create_and_add_to_prime_elements()
        self.add_tab = [[self.find_alpha(self.prim_elements[i] ^ self.prim_elements[j]) for j in range(256)] for i in range(256)]   #Creating tab of results of addition two values
        self.mul_tab = [[((i + j) % 255) for j in range(256)] for i in range(256)]  #Creating tab of results of multiplication

        # specjalna która jest czystym zerem

    # Return value of alpha based on prim element
    def find_alpha(self,value):
        for i in range(0, len(self.prim_elements)):
            if self.prim_elements[i] == value:
                return i



    def create_and_add_to_prime_elements(self):
        for i in range(0, 255):
            tmp = str(self.alpha ** i)
            tmp = tmp.replace('0b', '')
            self.prim_elements[i] = int(tmp, base=2)



    def display_prime_elements(self):
        for i in range(len(self.prim_elements)):
            print(str(i) + " " + str(self.prim_elements[i]))


