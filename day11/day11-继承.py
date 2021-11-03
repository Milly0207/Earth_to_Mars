'''
按要求定义类
考查知识点：super关键字的使用和继承中方法的调用
要求：
    1、定义老手机类，有品牌属性，且属性私有化，提供相应的getXxx与setXxx方法，
       提供无返回值的带一个Str类型参数的打电话的方法，内容为：“正在给xxx打电话...”
    2、定义新手机类，继承老手机类，重写父类的打电话的方法，
       内容为2句话：“语音拨号中...”、“正在给xxx打电话...”
       要求打印“正在给xxx打电话...”这一句调用父类的方法实现，不能在子类的方法中直接打印；
       提供无返回值的无参数的手机介绍的方法，内容为：“品牌为：xxx的手机很好用...”
    3、定义测试类，创建新手机对象，并使用该对象，对父类中的品牌属性赋值；
    4、使用新手机对象调用手机介绍的方法；
    5、使用新手机对象调用打电话的方法；
'''
import time
class OldPhone:
    __brand = ""

    def setBrand(self, brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand

    def call(self, phoneNum):
        print("正在给", phoneNum, "打电话")
        for i in range(8):
            print(".", end="")
            time.sleep(0.25)
        print("\n已接通")

class NewPhone(OldPhone):
    def call(self,phoneNum):
        print("语音拨号中...")
        super().call(phoneNum)

    def intro(self):
        print(super().getBrand(), "牌子的手机真好用")

p = NewPhone()
p.setBrand("华为")
p.call("110")
p.intro()


'''
考查知识点：继承的传递性
按要求定义类
要求：
    1、定义厨师类，有姓名和年龄的属性，且属性私有化，
       提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
    2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
    3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
    4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，
       对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
    5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法；
'''
print()
class Chef:
    __name = ""
    __age = None

    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self, age):
        if age.isdigit():
            self.__age = age
        else:
            print("请输入正确的年龄!")
    def getAge(self):
        return self.__age

    def cook_rice(self):
        pass

class Chef1(Chef):
    def cook_fry(self):
        pass

class Chef2(Chef1):
    def cook_rice(self):
        print(" 会蒸饭", end="")

    def cook_fry(self):
        print(" 会炒菜", end="")

c = Chef2()
c.setName("华厨神")
c.setAge('31')
print(c.getName(), c.getAge(), "岁，", end="")
c.cook_rice()
c.cook_fry()



'''
1、人：年龄，性别，姓名。
2、现在有个工种：工人，
    属性：年龄，性别，姓名 。
    行为：干活。
    请用继承的角度来实现该类。
3、现在有个工种: 学生，
    属性：年龄，性别，姓名，学号。
    行为：学习，唱歌。
请结合上面的几个题目用继承的角度来实现。
'''
print("\n")
class Human:
    __name = ""
    __age = None
    __sex = ""

    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self, age):
        if age.isdigit():
            self.__age = age
        else:
            print("请输入正确的年龄!")
    def getAge(self):
        return self.__age

    def setSex(self, sex):
        if sex == "男" or sex == "女":
            self.__sex = sex
        else:
            print("请输入正确的性别！")
    def getSex(self):
        return self.__sex

class Worker(Human):
    def work(self, job):
        print(self.getName(), "是工人，要", job)

class Student(Human):
    __stuNo = 0

    def setStuno(self, stuNo):
        self.__stuNo = stuNo
    def getStuno(self):
        return self.__stuNo

    def study(self, course):
        print(self.getAge(), "岁的", self.getName(), "是学生，要学习", course)

    def sing(self, song):
        print(self.getAge(), "岁的", self.getName(), "是学生，会唱", song)

person1 = Worker()
person1.setName("绒绒")
person1.setAge("5")
person1.setSex("男")
person1.work("搬砖")

person2 = Student()
person2.setName("小华")
person2.setAge("2")
person2.setSex("男")
person2.setStuno('001')
person2.study("乐理")
person2.sing("斗牛")




