import matplotlib.pyplot as plt
import numpy as np

n = 100
x = [np.random.randint(1, n) for i in range(n)]
y = [np.random.randint(1, n) for i in range(n)]

x_c = np.mean(x)
y_c = np.mean(y)


def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def clust(x, y, x_cc, y_cc, k):
    cluster = []
    for i in range(0, n):
        d = dist(x[i], y[i], x_cc[0], y_cc[0])
        numb = 0
        for j in range(0, k):
            if dist(x[i], y[i], x_cc[j], y_cc[j]) < d:
                d = dist(x[i], y[i], x_cc[j], y_cc[j])
                numb = j
        cluster.append(numb)
    return cluster


def k_means(k):
    R = 0
    for i in range(0, n):
        r = dist(x_c, y_c, x[i], y[i])
        if r > R:
            R = r

    x_cc = [R * np.cos(2 * np.pi * i / k) + x_c for i in range(k)]
    y_cc = [R * np.sin(2 * np.pi * i / k) + y_c for i in range(k)]
    # x_cc и y_cc - координаты центроидов
    cluster = clust(x, y, x_cc, y_cc, k)
    colors = ['r', 'b', 'g', 'y', 'black', 'purple', 'cyan', 'lime']
    f_sum = 0
    for i in range(0, n):
        sum = 0
        for k_count in range(0, k):
            if cluster[i] == k_count:
                sum += (x_cc[k_count] - x[i]) ** 2
        f_sum += sum
    return f_sum


f_sums = []
min_k = 999999
for i in range(2, 8):
    f_sums.append(k_means(i))
for i in range(0, 6):
    if (f_sums[i] < min_k):
        min_k = i
print("Суммы: ", f_sums, " Мин сумма", min(f_sums), " при k=", min_k + 5)


def calculateD(f_sums):
    d = 123456
    k_temp = 0
    sum = 0
    for i in range(1, 5):
        temp = (f_sums[i] - f_sums[i + 1]) / (f_sums[i - 1] - f_sums[i])
        if (temp < d):
            d = temp
            k_temp = i
            sum = f_sums[i]
        print(temp)
    print("d=", d, "k=", k_temp + 1, "при сумме=", sum)


calculateD(f_sums)
