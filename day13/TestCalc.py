from unittest import TestCase
from  Calc import Calc

# 只是测试用例
class TestCalc(TestCase):

    def testAdd1(self):
        # 造数据
        a = -6
        b = 5
        s = 11 # 期望结果

        # 调用加法方法，得到实际结果
        calc = Calc()
        sum = calc.add(a,b)

        # 判断实际结果与期望结果是否一致。
        self.assertEqual(s,sum)

    def testAdd2(self):
        # 造数据
        a = -6
        b = -5
        s = -11 # 期望结果

        # 调用加法方法，得到实际结果
        calc = Calc()
        sum = calc.add(a,b)

        # 判断实际结果与期望结果是否一致。
        self.assertEqual(s,sum)
    def testAdd3(self):
        # 造数据
        a = -6
        b = 5
        s = -1 # 期望结果

        # 调用加法方法，得到实际结果
        calc = Calc()
        sum = calc.add(a,b)

        # 判断实际结果与期望结果是否一致。
        self.assertEqual(s,sum)
    def testAdd4(self):
        # 造数据
        a = 6
        b = -5
        s = 1 # 期望结果

        # 调用加法方法，得到实际结果
        calc = Calc()
        sum = calc.add(a,b)

        # 判断实际结果与期望结果是否一致。
        self.assertEqual(s,sum)
