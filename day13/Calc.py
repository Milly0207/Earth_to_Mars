'''
    单元测试框架：unittest
    1.子类继承TestCase
    2.写测试用例，testXxxx

'''

class Calc:
    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def multi(self, a, b):
        return a * b

    def devision(self, a, b):
        return a / b


# # 造数据
# a = 6
# b = 5
# s = 11 # 期望结果
#
# # 调用加法方法，得到实际结果
# calc = Calc()
# sum = calc.add(a,b)
#
# # 判断实际结果与期望结果是否一致。
# if sum  == s :
#     print("用例通过！")
# else:
#     print("用例不通过!")
























