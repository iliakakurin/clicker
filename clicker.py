# здесь подключаются модули
import pygame
import sys

# здесь определяются константы,
# классы и функции
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

# здесь происходит инициация,
# создание объектов
pygame.init()
sc = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# если надо до цикла отобразить
# какие-то объекты, обновляем экран

pygame.display.update()

# главный цикл
while True:

    # задержка
    clock.tick(FPS)


    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        print(i)

    # --------
    # изменение объектов
    # --------

    # обновление экрана
    sc.fill(WHITE)
    pygame.draw.circle(sc, YELLOW, (550, 350), 50)
    pygame.display.update()

# залить экран белым
# создавать кружки
# проверять нажатия на кружки

# создать 5 кружков случайного радиуса от 10 до 50
# случайные координаты центров от [0, 0] до [600, 400]
