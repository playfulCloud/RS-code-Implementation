import re
from primeElements import PrimeElements
class GeneratingPolynomial:
    prim = PrimeElements()
    def __init__(self):
        row = "x6+x5(a1+a2+a3+a4+a5+a6)+x4(a3+a4+a7+a10+a11)+x3(a6+a7+a9+a10+a11+a12+a14+a15)+x2(a10+a11+a14+a17+a18)+x(" \
              "a15+a16+a17+a18+a19+a20)+a21 "
        self.gen_poly = self.gen_fun_256(row)






    # function that generates generating polynomial for RS code
    def gen_fun_256(self, strum):
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
                        tab[i + 1] = "a" + str(self.prim.add_tab[int(num1[1])][int(num2[1])])
                        tab.remove(tab[i])
                        i -= 1
                i += 1
            except IndexError:
                print("error")

        for k in range(0, len(tab)):
            if 'a' in tab[k]:
                gen_alfa_tab.append(int(tab[k].split('a')[1]))

        return gen_alfa_tab

