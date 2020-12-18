import numpy as np
import random


class Person:
    def __init__(self):
        self.Atr = np.random.randint(0, 2, 30)
        self.hp = 0

    def getSum(self):
        sum = 0
        for i in range(30):
            sum = sum + self.Atr[i]
            self.hp = sum


class Population:
    def __init__(self):
        self.P = []
        for i in range(10):
            ind = Person()
            self.P.append(ind)

    def getData(self):
        for i in range(10):
            for j in range(30):
                print(self.P[i].Atr[j], end="")
            print(" = ", end="")
            self.P[i].getSum()
            print(self.P[i].hp)


p1 = Population()
print("Данные о популяции в начале")
p1.getData()

Dad = Person()
Mom = Person()
Child1 = Person()
Child2 = Person()
AllPeople = []

for j in range(20):
    AllPeople.append(Person())
print("\n")
print("\n")
print("\n")
print("Началась жизнь")

for p in range(50):
    for i in range(10):
        for j in range(30):
            AllPeople[i].Atr[j] = p1.P[i].Atr[j]

    icount = 0

    for s in range(0, 10, 2):
        for j in range(30):
            Mom.Atr[j] = p1.P[icount + 5].Atr[j]
            Dad.Atr[j] = p1.P[random.randint(0, 9)].Atr[j]

        icount += 1
        ran = random.random()

        if ran > 0.8:
            for n in range(5):
                Child1.Atr[n] = Dad.Atr[n]
                Child2.Atr[n] = Mom.Atr[n]

            for n in range(5, 30):
                Child1.Atr[n] = Mom.Atr[n]
                Child2.Atr[n] = Dad.Atr[n]

        if (ran > 0.6) & (ran <= 0.8):
            for n in range(15):
                Child1.Atr[n] = Dad.Atr[n]
                Child2.Atr[n] = Mom.Atr[n]
            for n in range(16, 30):
                Child1.Atr[n] = Mom.Atr[n]
                Child2.Atr[n] = Dad.Atr[n]

        if (ran < 0.6) & (ran >= 0.4):
            for n in range(25):
                Child1.Atr[n] = Dad.Atr[n]
                Child2.Atr[n] = Mom.Atr[n]
            for n in range(25, 30):
                Child1.Atr[n] = Mom.Atr[n]
                Child2.Atr[n] = Dad.Atr[n]

        if (ran < 0.4) & (ran >= 0.3):
            for n in range(15):
                Child1.Atr[n] = Dad.Atr[14 - n]
                Child2.Atr[n] = Mom.Atr[14 - n]
            for n in range(15, 30):
                Child1.Atr[n] = Mom.Atr[44 - n]
                Child2.Atr[n] = Dad.Atr[44 - n]

        if ran < 0.3:
            for n in range(15):
                Child1.Atr[n] = Dad.Atr[n]
                Child1.Atr[n + 15] = Mom.Atr[n]
                Child2.Atr[n] = Mom.Atr[n + 15]
                Child2.Atr[n + 15] = Dad.Atr[n + 15]

        for i in range(30):
            AllPeople[10 + s].Atr[i] = Child1.Atr[i]
            AllPeople[11 + s].Atr[i] = Child2.Atr[i]

        for w in range(30):
            if random.random() < 0.001:
                if AllPeople[15].Atr[w] == 1:
                    AllPeople[15].Atr[w] = 0
                if AllPeople[15].Atr[w] == 0:
                    AllPeople[15].Atr[w] = 1

    for i in range(20):
        AllPeople[i].getSum()

    for m in range(len(AllPeople) - 1, 0, -1):
        for b in range(m):
            if AllPeople[b].hp > AllPeople[b + 1].hp:
                sor = AllPeople[b]
                AllPeople[b] = AllPeople[b + 1]
                AllPeople[b + 1] = sor

    for i in range(10):
        for j in range(30):
            p1.P[i].Atr[j] = AllPeople[i + 10].Atr[j]

    p1.getData()
