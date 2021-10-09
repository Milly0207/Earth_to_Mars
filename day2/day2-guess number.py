'''
猜字游戏
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
任务：猜3次就睡眠 time.sleep(10)
    起始：5000金币，每猜错一次，减去500金币，一直扣完为止。15次没猜中，系统锁定。猜中加3000。
'''
import random
import time
import os
randint = random.randint(1, 30)  # 随机产生的数字
gold = 5000
i = 1
while True:
    print(randint)
    num=input("请输入一个数字")
    if num.isdigit():
        num = int(num)
        i += 1
        if i <= 15:
            if num == randint:
                gold += 3000
                print("OK，金币+3000,剩余",gold,"。你只用了",i-1,"次就猜对了！")
                break
            elif num > randint:
                if gold > 0:
                    gold -= 500
                    print("猜大了,金币-500，剩余", gold,"。 你还有",16-i,"次机会")
                    if (i-1)%3 != 0:
                        continue
                    else:
                        time.sleep(5)
                else:
                    print("猜大了,金币",gold,"。 你还有",16-i,"次机会")
                    if (i-1)%3 != 0:
                        continue
                    else:
                        time.sleep(5)
            elif num < randint:
                if gold > 0:
                    gold -= 500
                    print("猜小了,金币-500，剩余", gold,"。 你还有",16-i,"次机会")
                    if (i-1)%3 != 0:
                        continue
                    else:
                        time.sleep(10)
                else:
                    print("猜小了,金币剩余", gold,"。 你还有",16-i,"次机会")
                    if (i-1)%3 != 0:
                        continue
                    else:
                        time.sleep(5)
        else:
            print("您已猜错15次，将退出系统")
            exit()
    else:
        print("别瞎输入！")
        time.sleep(5)
