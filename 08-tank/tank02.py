'''
坦克大战
坦克大战第一版结束
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
    Enemy_Tanks = pygame.sprite.Group()
    explode_list = []
    wall = None

    def __init__(self):
        pass

    def start(self):
        _display.init()
        MainGame.screen = _display.set_mode((MainGame.width, MainGame.height), 0, 0)
        _display.set_caption("坦克大战v1.00")
        MainGame.My_Tank = MyTank()

        for i in range(1, 5):
            MainGame.Enemy_Tanks.add(EnemyTank())

        MainGame.wall = Wall(50, 300, 360, 70)

        while True:
            MainGame.screen.fill(COLOR_BLACK)
            self.getEvent()
            if MainGame.My_Tank.live:
                MainGame.My_Tank.dispalyTank()
                MainGame.My_Tank.hitEnemy()
            else:
                self.setGameOverText()

            for E_Tank in MainGame.Enemy_Tanks:
                E_Tank.displayTank()

            # 显示左上角的文字
            for i, item  in enumerate(self.setText(),1):
                self.screen.blit(item, (5, i*15 + 5))

            for e in MainGame.explode_list:
                e.displayExplode()

             # 展示墙
            MainGame.wall.displayWall()
            MainGame.wall.hitOther()

            _display.update()
            time.sleep(0.05)

    def end(self):
        sys.exit()
    def getEvent(self):
        event_lists = pygame.event.get()
        for event in event_lists:
            if event.type == pygame.QUIT:
                self.end()
            if event.type == pygame.KEYDOWN and not MainGame.My_Tank.live:
                if event.key == pygame.K_n:
                    MainGame.My_Tank.live = True

            if event.type == pygame.KEYDOWN and MainGame.My_Tank.live:
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

    def setText(self):
        pygame.font.init()
        font = pygame.font.SysFont("kaiti", 16)
        text_surface01 = font.render("敌方坦克的数量%d"%(len(MainGame.Enemy_Tanks)), True, COLOR_RED)
        text_surface02 = font.render("我方坦克炮弹的数量%d"%(len(MyTank.bullet_list)), True, COLOR_RED)
        return text_surface01, text_surface02

    def setGameOverText(self):
        pygame.font.init()
        font = pygame.font.SysFont("kaiti", 30)
        text_surface01 = font.render("游戏结束，按n键复活", True, COLOR_RED)
        MainGame.screen.blit(text_surface01, (400, 400))

class Tank(pygame.sprite.Sprite):

    def displayTank(self):
        pygame.sprite.Sprite.__init__(self)

class MyTank(Tank):

    width = 50
    height = 50
    bullet_list = []

    def __init__(self):
        super().__init__()
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
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top

    def dispalyTank(self):
        self.image = self.images[self.direction]
        MainGame.screen.blit(self.image, self.rect)
        self.move()

        # 显示我方炮弹
        for bullet in MyTank.bullet_list:
            if bullet.live:
                bullet.displayBullet()
                bullet.move()
                bullet.hitTank()
            else:
                MyTank.bullet_list.remove(bullet)

    def stay(self):
        self.rect.left = self.oldLeft
        self.rect.top = self.oldTop

    def move(self):
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
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
        b = Bullet(self)
        b.good = True
        MyTank.bullet_list.append(b)

    def hitEnemy(self):
        hit_list = pygame.sprite.spritecollide(self, EnemyTank.bullet_list, False)
        for m in hit_list:
            self.live = False
            EnemyTank.bullet_list.remove(m)
            m.live = False
            explode = Explode(self)
            MainGame.explode_list.append(explode)

class EnemyTank(Tank):

    width = 50
    height = 50
    bullet_list = pygame.sprite.Group()
    str_direction = 'UDLR'

    def __init__(self):
        super().__init__()
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
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top

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

        if self.live:
            self.random_fire()
            for bullet in EnemyTank.bullet_list:
                if bullet.live:
                    bullet.displayBullet()
                    bullet.move()
                else:
                    EnemyTank.bullet_list.remove(bullet)

    def stay(self):
        self.rect.left = self.oldLeft
        self.rect.top = self.oldTop

    def move(self):
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top

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

    def random_fire(self):
        r = randint(0, 50)
        if r == 10 or r == 20 or r == 30:
            EnemyTank.bullet_list.add(Bullet(self))

class Bullet(pygame.sprite.Sprite):

    def __init__(self, tank):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./img/tankmissile.gif")
        self.rect = self.image.get_rect()
        self.rect.left = tank.rect.left + 20
        self.rect.top = tank.rect.top + 20
        self.direction = tank.direction
        self.speed = 20
        self.live = True
        self.stop = False
        self.good = False

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

    def hitTank(self):
        if self.good:
            hit_list = pygame.sprite.spritecollide(self, MainGame.Enemy_Tanks, False)
            for e in hit_list:
                e.live = False
                MainGame.Enemy_Tanks.remove(e) # 删除 击中的敌方坦克坦克
                self.live = False
                explode = Explode(e)
                MainGame.explode_list.append(explode)

class Explode:

    def __init__(self, tank):
        self.live = True
        self.images = [pygame.image.load("./img/blast0.gif"),\
                       pygame.image.load("./img/blast1.gif"),\
                       pygame.image.load("./img/blast2.gif"),\
                       pygame.image.load("./img/blast3.gif"),\
                       pygame.image.load("./img/blast4.gif"),\
                       pygame.image.load("./img/blast5.gif"),\
                       pygame.image.load("./img/blast6.gif"),\
                       pygame.image.load("./img/blast7.gif"),\
                       ]
        self.step = 0
        self.rect = tank.rect

    def displayExplode(self):
        if self.live:
            if self.step == len(self.images):
                self.live = False
            else:
                self.image = self.images[self.step]
                MainGame.screen.blit(self.image, self.rect)
                self.step += 1
        else:
            return

class Wall(pygame.sprite.Sprite):

    def __init__(self, left, top, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(left, top, width, height)

    def displayWall(self):
        pygame.draw.rect(MainGame.screen, COLOR_RED, self.rect, 2)

    def hitOther(self):
        isHit = pygame.sprite.collide_rect(self, MainGame.My_Tank)
        if isHit:
            # MainGame.My_Tank.stop = True
            MainGame.My_Tank.stay()
        hit_enemy_list = pygame.sprite.spritecollide(self, MainGame.Enemy_Tanks, False)
        for e in hit_enemy_list:
            e.stay()

if __name__ == "__main__":
    game = MainGame()
    game.start()