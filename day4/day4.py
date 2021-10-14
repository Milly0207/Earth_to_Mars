'''
# 1.有下列人员数据库，请按要求实现
    1.统计每个人的平均薪资
    2.统计每个人的平均年龄
    3.公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
    4.统计公司男女人数
    5.每个部门的人数
'''
#    姓名    年龄  性别    编号  任职公司 薪资 部门编号
names = [
    ["曹操", "56", "男", "106", "IBM", 500,"50"],
    ["大乔", "19", "女", "230", "微软", 501,"60"],
    ["小乔", "19", "女", "210", "Oracle",600,"60"],
    ["许褚", "45", "男", "230", "Tencent",700,"10"] ]
male = 0
female = 0
sum_salery = 0
sum_age = 0
for i in range(len(names)):
    # 1、求工资总和：
    sum_salery = sum_salery + names[i][5]
    # 2、求年龄总和：
    sum_age = sum_age + int(names[i][1])
    # 4、求男女人数：
    if names[i][2] == "男": male += 1
    elif names[i][2] == "女": female += 1
print("-------------------------")
print("平均工资：",sum_salery / (len(names)))
print("-------------------------")
print("平均年龄：",sum_age / (len(names)))
print("-------------------------")
print("男性员工人数：",male)
print("女性员工人数：", female)
print("-------------------------")
# 5、求各部门人数：
dept = []
for i in range(len(names)):
    dept.append(names[i][6])
# print(dept)
num = {}
for k in range(len(dept)):
    num[dept[k]] = dept.count(dept[k])
# print(num)
for a,b in num.items():
    print("部门编号为",a,"的人数：",b)
print("-------------------------")
# 3、新增员工：
new = ["刘备","45","男","220","alibaba",500,"30"]
names.append(new)
print(names)


print("")
print("=========================================")
print("")
# 2.现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。
# 但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
# 求每个人的总成绩？
a =[
    ["罗恩", 23, 35, 44],
    ["哈利", 60, 77, 68, 88, 90],
    ["赫敏", 97, 99, 89, 91, 95, 90],
    ["马尔福", 100, 85, 90]
]
score = 0
for i in range(len(a)):
    print(a[i][0],"的总成绩是",end="")
    for j in range(1,len(a[i])):
        score = score + a[i][j]
    print(score)
    score = 0

# 3.阅读程序并回答问题
# num = int(input("请输入一个数："))
# while num != 0:
#     print(num % 10)  # % 取余
#     num = num // 10  # // 取整
# # 当输入的是54321时，执行结果是？
'''
执行结果：
    1
    2
    3
    4
    5
'''
print("")
print("=========================================")
print("")
# 4.请对下列列表进行冒泡排序（网易测试开发笔试题）
'''
    冒泡排序的特点：
    1.如果有 N 个数，则要进行 N - 1 轮排序；
    2.在第 i 轮排序中，要进行 N-i 次两两比较
    3.可以从前往后排序，也可从后往前排序
'''
a = [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3]
lun = 0
for i in range(len(a)-1):
    lun += 1
    print("第",lun,"轮排序")
    for i in range(len(a)-lun):
        i += 1
        # print(a[i - 1], a[i])
        if a[i] < a[i-1]:
            a[i-1],a[i] = a[i],a[i-1] # 方法一
            # a.insert(i-1,a.pop(i))  # 方法二
        print(a)