import matplotlib.pyplot as plt
import pandas as pd


def draw(dataset):
    numb = list(data.Passengerid)
    ages = list(dataset.Age)
    genders = list(dataset.Sex)
    colors = []
    for i in range(0, len(ages)):
        if genders[i] == 0:
            colors.append('r')
        else:
            colors.append('b')
    fig, ax = plt.subplots()
    ax.bar(numb, ages, color=colors)
    plt.show()


data = pd.read_csv("titanic.csv")
draw(data)
