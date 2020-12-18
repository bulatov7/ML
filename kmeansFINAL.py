import matplotlib.pyplot as plt
import numpy as np
import random

n, clusters = 100, 7
x = [random.randint(1, 100) for i in range(n)]
y = [random.randint(1, 100) for i in range(n)]
x_c = np.mean(x)
y_c = np.mean(y)


def dist(x1, y1, x2, y2):
    return np.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))


def clust(x, y, x_cc, y_cc, k):
    cluster = []
    for i in range(0, n - 1):
        d = dist(x[i], y[i], x_cc[0], y_cc[0])
        numb = 0
        for j in range(0, k):
            if dist(x[i], y[i], x_cc[j], y_cc[j]) < d:
                d = dist(x[i], y[i], x_cc[j], y_cc[j])
                numb = j
        cluster.append(numb)
    return cluster


def kmeans(x_cc, y_cc, k):
    is_clustered = False
    countc = 0

    while not is_clustered:
        countc += 1
        clusters = clust(x, y, x_cc, y_cc, k)
        new_x_cc = []
        new_y_cc = []

        for i in range(0, k):
            summed_x = 0
            summed_y = 0
            count = 0

            for j in range(0, n - 1):
                if i == clusters[j]:
                    summed_x += x[j]
                    summed_y += y[j]
                    count += 1

            if count > 0:
                new_x_cc.append(summed_x / count)
                new_y_cc.append(summed_y / count)
            else:
                new_x_cc.append(x_cc[i])
                new_y_cc.append(y_cc[i])

        is_clustered = (x_cc == new_x_cc) & (y_cc == new_y_cc)
        x_cc = new_x_cc
        y_cc = new_y_cc
    return x_cc, y_cc


def С_sum(x, y, clusters, x_cc, y_cc):
    clusterSum = 0
    for i in range(0, n - 1):
        cluster = clusters[i]
        clusterSum += dist(x[i], y[i], x_cc[cluster], y_cc[cluster]) ** 2
    return clusterSum


R = 0
for i in range(0, n):
    r = dist(x_c, y_c, x[i], y[i])
    if r > R:
        R = r

c = []

for k in range(1, clusters + 1):
    x_cc = [R * np.cos(2 * np.pi * i / k) + x_c for i in range(k)]
    y_cc = [R * np.sin(2 * np.pi * i / k) + x_c for i in range(k)]

    x_ccEND, y_ccEND = kmeans(x_cc, y_cc, k)
    clustersEND = clust(x, y, x_ccEND, y_ccEND, k)
    c.append(С_sum(x, y, clustersEND, x_cc, y_cc))
    # draw(x, y, final_clusters, final_x_cc, final_y_cc, k)

d = [0] * clusters

for k in range(2, len(d) - 1):
    d[k] = np.abs(c[k] - c[k + 1]) / np.abs(c[k] - c[k - 1])

dimin = d[2]
idimin = 2
for i in range(2, len(d) - 1):
    if d[i] < dimin:
        dimin = d[i]
        idimin = i

optimalK = idimin
x_cc = [R * np.cos(2 * np.pi * i / optimalK) + x_c for i in range(optimalK)]
y_cc = [R * np.sin(2 * np.pi * i / optimalK) + x_c for i in range(optimalK)]
x_ccEND, y_ccEND = kmeans(x_cc, y_cc, optimalK)
clustersEND = clust(x, y, x_ccEND, y_ccEND, optimalK)


def draw(x, y, clusters, x_cc, y_cc, k):
    for i in range(0, n - 1):
        if clusters[i] == 0:
            plt.scatter(x[i], y[i], color='r')
        if clusters[i] == 1:
            plt.scatter(x[i], y[i], color='g')
        if clusters[i] == 2:
            plt.scatter(x[i], y[i], color='b')
        if clusters[i] == 3:
            plt.scatter(x[i], y[i], color='y')
        if clusters[i] == 4:
            plt.scatter(x[i], y[i], color='cyan')
        if clusters[i] == 5:
            plt.scatter(x[i], y[i], color='darkmagenta')
        if clusters[i] == 6:
            plt.scatter(x[i], y[i], color='lime')
        # тут надо больше цветов, можно сделать через matplotlib.colors,
        # но для 7 хватит этих цветов в ИФах)))
    for i in range(0, k):
        plt.scatter(x_cc[i], y_cc[i], color='black', s=100)
    plt.show()


draw(x, y, clustersEND, x_ccEND, y_ccEND, optimalK)
print(optimalK)
