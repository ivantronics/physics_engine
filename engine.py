import pygame
import math

wScreen = 1200
hScreen = 500

win = pygame.display.set_mode((wScreen, hScreen))
pygame.display.set_caption('Physics')


class ball(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius - 1)

    @staticmethod
    def ballPath(startx, starty, power, ang, time):
        angle = ang
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        distX = velx * time
        distY = (vely * time) + ((-4.9 * (time ** 2)) / 2)

        newx = round(distX + startx)
        newy = round(starty - distY)

        return (newx, newy)


def redrawWindow():
    win.fill((164, 164, 164))
    theball.draw(win)
    pygame.draw.line(win, (0, 0, 0), line[0], line[1])
    pygame.display.update()


def findAngle(pos):
    sX = theball.x
    sY = theball.y
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle = math.pi / 2

    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle

    return angle


radius = 35
ground = 499 - radius

theball = ball(300, ground, radius, (255, 255, 255))

run = True
time = 0
power = 0
angle = 0
shoot = False
clock = pygame.time.Clock()

while run:
    clock.tick(200)
    if shoot:
        if theball.y < 500 - theball.radius:
            time += 0.05
            po = ball.ballPath(x, y, power, angle, time)
            theball.x = po[0]
            theball.y = po[1]
        else:
            shoot = False
            time = 0
            theball.y = ground

    line = [(theball.x, theball.y), pygame.mouse.get_pos()]
    redrawWindow()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not shoot:
                x = theball.x
                y = theball.y
                pos = pygame.mouse.get_pos()
                shoot = True
                power = math.sqrt((line[1][1] - line[0][1]) ** 2 + (
                        line[1][0] - line[0][1]) ** 2) / 8
                angle = findAngle(pos)

pygame.quit()
quit()
