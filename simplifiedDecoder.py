from primeElements import PrimeElements
from division import  Division
class SimplifiedDecoder:
    big_vector = []
    prim = PrimeElements()
    divisor = Division()
    def __init__(self):
        self.create_big_vector()



    def create_big_vector(self):
        for i in range(0, 244):
            self.big_vector.append(255)



    def shift(self, direction, polly):
        result = []
        if (direction == True):  # shift right
            polly.insert(0, polly[len(polly) - 1])
            polly.pop()
            return polly
        else:  # left
            polly.append(polly[0])
            polly.pop(0)
            return polly


    def calculate_wage(self,polly):
        w = 0
        for i in range(0, len(polly)):
            if polly[i] != 255:
                w += 1
        return w



    def xor_polly(self,polly1, polly2):
        polly3 = []
        for i in range(0, len(polly2)):
            polly3.append(self.prim.add_tab[polly1[i]][polly2[i]])
        return polly3


    def simplified_decoder(self, big_vector, gen, k, t):
        i = 0
        while (True):
            tmp_syndrom = self.divisor.div(big_vector[-10:], gen, True)
            w = self.calculate_wage(tmp_syndrom)
            if w <= t:
                big_vector = self.xor_polly(big_vector[-10:], tmp_syndrom)
                result = self.shift_n_times(i, big_vector, False)
                return result
                break
            else:
                if i != k:
                    big_vector = self.shift(True, big_vector)
                    i += 1
                else:
                    print("Cant decode message")
                    break






    def shift_n_times(self,n, polly, direction):
        for i in range(0, n):
          self.shift(direction, polly)
        return polly