import unittest

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


if __name__ == '__main__':
    unittest.main()
