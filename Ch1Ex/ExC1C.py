import unittest
import random
import string
import copy

# C1.13
"""For each index at the start swap with the index at the back
Move one index forward and one index backwards
and swap those two until you have touched all indices"""


def reverse(data):
    start = 0
    back = -1
    visited_count = 0
    while visited_count < len(data):
        data[start], data[back] = data[back], data[start]
        start += 1
        back -= 1
        visited_count += 2
    return data


# C1.14
def findOddProduct(data):
    for i in range(len(data)):
        j = i + 1
        while j < len(data):
            if data[i] * data[j] % 2 == 1:
                return True
            else:
                j = j + 1
    return False


# C1.15
def hasDistinctEntries(data):
    for entry1 in data:
        counter = 0
        for entry2 in data:
            if entry1 == entry2:
                counter = counter + 1
            if counter > 1:
                return False
    return True


# C1.16
def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor


# The parameter data in the scale function is a list as such it is a mutable data type when referenced

# C1.17
def scale2(data, factor):
    for val in data:
        val *= factor


# the data will not be changed by the scale function in this implementation. The val is the result
# of an iterator and only exists in the functions scope, not in the callers scope.

# C1.18
def createByListComp1():
    return [x * (x + 1) for x in range(10)]


# C1.19
def alphabetListComp():
    # ord() function returns the number representing the unicode code of a specified character.
    # The chr() method returns a character string from the integer unicode code point of the character).
    [chr(i) for i in range(ord('a'), ord('z') + 1)]


# C1.20
def myShuffle(data):
    for i in range(len(data) // 2):
        ind1 = random.randint(0, len(data) - 1)
        ind2 = random.randint(0, len(data) - 1)
        data[ind1], data[ind2] = data[ind2], data[ind1]


# C1.21
# Ctrl+Z to send EOF to windows cannot do in Pycharm REPL need to use Terminal
def reverseInput():
    print("Enter some stuff")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.insert(0, line)
    for entry in contents:
        print(entry)


# C1.22
def dotProd(a, b):
    ret = []
    for i, j in zip(a, b):
        ret.append(i * j)
    return ret


# C1.23
def bufferOverflow(list):
    try:
        list[2] = 15
    except IndexError:
        print('Don\'t try buffer overflow attacks in Python')


# C1.24
def countVowels(teststr):
    lstring = teststr.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for vowel in vowels:
        for char in lstring:
            if char == vowel:
                count += 1
    return count


# C1.25
def remPunct(teststr):
    l = list(teststr)
    for mark in string.punctuation:
        for i in l:
            if i == mark:
                l.remove(i)
    return ''.join([str(elem) for elem in l])


# C1.26
def isArithmetic():
    a = int(input("Enter 3 numbers"))
    b = int(input())
    c = int(input())
    if a + b == c:
        return True
    elif a == b - c:
        return True
    elif a * b == c:
        return True
    else:
        return False


# C1.27
def factors(n):
    k = 1
    upperFactors = []
    while k * k < n:
        if n % k == 0:
            yield k
            upperFactors.insert(0, n // k)
        k+=1
    if k * k == n:
        yield k
    for i in upperFactors:
        yield i

# C1.28
def norm(v,p=2):
    sum = 0
    for coord in v:
        sum=sum+coord**p
    return sum**(1/p)




class TestAnsC1(unittest.TestCase):
    def testRev(self):
        testdata = [1, 2, 3, 4]
        testdata2 = [1, 2, 3, 4, 5]
        self.assertEqual(reverse(testdata), [4, 3, 2, 1])
        self.assertEqual(reverse(testdata2), [5, 4, 3, 2, 1])

    def testFindOddProduct(self):
        testdata = [1, 2]
        testdata2 = [1, 2, 3]
        testdata3 = [2, 2, 3, 5]
        testdata4 = [1, 2, 4, 6]
        self.assertFalse(findOddProduct(testdata))
        self.assertTrue(findOddProduct(testdata2))
        self.assertTrue(findOddProduct(testdata3))
        self.assertFalse(findOddProduct(testdata4))

    def testHasDistinct(self):
        testdata = [1]
        testdata2 = [1, 2]
        testdata3 = [1, 2, 2]
        testdata4 = [1, 2, 3, 4]
        testdata5 = [0, 1, 2, 3, 4, 5, 6, 7, 4]
        self.assertTrue(hasDistinctEntries(testdata))
        self.assertTrue(hasDistinctEntries(testdata2))
        self.assertTrue(hasDistinctEntries(testdata4))
        self.assertFalse(hasDistinctEntries(testdata3))
        self.assertFalse(hasDistinctEntries(testdata5))

    def lookAtScale(self):
        testdata = [1, 2, 3, 4, 5, 6, 7]
        scale(testdata, 2)
        self.assertEqual(testdata, [2, 4, 6, 8, 10, 12, 14])


if __name__ == '__main__':
    unittest.main()
