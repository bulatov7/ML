import pygame as pygame
import numpy as np
from sklearn import svm

pygame.font.init()

screen = pygame.display.set_mode((1000, 600))
screen.fill((255, 255, 255))

data = np.empty((0, 5), dtype='f')


def create_data(pos, color):
    (x, y) = pos
    coord = [color[0], color[1], color[2], x, y]
    global data
    data = np.append(data, [coord], axis=0)
    points.append(pos)


def draw_circle():
    for point in data:
        pygame.draw.circle(screen, (point[0], point[1], point[2]), (int(point[3]), int(point[4])), radius, thickness)


radius = 5
selected_color = 123, 123, 123
selected_color_1 = 255, 200, 2

thickness = 0
points = []
clusters = []

pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                create_data(pygame.mouse.get_pos(), selected_color)
                clusters.append(0)
            elif event.button == 3:
                create_data(pygame.mouse.get_pos(), selected_color_1)
                clusters.append(1)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                model = svm.SVC(kernel='linear', C=1.0)
                model.fit(points, clusters)

                m = model.coef0

                W = model.coef_[0]
                I = model.intercept_

                n = -W[0] / W[1]
                xx = np.linspace(0, 1000, 1000)
                yy = n * xx - I[0] / W[1]

                pygame.draw.line(screen, (0, 0, 0), (xx[0], yy[0]), (xx[-1], yy[-1]), 2)
                pygame.display.update()

        draw_circle()
        pygame.display.flip()

pygame.quit()


