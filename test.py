import unittest
from datetime import datetime

from main import Wichislyator

class WichislyatorTest(unittest.TestCase):
    def setUp(self):
        self.wich = Wichislyator()
        self.begin = datetime.now()

    def tearDown(self):
        self.end = datetime.now()
        self.diff = self.end - self.begin
        print(self.diff.microseconds / 1000, "ms")

    def test_sum (self):
        self.assertEqual(16, self.wich.summ("nummbers_3.txt"))

    def test_min(self):
        self.assertEqual(-124, self.wich.minn("nummbers_4.txt"))







"""import math
import time

spisok = []

def summ(ass):
    sumer = 0
    for bubu in ass:
        sumer = sumer + bubu
    return sumer

def mult(picya):
    mult = 1
    for lulu in picya:
        mult = lulu * mult
    if type(lulu) not in [int, float]:
        raise TypeError("Чиcло должно соответствовать формату [int. float.")
    return mult

def minn(popochka):
    min = popochka[0]
    for bukko in popochka:
        if bukko <= min:
            min = bukko
    return min

def maxx(kisonyka):
    max = kisonyka[0]
    for bukko in kisonyka:
        if bukko >= max:
            max = bukko
    return max


test_file = ["nummbers.txt", "nummbers_2.txt", "nummbers_3.txt", "nummbers_4.txt", "nummbers_5.txt", "nummbers_6.txt", "nummbers_7.txt", "nummbers_8.txt", "nummbers_9.txt", "nummbers_10.txt"]
for i in test_file:
    start = time.time()
    d = []
    with open(i) as f:
        for line in f:
            d.append([float(x) for x in line.split()])
    data = d[0]

    print(maxx(data),
        minn(data))

    if mult(data) == math.prod(data):
        print("mult Ok")
    if summ(data) == sum(data):
        print("summ Ok")
    if maxx(data) == max(data):
        print ("max Ok")
    if minn(data) == min(data):
        print ("minn Ok")


    end = time.time()

    print(end - start)
    print(" ")
    print(" ")

"""