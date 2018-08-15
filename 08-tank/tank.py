'''
    坦克游戏
    游戏分析
    1、游戏主界面
    2、坦克
        1/ 移动
        2/ 发射
    3、障碍物
    4、炮弹
    5、爆炸效果
'''
import pygame

_display = pygame.display

COLOR_BLACK = pygame.Color(0, 0, 0, 1)
COLOR_RED = pygame.Color(255, 0, 0, 1)

class MainGame:
    '''主游戏界面'''
    mainWindow = None

    # 创建我方坦克
    TANK_P1 = None
    ENEMY_TANKS = []

    def __init__(self):
        pass
    def startGame(self):
        _display.init()
        MainGame.mainWindow = _display.set_mode((800, 500))
        _display.set_caption("坦克大战v1.00")
        MainGame.TANK_P1 = MyTank(400, 300)
        while True:
            MainGame.mainWindow.fill(COLOR_BLACK)
            MainGame.mainWindow.blit(self.getTextSurface("剩余敌方坦克 %d 量"%(len(MainGame.ENEMY_TANKS))), (10, 10))

            MainGame.TANK_P1.dispalyTank()
            self.getEvent()
            _display.update()

    def endGame(self):
        exit()

    def getEvent(self):
        # pygame.key.set_repeat(273, 10)
        eventLists = pygame.event.get()
        for event in eventLists:
            if event.type == pygame.QUIT:
                self.endGame()
            if event.type == pygame.KEYDOWN:
                # 下面应该是 event.key 具体按的哪一个键
                # print(event.key)
                if event.key == pygame.K_LEFT:
                    print("left")
                    MainGame.TANK_P1.direction = "L"
                    MainGame.TANK_P1.move()
                elif(event.key == pygame.K_RIGHT):
                    print("right")
                    MainGame.TANK_P1.direction = "R"
                    MainGame.TANK_P1.move()
                elif(event.key == pygame.K_UP):
                    print("up")
                    MainGame.TANK_P1.direction = "U"
                    MainGame.TANK_P1.move()
                elif(event.key == pygame.K_DOWN):
                    print("down")
                    MainGame.TANK_P1.direction = "D"
                    MainGame.TANK_P1.move()
                elif(event.key == pygame.K_SPACE):
                    print("发射..")
                    MainGame.TANK_P1.shot()

    def getTextSurface(self, text):
        '''设置字体，显示敌方坦克的数量'''
        pygame.font.init()
        font = pygame.font.SysFont("kaiti", 16)
        textSurface = font.render(text, True, COLOR_RED)
        return textSurface

class Tank:

    def __init__(self, left, top):
        self.images = {
            "U": pygame.image.load("./img/p1tankU.gif"),
            "D": pygame.image.load("./img/p1tankD.gif"),
            "L": pygame.image.load("./img/p1tankL.gif"),
            "R": pygame.image.load("./img/p1tankR.gif")
        }
        self.direction = 'U'  # 方向
        self.image = self.images[self.direction]  # 当前的坦克的图片
        self.left = left
        self.top = top
        self.speed = 5
        self.bullet_lists = []

    def move(self):
        direction = self.direction
        if direction == 'U':
            self.top -= self.speed
        elif direction == 'D':
            self.top += self.speed
        elif direction == 'L':
            self.left -= self.speed
        elif direction == 'R':
            self.left += self.speed

    def shot(self):
        self.bullet_lists.append(Bullet(self.direction, self.left, self.top))
    def dispalyTank(self):
        self.image = self.images[self.direction]
        MainGame.mainWindow.blit(self.image, (self.left, self.top))

        for bullet in self.bullet_lists:
            bullet.display()
            bullet.move()

class MyTank(Tank):

    def __init__(self, left, top):
        self.images = {
            "U": pygame.image.load("./img/p1tankU.gif"),
            "D": pygame.image.load("./img/p1tankD.gif"),
            "L": pygame.image.load("./img/p1tankL.gif"),
            "R": pygame.image.load("./img/p1tankR.gif")
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        super().__init__(left, top)

class EnemyTank(Tank):

    def __init__(self, left, top):
        self.images = {
            "U": pygame.image.load("./img/enemy1U.giff"),
            "D": pygame.image.load("./img/enemy1D.gif"),
            "L": pygame.image.load("./img/enemy1L.gif"),
            "R": pygame.image.load("./img/enemy1R.gif")
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        super().__init__(left, top)

class Wall:
    pass
class Bullet:

    def __init__(self, direction, left, top):
        self.image = pygame.image.load("./img/tankmissile.gif")
        self.direction = direction
        self.left = left + 20
        self.top = top + 20
        self.speed = 2

    def display(self):
        MainGame.mainWindow.blit(self.image, (self.left, self.top))
    def move(self):
        if self.direction == 'U':
            self.top -= self.speed
        elif self.direction == 'D':
            self.top += self.speed
        elif self.direction == 'L':
            self.left -= self.speed
        elif self.direction == 'R':
            self.left += self.speed
    def remove(self):
        pass

game = MainGame()
game.startGame()
