from primeElements import PrimeElements
class RsDecoder:
    def __init__(self):
        self.prim = PrimeElements()


################ STEP 1 Counting all syndroms ############################
    def cal_syndroms(self,encrypt_mess):
        sydroms = []
        for symbol in range(1, 7):
            sydroms.append(self.cal_poly_syn(symbol, encrypt_mess))

        return sydroms


    def cal_poly_syn(self,alf_symbol, poly):
        tmp_tab = []
        for x in range(0, len(poly)):
            power = ((len(poly) - (x + 1)) * alf_symbol) % 255
            sym_tmp = poly[x]
            tmp_tab.append(self.prim.mul_tab[sym_tmp][power])

        wynik_tab = tmp_tab[0]
        for k in range(1, len(tmp_tab)):
            helper = self.prim.add_tab[wynik_tab][tmp_tab[k]]
            wynik_tab = self.prim.add_tab[wynik_tab][tmp_tab[k]]

        return wynik_tab
#######################################################################