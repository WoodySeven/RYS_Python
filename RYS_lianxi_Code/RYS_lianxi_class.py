#!/usr/bin/env python


class Robot(object):
    """表示有一个带有名字的机器人。"""
    #一个类变量，用来计数机器人的数量
    population = 0
    h_status = 0
    def __init__(self,name,date):
        """初始化数据,z主要实现"""
        self.name = name
        self.date = date
        print ("初始化{0},年龄{1}".format(self.name,self.date))
        Robot.population +=1
    def die(self):
        print("{0}挂掉了".format(self.name))
        Robot.population -=1
        if Robot.population == 0 :
            print("{0}是最后一个机器人了,生产日期{1}".format(self.name,self.date))
        elif Robot.population > 0:
            print("现在还存在机器人个数为{}".format(Robot.population))
        else:
            print("计数错误")
            return

    def say(self,n):

        self.n = n
        if n == 0 :
            print("good moring")
        elif n == 1:
            print("上午好")
        else:
            print("下午好")

    def food(self):
        Robot.h_status = 1
        print("我以吃饱")

    def walk(self):
        if self.h_status == 0:
            print("我饿了没力气，快喂我吃东西吧")
        else:
            print("走吧，我们去散步吧")

    @classmethod
    def how_many(cls):
        pass



if __name__=="__main__":

    yadang = Robot("yadang",17)
    yadang.say(2)
    yadang.walk()
    yadang.die()
    yadang.die()

