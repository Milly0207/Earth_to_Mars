'''
分析一个水杯的属性和功能，使用类描述并创建对象
    高度，容积，颜色，材质
    能存放液体
'''
class cap:
    height = 0
    volume = 0.0
    color = ""
    material = ""

    def store_liquid(self):
        print("能存放", volume, "升液体")

'''
有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），
行为（打字，打游戏，看视频）
'''
class laptop:
    screen_size = 0.0
    price = 0.00
    cpu = ""
    RAM = ""
    stanby_time = 5

    def typing(self):
        print("可以打字")

    def game(self):
        print("可以打游戏")

    def video(self):
        print("可以看视频")


'''
先构思面向对象版的中国工商银行系统
'''
class bank:


    def