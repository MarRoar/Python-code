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

class MainGame:
    '''主游戏界面'''
    def __init__(self):
        pass
    def startGame(self):
        pygame.display.init()
        pygame.display.set_mode((800, 500))
        pygame.display.set_caption("坦克大战v1.00")
        while True:
            self.getEvent()
            pygame.display.update()

    def endGame(self):
        exit()

    def getEvent(self):
        eventLists = pygame.event.get()
        for event in eventLists:
            eType = event.type

            if event.type == pygame.QUIT:
                self.endGame()
            if event.type == pygame.KEYDOWN:
                # 下面应该是 event.key 具体按的哪一个键
                if event.key == pygame.K_LEFT:
                    print("left")
                elif(event.key == pygame.K_RIGHT):
                    print("right")
                elif(event.key == pygame.K_UP):
                    print("up")
                elif(event.key == pygame.K_DOWN):
                    print("down")

class Tank:
    pass
class Wall:
    pass
class Bullet:
    pass

game = MainGame()
game.startGame()
