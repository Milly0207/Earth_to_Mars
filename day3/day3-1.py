# # 1.实现输入10个数字，并打印10个数的求和结果
print("")
print("---1、输入10个数字，计算求和结果-----------------------")
i = 0
result = 0
while i <= 9:
    num = input("请输入一个数：")
    if num.isalpha():
        print("输入格式错误！请重新输入")
    else:
        num = float(num)
        result = result + num
        i += 1
print("求和结果为：",result)


#  2.从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
print("")
print("---2、输入10个数，计算求和结果、最大值及平均数---------------------")
list = []
i = 0
while i <= 9:
    num1 = input("请输入一个数：")
    if num1.isalpha() :
        print("输入格式错误！请重新输入")
    else:
        num1 = float(num1)
        list.append(num1)
        i += 1
print("你输入的10个数是：",list)
print("最大的数是",max(list))
print("10个数之和是",sum(list))
print("10个数平均数是",sum(list)/len(list))


# 3.使用random模块，如何产生 50~150之间的数？
print("")
print("---3、生成50~150之间的随机数----------------------------")
import random
num2 = random.randint(50,150)
print(num2)

# 4.从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
print("")
print("---4、输入任意三边，判断三角形----------------------------")
while True:
    side1 = input("请输入第1条边：")
    side2 = input("请输入第2条边：")
    side3 = input("请输入第3条边：")
    if side1.isalpha() or side2.isalpha() or side3.isalpha():
        print("输入格式错误")
    else:
        if side3.isalpha():
            print("输入格式错误")
        else:
            side1 = float(side1)
            side2 = float(side2)
            side3 = float(side3)
            if side1+side2>side3 or side1+side3>side2 or side2+side3>side1 :
                if side1 == side2 == side3:
                    print("等边三角形")
                elif side1==side2 or side2==side3 or side1==side3:
                    print("等腰三角形")
                elif side1**2 == side2**2+side3**2 or side2**2==side1**2+side3**2 or side3**2==side2**2+side1**2 :
                    print("直角三角形")
                else:
                    print("普通三角形")
            else:
                print("不能构成三角形")
    print("还要继续吗？按N退出，按其他键继续")
    yesno = input("请输入:")
    if yesno == "N" or yesno == "n":
        exit()





