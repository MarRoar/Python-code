'''
定义发动机类 Motor、底盘类 Chassis、座椅类 Seat，车辆外壳类 Shell，并使用组合
关系定义汽车类。其他要求如下：

定义汽车的 run()方法，里面需要调用 Motor 类的 work()方法，也需要调用座椅
类 Seat 的 work()方法，也需要调用底盘类 Chassis 的 work()方法。
'''

class Motor:
    '''发动机'''
    def work(self):
        print("发动机就位...")

class Chassis:
    '''底盘'''
    def work(self):
        print("底盘就位...")

class Seat:
    '''椅子'''
    def work(self):
        print("椅子就位...")

class Shell:
    '''外壳'''
    def work(self):
        print("外壳就位...")

class Car:
    '''汽车'''
    def __init__(self, motor, chassis, seat, shell):
        self.motor = motor
        self.chassis = chassis
        self.seat = seat
        self.shell = shell

    def run(self):
        self.motor.work()
        self.chassis.work()
        self.seat.work()

motor = Motor()
chassis = Chassis()
seat = Seat()
shell = Shell()

c = Car(motor, chassis, seat, shell)
c.run()
