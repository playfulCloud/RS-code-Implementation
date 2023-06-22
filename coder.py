from generatingPolynomial import GeneratingPolynomial
from division import Division
class Coder:
    def __init__(self):
        self.generatingPollynomial = GeneratingPolynomial()
        self.divisor = Division()



    def encode_message(self, uncoded_message):
        couter_power = 0
        help_mess = uncoded_message.copy()
        while couter_power < 6:
            help_mess.append(255)
            couter_power += 1
        encode = self.divisor.div(help_mess, self.generatingPollynomial.gen_poly, False)
        return uncoded_message+encode

