from primeElements import PrimeElements
class Division:

    def __init__(self):
        self.prim = PrimeElements()


    #Division algoithm
    def div(self,poly1, poly2, isSyndrome):

        tmp_zero = []

        for k in range(0, 10):
            tmp_zero.append(255)

        if len(poly2) > len(poly1):
            return [], poly1

        remainder = poly1.copy()
        i = 0
        while len(remainder) >= len(poly2) and len(poly1) - (len(poly2) + i) >= 0:
            if remainder[i] != 255:  # jezeli sprawdzany znak jest rowny pierwszemu znakowy
                temp = self.mul_poly(remainder, poly2, i)
                wynik = self.xor_poly(remainder, poly2, temp, i)
                remainder, i = self.delete_if_zero_in_result(wynik, remainder, i, poly2)
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



    def mul_poly(self,remainder, gen, i):
        temp = []
        for j in range(len(gen)):
            temp.append(self.prim.mul_tab[remainder[i]][gen[j]])

        return temp



    def xor_poly(self, remainder, gen, temp, i):
        wynik = []
        for j in range(len(gen)):
            wynik.append(self.prim.add_tab[remainder[i + j]][temp[j]])
        return wynik




    def delete_if_zero_in_result(self, wynik, poly1, i, poly2):
        while wynik and wynik[0] == 255:
            wynik.pop(0)

        num_of_last_num = len(poly1) - (len(poly2) + i)
        while num_of_last_num > 0:
            num = len(poly1) - num_of_last_num
            wynik.append(poly1[num])
            num_of_last_num -= 1

        return wynik, 0