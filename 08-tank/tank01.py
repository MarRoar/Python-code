'''
坦克大战
'''
import pygame, sys
import time
from random import randint

COLOR_RED = pygame.Color(255, 0, 0)
COLOR_BLACK = pygame.Color(0, 0, 0)
_display = pygame.display

class MainGame:

    screen = None
    width = 1000
    height = 800
    My_Tank = None
    Enemy_Tanks = []

    def __init__(self):
        pass

    def start(self):
        _display.init()
        MainGame.screen = _display.set_mode((MainGame.width, MainGame.height), 0, 0)
        _display.set_caption("坦克大战v1.00")
        MainGame.My_Tank = MyTank()

        for i in range(1, 5):
            MainGame.Enemy_Tanks.append(EnemyTank())

        while True:
            MainGame.screen.fill(COLOR_BLACK)
            self.getEvent()

            MainGame.My_Tank.dispalyTank()

            for E_Tank in MainGame.Enemy_Tanks:
                E_Tank.displayTank()

            _display.update()

            time.sleep(0.05)

    def end(self):
        sys.exit()
    def getEvent(self):
        event_lists = pygame.event.get()
        for event in event_lists:
            if event.type == pygame.QUIT:
                self.end()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    MainGame.My_Tank.direction = 'L'
                    MainGame.My_Tank.stop = False
                elif(event.key == pygame.K_RIGHT):
                    MainGame.My_Tank.direction = 'R'
                    MainGame.My_Tank.stop = False
                elif(event.key == pygame.K_UP):
                    MainGame.My_Tank.direction = 'U'
                    MainGame.My_Tank.stop = False
                elif(event.key == pygame.K_DOWN):
                    MainGame.My_Tank.direction = 'D'
                    MainGame.My_Tank.stop = False
                elif(event.key == pygame.K_SPACE):
                    MainGame.My_Tank.fire()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    MainGame.My_Tank.stop = True
class Tank:

    def displayTank(self):
        pass

    def move(self):
        pass

class MyTank(Tank):

    width = 50
    height = 50
    bullet_list = []

    def __init__(self):
        self.width = MyTank.width
        self.height = MyTank.height
        self.images = {
            "U": pygame.image.load("./img/p1tankU.gif"),
            "D": pygame.image.load("./img/p1tankD.gif"),
            "L": pygame.image.load("./img/p1tankL.gif"),
            "R": pygame.image.load("./img/p1tankR.gif")
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = 400
        self.rect.top = 400
        self.live = True
        self.speed = 5
        self.stop = True

    def dispalyTank(self):
        self.image = self.images[self.direction]
        MainGame.screen.blit(self.image, self.rect)
        self.move()
        for bullet in MyTank.bullet_list:
            if bullet.live:
                bullet.displayBullet()
                bullet.move()
            else:
                MyTank.bullet_list.remove(bullet)

    def move(self):
        if not self.stop:
            if self.direction == 'L':
                if self.rect.left > 0:
                    self.rect.left -= self.speed
                else:
                    self.rect.left = 0

            elif self.direction == 'R':
                if self.rect.left < MainGame.width - self.width:
                    self.rect.left += self.speed
                else:
                    self.rect.left = MainGame.width - self.width

            elif self.direction == 'U':
                if self.rect.top > 0:
                    self.rect.top -= self.speed
                else:
                    self.rect.top = 0

            elif self.direction == 'D':
                if self.rect.top < MainGame.height - self.height:
                    self.rect.top += self.speed
                else:
                    self.rect.top = MainGame.height - self.height

    def fire(self):
        MyTank.bullet_list.append(Bullet(self))

class EnemyTank(Tank):

    width = 50
    height = 50
    bullet_list = []
    str_direction = 'UDLR'

    def __init__(self):
        self.width = EnemyTank.width
        self.height = EnemyTank.height
        self.images = {
            "U": pygame.image.load("./img/enemy2U.gif"),
            "D": pygame.image.load("./img/enemy2D.gif"),
            "L": pygame.image.load("./img/enemy2L.gif"),
            "R": pygame.image.load("./img/enemy2R.gif")
        }
        r = randint(0, 3)
        self.direction = EnemyTank.str_direction[r]
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = randint(0, 5) * 100
        self.rect.top = 100
        self.live = True
        self.stop = False
        self.speed = 10
        self.step = 6

    def get_random_direction(self):
        r = randint(0, 4)
        if r == 4:
            self.stop = True
        elif r == 1:
            self.direction = 'L'
            self.stop = False
        elif r == 0:
            self.direction = 'D'
            self.stop = False
        elif r == 2:
            self.direction = 'U'
            self.stop = False
        elif r == 3:
            self.direction = "R"
            self.stop = False

    def displayTank(self):
        self.image = self.images[self.direction]
        MainGame.screen.blit(self.image, self.rect)
        self.random_move()

    def move(self):
        if not self.stop:
            if self.direction == 'L':
                if self.rect.left > 0:
                    self.rect.left -= self.speed
                else:
                    self.rect.left = 0

            elif self.direction == 'R':
                if self.rect.left < MainGame.width - self.width:
                    self.rect.left += self.speed
                else:
                    self.rect.left = MainGame.width - self.width

            elif self.direction == 'U':
                if self.rect.top > 0:
                    self.rect.top -= self.speed
                else:
                    self.rect.top = 0

            elif self.direction == 'D':
                if self.rect.top < MainGame.height - self.height:
                    self.rect.top += self.speed
                else:
                    self.rect.top = MainGame.height - self.height


    def random_move(self):
        if self.live:
            if self.step == 0:
                self.get_random_direction()
                self.step = 6
            else:
                self.move()
                self.step -= 1

class Bullet:

    def __init__(self, tank):
        self.image = pygame.image.load("./img/tankmissile.gif")
        self.rect = self.image.get_rect()
        self.rect.left = tank.rect.left + 20
        self.rect.top = tank.rect.top + 20
        self.direction = tank.direction
        self.speed = 20
        self.live = True
        self.stop = False

    def displayBullet(self):
        MainGame.screen.blit(self.image, self.rect)

    def move(self):
        if self.live:
            if self.direction == 'L':
                if self.rect.left > 0:
                    self.rect.left -= self.speed
                else:
                    self.live = False

            elif self.direction == 'R':
                if self.rect.left < MainGame.width:
                    self.rect.left += self.speed
                else:
                    self.live = False

            elif self.direction == 'U':
                if self.rect.top > 0:
                    self.rect.top -= self.speed
                else:
                    self.live = False

            elif self.direction == 'D':
                if self.rect.top < MainGame.height:
                    self.rect.top += self.speed
                else:
                    self.live = False


class Wall:
    pass


if __name__ == "__main__":
    game = MainGame()
    game.start()