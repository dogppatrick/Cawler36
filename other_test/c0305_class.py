import random
class Person:
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def cbmi(self):
        return self.w/(self.h**2)


class Guessgame:
    def __init__(self, high, low):
        self.high = high
        self.low = low
        self.ans = random.randint(low, high)
        print(self.ans)

    def guess(self, g):
        if g > self.ans:
            self.high = g
        elif g < self.ans:
            self.low = g
        else:
            print("done")
            return True

    def __str__(self):

        return str(self.low) + "-" + str(self.high)


# p1 = Person(1.8, 60)
# print(p1.cbmi())
g1 = Guessgame(40, 1)

while True:
    print(g1)
    n = int(input())
    if g1.guess(n):
        break
