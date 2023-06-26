import random

class TestForDecoder:
    def test_3_mistakes_in_message(self, coder, simplifiedDecoder, generatingPolynomial):
        all_answers = 5
        corrected_answer = 0
        x = 0
        for i in range(0,5):
            combination = [random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15)]
            fullmess = coder.encode_message(combination)
            while len(fullmess)<15:
               repeat_combination = [random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15)]
               fullmess = coder.encode_message(repeat_combination)

            oryginal_message = fullmess
            mistake_on_random_posstion1 = random.randint(0, 15)
            random_possition1 = random.randint(0, 8)
            mistake_on_random_posstion2 = random.randint(0, 15)
            random_possition2 = random.randint(0, 8)
            mistake_on_random_posstion = random.randint(0, 15)
            random_possition = random.randint(0, 8)
            fullmess[random_possition] = mistake_on_random_posstion
            fullmess[random_possition1] = mistake_on_random_posstion1
            fullmess[random_possition2] = mistake_on_random_posstion2

            decoded_message, wynik = simplifiedDecoder.simplified_decoder(fullmess,generatingPolynomial.gen_poly,9,3)
            #print(decoded_message)
            if wynik:
                corrected_answer+=1
                #print("Corrected" + str((x / all_answers)))
            #print(wynik)
            else:
                print(fullmess)
            x+=1
        print("Percentage of correctly decoded messages: " + str((corrected_answer / all_answers) * 5) + " %")

    def test_1_mistake_in_message(self, coder, simplifiedDecoder, generatingPolynomial):
        all_answers = 5
        corrected_answer = 0
        x = 0
        for i in range(0,5):
            combination = [random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15)]
            fullmess = coder.encode_message(combination)
            oryginal_message = fullmess
            mistake_on_random_posstion = random.randint(0, 15)
            random_possition = random.randint(0, 8)
            fullmess[random_possition] = mistake_on_random_posstion
            while len(fullmess) < 15:
                repeat_combination = [random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                                      random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                                      random.randint(1, 15), random.randint(1, 15), random.randint(1, 15)]
                fullmess = coder.encode_message(repeat_combination)
            decoded_message, wynik = simplifiedDecoder.simplified_decoder(fullmess,generatingPolynomial.gen_poly,9,3)
            #print(decoded_message)
            if wynik:
                corrected_answer+=1
                #print("Corrected" + str((x / all_answers)))
            #print(wynik)
            else:
                print(fullmess)
            x+=1
        print("Percentage of correctly decoded messages: " + str((corrected_answer / all_answers) * 5) + " %")


    def test_2_mistake_in_message(self, coder, simplifiedDecoder, generatingPolynomial):
        all_answers = 5
        corrected_answer = 0
        x = 0
        for i in range(0, 5):
            combination = [random.randint(1, 15), random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                           random.randint(1, 15), random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                           random.randint(1, 15)]
            fullmess = coder.encode_message(combination)
            oryginal_message = fullmess
            while len(fullmess) < 15:
                repeat_combination = [random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                                      random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                                      random.randint(1, 15), random.randint(1, 15), random.randint(1, 15)]
                fullmess = coder.encode_message(repeat_combination)
            mistake_on_random_posstion1 = random.randint(0, 15)
            random_possition1 = random.randint(0, 8)
            mistake_on_random_posstion = random.randint(0, 15)
            random_possition = random.randint(0, 8)
            fullmess[random_possition] = mistake_on_random_posstion
            fullmess[random_possition1] = mistake_on_random_posstion1

            decoded_message, wynik = simplifiedDecoder.simplified_decoder(fullmess, generatingPolynomial.gen_poly, 9, 3)
            # print(decoded_message)
            if wynik:
                corrected_answer += 1
                # print("Corrected" + str((x / all_answers)))
            # print(wynik)
            else:
                print(fullmess)
            x += 1
        print("Percentage of correctly decoded messages: " + str((corrected_answer / all_answers) * 5) + " %")

    def test_3_mistakes_in_whole(self, coder, simplifiedDecoder, generatingPolynomial):
        all_answers = 5
        corrected_answer = 0
        x = 0
        for i in range(0,5):
            combination = [random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15)]
            fullmess = coder.encode_message(combination)
            oryginal_message = fullmess
            while len(fullmess) < 15:
                repeat_combination = [random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                                      random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                                      random.randint(1, 15), random.randint(1, 15), random.randint(1, 15)]
                fullmess = coder.encode_message(repeat_combination)

            mistake_on_random_posstion1 = random.randint(0, 15)
            random_possition1 = random.randint(0, 14)
            mistake_on_random_posstion2 = random.randint(0, 15)
            random_possition2 = random.randint(0, 14)
            mistake_on_random_posstion = random.randint(0, 15)
            random_possition = random.randint(0, 14)
            fullmess[random_possition] = mistake_on_random_posstion
            fullmess[random_possition1] = mistake_on_random_posstion1
            fullmess[random_possition2] = mistake_on_random_posstion2

            decoded_message, wynik = simplifiedDecoder.simplified_decoder(fullmess,generatingPolynomial.gen_poly,9,3)
            #print(decoded_message)
            if wynik:
                corrected_answer+=1
                #print("Corrected" + str((x / all_answers)))
            #print(wynik)
            else:
                print(fullmess)
            x+=1
        print("Percentage of correctly decoded messages: " + str((corrected_answer / all_answers) * 5) + " %")

    def test_1_mistake_in_whole(self, coder, simplifiedDecoder, generatingPolynomial):
        all_answers = 5
        corrected_answer = 0
        x = 0
        for i in range(0,5):
            combination = [random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15)]
            fullmess = coder.encode_message(combination)
            oryginal_message = fullmess
            while len(fullmess) < 15:
                repeat_combination = [random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                                      random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                                      random.randint(1, 15), random.randint(1, 15), random.randint(1, 15)]
                fullmess = coder.encode_message(repeat_combination)
            mistake_on_random_posstion = random.randint(0, 15)
            random_possition = random.randint(0, 14)
            fullmess[random_possition] = mistake_on_random_posstion

            decoded_message, wynik = simplifiedDecoder.simplified_decoder(fullmess,generatingPolynomial.gen_poly,9,3)
            #print(decoded_message)
            if wynik:
                corrected_answer+=1
                #print("Corrected" + str((x / all_answers)))
            #print(wynik)
            else:
                print(fullmess)
            x+=1
        print("Percentage of correctly decoded messages: " + str((corrected_answer / all_answers) * 5) + " %")


    def test_2_mistake_in_whole(self, coder, simplifiedDecoder, generatingPolynomial):
        all_answers = 5
        corrected_answer = 0
        x = 0
        for i in range(0, 5):
            combination = [random.randint(1, 15), random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                           random.randint(1, 15), random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                           random.randint(1, 15)]
            fullmess = coder.encode_message(combination)
            oryginal_message = fullmess
            while len(fullmess) < 15:
                repeat_combination = [random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                                      random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                                      random.randint(1, 15), random.randint(1, 15), random.randint(1, 15)]
                fullmess = coder.encode_message(repeat_combination)
            mistake_on_random_posstion1 = random.randint(0, 15)
            random_possition1 = random.randint(0, 14)
            mistake_on_random_posstion = random.randint(0, 15)
            random_possition = random.randint(0, 14)
            fullmess[random_possition] = mistake_on_random_posstion
            fullmess[random_possition1] = mistake_on_random_posstion1

            decoded_message, wynik = simplifiedDecoder.simplified_decoder(fullmess, generatingPolynomial.gen_poly, 9, 3)
            # print(decoded_message)
            if wynik:
                corrected_answer += 1
                # print("Corrected" + str((x / all_answers)))
            # print(wynik)
            else:
                print(fullmess)
            x += 1
        print("Percentage of correctly decoded messages: " + str((corrected_answer / all_answers) * 5) + " %")

    def test_3_mistakes_in_correction(self, coder, simplifiedDecoder, generatingPolynomial):
        all_answers = 5
        corrected_answer = 0
        x = 0
        for i in range(0,5):
            combination = [random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15)]
            fullmess = coder.encode_message(combination)
            oryginal_message = fullmess
            while len(fullmess) < 15:
                repeat_combination = [random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                                      random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                                      random.randint(1, 15), random.randint(1, 15), random.randint(1, 15)]
                fullmess = coder.encode_message(repeat_combination)
            else:
                mistake_on_random_posstion1 = random.randint(0, 15)
                random_possition1 = random.randint(8, 14)
                mistake_on_random_posstion2 = random.randint(0, 15)
                random_possition2 = random.randint(8, 14)
                mistake_on_random_posstion = random.randint(0, 15)
                random_possition = random.randint(8, 14)
                fullmess[random_possition] = mistake_on_random_posstion
                fullmess[random_possition1] = mistake_on_random_posstion1
                fullmess[random_possition2] = mistake_on_random_posstion2

            decoded_message, wynik = simplifiedDecoder.simplified_decoder(fullmess,generatingPolynomial.gen_poly,9,3)
            #print(decoded_message)
            if wynik:
                corrected_answer+=1
                #print("Corrected" + str((x / all_answers)))
            #print(wynik)
            else:
                print(fullmess)
            x+=1
        print("Percentage of correctly decoded messages: " + str((corrected_answer / all_answers) * 5) + " %")

    def test_1_mistake_in_correction(self, coder, simplifiedDecoder, generatingPolynomial):
        all_answers = 5
        corrected_answer = 0
        x = 0
        for i in range(0,5):
            combination = [random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15),random.randint(1, 15)]
            fullmess = coder.encode_message(combination)
            oryginal_message = fullmess
            while len(fullmess) < 15:
                repeat_combination = [random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                                      random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                                      random.randint(1, 15), random.randint(1, 15), random.randint(1, 15)]
                fullmess = coder.encode_message(repeat_combination)
            mistake_on_random_posstion = random.randint(0, 15)
            random_possition = random.randint(8, 14)
            fullmess[random_possition] = mistake_on_random_posstion

            decoded_message, wynik = simplifiedDecoder.simplified_decoder(fullmess,generatingPolynomial.gen_poly,9,3)
            #print(decoded_message)
            if wynik:
                corrected_answer+=1
                #print("Corrected" + str((x / all_answers)))
            #print(wynik)
            x+=1
        print("Percentage of correctly decoded messages: " + str((corrected_answer / all_answers) * 5) + " %")


    def test_2_mistake_in_correction(self, coder, simplifiedDecoder, generatingPolynomial):
        all_answers = 5
        corrected_answer = 0
        x = 0
        for i in range(0, 5):
            combination = [random.randint(1, 15), random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                           random.randint(1, 15), random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                           random.randint(1, 15)]
            fullmess = coder.encode_message(combination)
            oryginal_message = fullmess
            if len(fullmess) < 15:
                # print(oryginal_message)
                continue
            mistake_on_random_posstion1 = random.randint(0, 15)
            random_possition1 = random.randint(8, 14)
            mistake_on_random_posstion = random.randint(0, 15)
            random_possition = random.randint(8, 14)
            fullmess[random_possition] = mistake_on_random_posstion
            fullmess[random_possition1] = mistake_on_random_posstion1

            decoded_message, wynik = simplifiedDecoder.simplified_decoder(fullmess, generatingPolynomial.gen_poly, 9, 3)
            # print(decoded_message)
            if wynik:
                corrected_answer += 1
                # print("Corrected" + str((x / all_answers)))
            # print(wynik)
            else:
                print(fullmess)
            x += 1
        print("Percentage of correctly decoded messages: " + str((corrected_answer / all_answers) * 5) + " %")
