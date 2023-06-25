from coder import Coder
from generatingPolynomial import GeneratingPolynomial
from primeElements import PrimeElements
from simplifiedDecoder import SimplifiedDecoder
from division import Division
from testForDecoder import TestForDecoder
from reedsolo import RSCodec, xrange, gf_poly_mul, gf_pow, _bytearray
import random

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

testForDecoder.test_3_mistakes_in_message(coder,simplifiedDecoder,generatingPolynomial)
testForDecoder.test_2_mistake_in_message(coder,simplifiedDecoder,generatingPolynomial)
testForDecoder.test_1_mistake_in_message(coder,simplifiedDecoder,generatingPolynomial)