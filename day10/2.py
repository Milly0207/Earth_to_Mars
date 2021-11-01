'''
定义一个空调类和对应的测试类
要求：
    1、空调有品牌和价格两个属性，并且将属性私有化，提供公有的getXxx与setXxx方法对属性赋值和取值；
    2、提供一个无返回值的无参数的开机的方法，内容打印一句话：“空调开机了...”；
    3、提供一个无返回值的带1个int类型参数的定时关机的方法,(int类型的参数表示设定的分钟数)，内容打印一句话：“空调将在xxx分钟后自动关闭...”；
    4、在测试类中创建出空调对象，并给空调的品牌和价格赋任意值；
    5、使用空调对象获取空调的品牌和价格并打印到控制台上；
    6、使用空调对象调用开机方法；
    7、使用空调对象调用定时关机方法，并传递具体数据值，在控制台上可以看到的效果为：空调将在xxx分钟后自动关闭...
    其中语句中的“xxx”是调用方法时传递的具体数据值；
'''

class air_conditioner:
    __brand = ""
    __price = ""

    def setBrand(self, brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand

    def setPrice(self, price):
        self.__price = price
    def getPrice(self):
        return self.__price

    def boot_up(self):
        print("空调开机了...")

    def boot_down(self, min):
        print("空调将在", min, "分钟后自动关闭...")

    def intr(self):
        print("品牌:", a.getBrand())
        print("价格:", a.getPrice(), "元")

a = air_conditioner()
a.setBrand("美的")
a.setPrice(4000)

a.intr()
a.boot_up()
a.boot_down(1)


print()
'''
该题考查点：self关键字的使用！
定义一个学生类和对应的测试类
要求：
    1、学生有姓名和年龄两个属性，并且将属性私有化，提供公有的getXxx与setXxx方法对属性赋值和取值；
    2、提供一个无返回值的无参数的自我介绍的方法，内容打印一句话：
    “大家好，我叫xxx，今年xxx岁了！”
    3、提供一个返回值为String类型，参数为学生类型的比较年龄差值的方法，如果当前对象的年龄比参数中的学生的年龄大，则返回：“我比同桌大xxx岁！”；如果当前对象的年龄比参数中的学生的年龄小，则返回：“我比同桌小xxx岁！”；如果当前对象的年龄和参数中的学生的年龄一样大，则返回：“我和同桌一样大！”
    4、在测试类中分别创建你和你同桌两个人的对象，并分别给你和你同桌的姓名和年龄属性赋上对应的值；
    5、调用你自己的对象的自我介绍的方法，展示出你自己的姓名和年龄；
    6、用你自己的对象调用比较年龄差值的方法，把你同桌作为参数使用，并打印方法返回的字符串的内容；
'''
class student:
    __name = ""
    __age = 0

    def setName(self, name):
        if name == "":
            print("用户名不能为空！别瞎弄！")
        else:
           self. __name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        if age < 0 or age > 120:
            print("年龄非法！别瞎弄！")
        else:
            self.__age = age

    def getAge(self):
        return self.__age

    def intr(self):
        print("大家好，我叫", self.__name, "今年", self.__age, "岁了!")

    def age_dif(self, age2):
        if self.__age > age2:
            dif = self.__age - age2
            print("我比同桌大", dif, "岁！")
        elif self.__age < age2:
            dif = age2 - self.__age
            print("我比同桌小", dif, "岁！")
        else:
            print("我和同桌一样大！")

stu = student()

stu.setName("小华")
stu.setAge(5)
stu.intr()

stu2 = student()
stu2.setName("花花")
stu2.setAge(3)
stu.age_dif( stu2.getAge())
