from coder import Coder
from generatingPolynomial import GeneratingPolynomial
from primeElements import PrimeElements
from simplifiedDecoder import SimplifiedDecoder
from division import Division
from testForDecoder import TestForDecoder


message = [1,2,3,5,5,5,6,1,1]
n = 15
k = 9
t = 3
r = 6


#
coder = Coder()
generatingPolynomial = GeneratingPolynomial()
simplifiedDecoder = SimplifiedDecoder()
primeElements = PrimeElements()
testForDecoder = TestForDecoder()
division = Division()



full_mess = coder.encode_message(message)
full_mess[8] = 1

print(simplifiedDecoder.simplified_decoder(full_mess,generatingPolynomial.gen_poly,9,3))



# testForDecoder.test_3_mistakes_in_message(coder,simplifiedDecoder,generatingPolynomial)
# testForDecoder.test_2_mistake_in_message(coder,simplifiedDecoder,generatingPolynomial)
# testForDecoder.test_1_mistake_in_message(coder,simplifiedDecoder,generatingPolynomial)
#
# testForDecoder.test_3_mistakes_in_whole(coder,simplifiedDecoder,generatingPolynomial)
# testForDecoder.test_2_mistake_in_whole(coder,simplifiedDecoder,generatingPolynomial)
# testForDecoder.test_1_mistake_in_whole(coder,simplifiedDecoder,generatingPolynomial)
#
# testForDecoder.test_3_mistakes_in_correction(coder,simplifiedDecoder,generatingPolynomial)
# testForDecoder.test_2_mistake_in_correction(coder,simplifiedDecoder,generatingPolynomial)
# testForDecoder.test_1_mistake_in_correction(coder,simplifiedDecoder,generatingPolynomial)




