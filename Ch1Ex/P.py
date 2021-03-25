# 1.29
def allCombos():
    data = ['c', 'a', 't', 'd', 'o', 'g']
    words = []
    for firstletter in data:
        rem1 = list(data)
        rem1.remove(firstletter)
        for secondLetter in rem1:
            rem2 = list(rem1)
            rem2.remove(secondLetter)
            for thirdLetter in rem2:
                rem3 = list(rem2)
                rem3.remove(thirdLetter)
                for fourthLetter in rem3:
                    rem4 = list(rem3)
                    rem4.remove(fourthLetter)
                    for fifthLetter in rem4:
                        rem5 = list(rem4)
                        rem5.remove(fifthLetter)
                        words.append(firstletter + secondLetter + thirdLetter + fourthLetter + fifthLetter + rem5[0])
    return words


# 1.30
def howManyHalfs(number):
    if number<=2:
        raise ValueError('Number must be greater than 2')
    quotient = number
    counter = 0
    while quotient > 2:
        quotient = quotient / 2
        counter += 1
    return counter, quotient

# 1.31

