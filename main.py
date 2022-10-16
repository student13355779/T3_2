import math
import time


class Wichislyator:

    def _sum(a):
        sumer = 0
        for bubu in a:
            sumer = sumer + bubu
        return sumer

    def _mult(date_file):
        biba = 1
        for lulu in date_file:
            biba = lulu * biba
        return biba

    def _min(popa):
        min = popa[0]
        for bukko in popa:
            if bukko <= min:
                min = bukko
        return min

    def _max(kisa):
        max = kisa[0]
        for bukko in kisa:
            if bukko >= max:
                max = bukko
        return max


    test_file = ["nummbers_1.txt", "nummbers_3.txt", "nummbers_4.txt"]
    for i in test_file:
        start = time.time()
        d = []
        with open(i) as f:
            for line in f:
                d.append([float(x) for x in line.split()])
        data = d[0]

        print("Результаты ВЫЧИСЛЯТОРА:")

        if _mult(data) >= 2e500:
            print("масимальное: ", _max(data))
            print("минимальное: ", _min(data))
            print("сумма: ", _sum(data))
            print(("произведение: ", "Слишком большое число"))
        elif _mult(data) <= -1 * 2e500:
            print("масимальное: ", _max(data))
            print("минимальное: ", _min(data))
            print("сумма: ", _sum(data))
            print("произведение: ", "Слишком большое отрицательное число")
        else:
            print("масимальное: ", _max(data))
            print("минимальное: ", _min(data))
            print("сумма: ", _sum(data))
            print("произведение: ", _mult(data))

        print("&&&")
        print("Результаты ТЕСТОВ:")

        if _mult(data) == math.prod(data) and _mult(data) < 2e500 and _mult(data) > (-1 * 2e500):
            print("_mult Ok")
        else:
            print('_mult BAD')
        if _sum(data) == sum(data):
            print("_sum Ok")
        else:
            print("_sum BAD")
        if _max(data) == max(data):
            print("_max Ok")
        else:
            print("_max BAD")
        if _min(data) == min(data):
            print("_minn Ok")
        else:
            print("_minn BAD")


        end = time.time()

        print((end - start) * 1000, "ms")
        print("********************")
        print(" ")

