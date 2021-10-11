# 7.编程实现下列图形的打印（7* 等边三角形）
print("")
print("---7、打印三角形---------------------")
for i in range(0,6):
    for j in range(0,6-i):
        print(" ",end="")
    for k in range(0,i+1):
        print("*",end=" ")
    print("")              # 换行


# 8.使用while循环实现NxN乘法表的打印。
print("")
print("---8、实现NxN乘法表的打印---------------------")
# while True:
n = input("请输入数字(查看NxN乘法表)：")
if n.isdigit():
    n = int(n)
    for i in range(n):
        for j in range(i+1):
            print(j+1,"x",i+1,"=",(j+1)*(i+1),end="   ")
        print("")
else:
    print("请输入一个整数！")

# 9.编程实现99乘法表的倒叙打印
print("")
print("---9、99乘法表的倒叙打印-------------------------")
for i in range(9):
    for j in range(9-i):
        print(j+1,"x",9-i,"=",(j+1)*(9-i),end="     ")
    print("")


# 10.一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
print("")
print("---10、青蛙掉在高20米的井里，白天上爬3米，晚上下滑2米，问第几天能出来？---------")
day = 0
height = -20
while height <= -1:
    day += 1
    height += 3 # 白天往上爬了3米
    height -= 2 # 晚上下滑了2米
    print("第", day, "天","爬到",height,"米")
print("它用了",day,"天才爬出来")


# 11.判断下列变量命名是否合法
# print("")
# print("=======================================")
# char = 1  # 合法
# print(char)
# Cy%ty = 1  # 非法!
# print(Cy%ty )
# Oax_li = 1  # 合法
# print()
# $123 = 2   # 非法!
# print($123)
# fLul = 3  # 合法
# print(fLul)
# 3_3 = 4   # 非法!
# print(3_3)
# BYTE = 5  # 合法
# print(BYTE)
# T_T = 6  # 合法
# print(T_T)


'''
12.继续完成上午的猜数字游戏的需求功能。
    添加计数打印功能
    添加次数金币功能和锁定系统功能。
'''
print("")
print("---12、猜数字游戏--------------------------")
import random
import time
randint = random.randint(1, 30)  # 随机产生的数字
gold = 5000
i = 1
print(randint)
while True:
    num=input("请输入一个数字：")
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
                        time.sleep(5)
                else:
                    print("猜小了,金币剩余", gold,"。 你还有",16-i,"次机会")
                    if (i-1)%3 != 0:
                        continue
                    else:
                        time.sleep(5)
        else:
            print("您已猜错15次，系统已锁定")
            exit()
    else:
        print("别瞎输入！")
        time.sleep(5)



# 13.用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
print("")
print("---13、求20以内的数的阶乘---------------------")
for i in range(21):
    result = i*(i-1)
    print(i,"的阶乘为",result)