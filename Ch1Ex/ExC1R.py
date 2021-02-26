import unittest
import random as rd


# R1.1
def is_multiple(n, m):
    if n % m == 0:
        return True
    return False


# R1.2
def is_even(k):
    while True:
        if k == 1 or k == -1:
            return False
        if k == 0:
            return True
        if k < 0:
            k += 2
        if k > 0:
            k -= 2


# R1.3
def minmax(data):
    min = data[0]
    max = data[0]
    for num in data:
        if num < min:
            min = num
        if num > max:
            max = num
    return min, max


# R1.4
def sumSquares(n):
    sum = 0
    for i in range(n):
        sum += i * i
    return sum


# R1.5
def sumSquaresComp(n):
    return sum([x * x for x in range(n)])


# R1.6 + 1.7
def sumOddSquares(n):
    return sum([x * x for x in range(n) if x % 2 != 0])


# R1.8
def findPosIndex(n, k):
    return k + n


# R1.9
def giveRange():
    for x in range(50, 81, 10):
        print(x)


# R1.10
def giveRange2():
    for x in range(8, -9, -2):
        print(x)


# R1.11
def geomComp():
    return [pow(2, x) for x in range(9)]


# R1.12
def choice(data):
    index_picked = rd.randrange(0, len(data))
    return data[index_picked]

# R1.13


class TestAnsR1(unittest.TestCase):

    def testObviousMultiples(self):
        self.assertTrue(is_multiple(9, 3))
        self.assertTrue(is_multiple(4, 2))

    def testEven(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(-2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(24))
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(-1))
        self.assertFalse(is_even(-11))
        self.assertFalse(is_even(111))

    def testMinMax(self):
        self.assertEqual(minmax([1, 2, 3, 4, 5, 6]), (1, 6))
        self.assertEqual(minmax([1, 1, 1, 1, 1, 1]), (1, 1))

    def testSumSquare(self):
        self.assertEqual(sumSquares(5), 30)


if __name__ == '__main__':
    unittest.main()
