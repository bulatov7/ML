import matplotlib.pyplot as plt
import matplotlib.colors as colorsq
import numpy as np


def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


n = 200
eps, minPts = 5, 3
color_list = []
for i in range(n):
    color_list.append('r')
# colors_list = list(colorsq._colors_full_map.values())
colors = ['lavenderblush', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'black', 'darkmagenta', 'darkorange', 'maroon',
          'pink', 'crimson', 'lime', 'red', 'gray', 'olive', 'dodgerblue', 'skyblue']

x = [np.random.randint(1, 100) for i in range(n)]
y = [np.random.randint(1, 100) for i in range(n)]
flags = []
for i in range(0, n):
    neighb = -1
    for j in range(0, n):
        if dist(x[i], y[i], x[j], y[j]) <= eps:
            neighb += 1
    if neighb >= minPts:
        flags.append('g')
    else:
        flags.append('lavenderblush')
for i in range(0, n):
    if flags[i] == 'lavenderblush':
        for j in range(0, n):
            if flags[j] == 'g':
                if dist(x[i], y[i], x[j], y[j]) <= eps:
                    flags[i] = 'y'
clast = []
for i in range(n):
    clast.append(0)
c = 1
for i in range(0, n):
    if flags[i] == 'g':
        for j in range(0, n):
            if dist(x[i], y[i], x[j], y[j]) <= eps:
                if flags[j] == 'g':
                    if clast[i] == 0 and clast[j] == 0:
                        clast[i] = c
                        clast[j] = c
                        c += 1
                    elif clast[i] == 0 and clast[j] != 0:
                        clast[i] = clast[j]
                    elif clast[j] == 0 and clast[i] != 0:
                        clast[j] = clast[i]
                    elif clast[i] != 0 and clast[j] != 0:
                        if clast[i] < clast[j]:
                            clast[j] = clast[i]
                        else:
                            clast[i] = clast[j]
                elif flags[j] == 'y':
                    if clast[i] == 0:
                        clast[i] = c
                        c += 1

for i in range(0, n):
    if flags[i] == 'y':
        for j in range(0, n):
            if flags[j] == 'g':
                if dist(x[i], y[i], x[j], y[j]) <= eps and clast[j] != 0:
                    clast[i] = clast[j]

for i in range(n):
    if (clast[i] == 0):
        color_list[i] = colors[0]
    if (clast[i] == 1):
        color_list[i] = colors[1]
    if (clast[i] == 2):
        color_list[i] = colors[2]
    if (clast[i] == 3):
        color_list[i] = colors[3]
    if (clast[i] == 4):
        color_list[i] = colors[4]
    if (clast[i] == 5):
        color_list[i] = colors[5]
    if (clast[i] == 6):
        color_list[i] = colors[6]
    if (clast[i] == 7):
        color_list[i] = colors[7]
    if (clast[i] == 8):
        color_list[i] = colors[8]
    if (clast[i] == 9):
        color_list[i] = colors[9]
    if (clast[i] == 10):
        color_list[i] = colors[10]
    if (clast[i] == 11):
        color_list[i] = colors[11]
    if (clast[i] == 12):
        color_list[i] = colors[12]
    if (clast[i] == 13):
        color_list[i] = colors[13]
    if (clast[i] == 14):
        color_list[i] = colors[14]
    if (clast[i] == 15):
        color_list[i] = colors[15]
    if (clast[i] == 16):
        color_list[i] = colors[16]
    if (clast[i] == 17):
        color_list[i] = colors[17]
clast.sort()
print(clast)
for i in range(0, n):
    plt.scatter(x[i], y[i], color=flags[i])
plt.show()

for i in range(0, n):
    plt.scatter(x[i], y[i], color=color_list[i])
plt.show()
