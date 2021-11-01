class student:
    __no = 0
    __name = ""
    __age = 0
    __sex = ""
    __height = 0.0
    __weight = 0.0
    __score = 0
    __addr = ""
    __phone = 1

    def setNo(self,no):
        self.__no = no
    def getNo(self):
        return self.__no

    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age
    def getAge(self):
        return self.__age

    def setSex(self, sex):
        self.__sex = sex
    def getSex(self):
        return self.__sex

    def setHeight(self, height):
        self.__height = height
    def getHeight(self):
        return self.__height


    def learn(self, time):
        print(self.__name, "已经学习了", time, "小时了")
    def game(self, game):
        print(self.__name, "喜欢玩", game)
    def code(self,rows):
        print(self.__name, "代码写了", rows, "行")
    def sum(self, num1, num2):
        sum = num1 + num2
        print("求和结果:", sum)

student = student()
student.setName("小华")
student.game("蜘蛛纸牌")
student.learn(10)
student.code(3)
student.sum(1,2)

#------------------------------------------------------
class car:
    __model = ""
    __num = 0
    __color = ""
    __weight = 0.0
    __size = 0.0

    def setModel(self, model):
        self.__model = model
    def getModel(self):
        return self.__model

    def setNum(self, num):
        self.__num = num
    def getNum(self):
        return self.__num

    def setColor(self, color):
        self.__color = color
    def getColor(self):
        return self.__color

    def setWeight(self, weight):
        self.__weight = weight
    def getWeight(self):
        return self.__weight

    def setSize(self, size):
        self.__size = size
    def getSize(self):
        return self.__size

    def run(self):
        print(self.__model, "可以跑")

car1 = car()
car1.setModel("法拉利")
car1.setColor("red")
car1.setNum(4)
car1.setWeight(10000)
car1.setSize(2.6)
car1.run()

car2 = car()
car2.setModel("宝马")
car2.setColor("white")
car2.setNum(4)
car2.setWeight(10000)
car2.setSize(2.6)
car2.run()

#------------------------------------------------------
class laptop:
    __model = ""
    __time = 0.0
    __color = ""
    __weight = 0.0
    __cpu = ""
    __ram = ""
    __disk = ""

    def setModel(self, model):
        self.__model = model
    def getModel(self):
        return self.__model

    def setTime(self, time):
        self.__time = time
    def getTime(self):
        return self.__time

    def setColor(self, color):
        self.__color = color
    def getColor(self):
        return self.__color

    def setWeight(self, weight):
        self.__weight = weight
    def getWeight(self):
        return self.__weight

    def setCpu(self, cpu):
        self.__cpu = cpu
    def getCpu(self):
        return self.__cpu

    def setRam(self, ram):
        self.__ram = ram
    def getRam(self):
        return self.__ram

    def setDisk(self, disk):
        self.__disk = disk

    def getDisk(self):
        return self.__disk

    def game(self, game):
        print(self.__model, "可以打游戏", game)

    def office(self):
        print("可以办公")

laptop = laptop()
laptop.setModel("华硕 U4000")
laptop.setColor("灰色")
laptop.game("扫雷")



#------------------------------------------------------
class monkey:
    __type = ""
    __sex = ""
    __color = ""
    __weight = 0.0

    def setType(self, type):
        self.__type = type
    def getType(self):
        return self.__type

    def setSex(self, sex):
        self.__sex = sex
    def getSex(self):
        return self__sex

    def setColor(self, color):
        self.__color = color
    def getColor(self):
        return self.__color

    def setWeight(self, weight):
        self.__weight = weight
    def getWeight(self):
        return self.__weight

    def make_fire(self, tool):
        print(self.__type, "可以使用", tool, "来造火")

    def learn(self, what):
        print(self.__type, "可以学习", what)

monkey1 = monkey()
monkey1.setType("金丝猴")
monkey1.setColor("棕色")
monkey1.setSex("母")
monkey1.setWeight("80")
monkey1.make_fire("石头")
monkey1.learn(what='骑车、'+'唱歌')