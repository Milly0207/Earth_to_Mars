print("----------------------------")
dict = {"k1":"v1","k2":"v2","k3":"v3"}
for a,b in dict.items():
    print("key:",a)  # 1、请循环遍历出所有的key
    print("value:",b)  # 2、请循环遍历出所有的value
# 3、请在字典中增加一个键值对,"k4":"v4"
dict["k4"] = "v4"
print(dict)

print("----------------------------")
info = {}
info["苹果"] = "32.8"
info["香蕉"] = "22"
info["葡萄"] = "15.5"
print(info)

# 小明购买了苹果，草莓，香蕉.  小刚购买了葡萄，橘子，樱桃.
# 请从下面的描述的字典中，计算金额,并写入到money字段里.
# 以姓名做key，value仍然是字典
friuts = {
    "苹果": 12.3,  # 水果和单价
    "草莓": 4.5,
    "香蕉": 6.3,
    "葡萄": 5.8,
    "橘子": 6.4,
    "樱桃": 15.8
}
info = {
    '小明': {
        'fruits': {'苹果': 4, '草莓': 13, '香蕉': 10},
        'money': 1
    },
    '小刚': {
        'fruits': {'葡萄': 19, '橘子': 12, '樱桃': 30},
        'money': 2
    }
}
a = friuts['苹果']*info['小明']['fruits']['苹果'] + friuts['草莓']*info['小明']['fruits']['草莓'] + friuts['香蕉']*info['小明']['fruits']['香蕉']
b = friuts['葡萄'] *info['小刚']['fruits']['葡萄'] + friuts['橘子'] *info['小刚']['fruits']['橘子'] + + friuts['樱桃'] *info['小刚']['fruits']['樱桃']
info['小明']['money'] = a
info['小刚']['money'] = b
print(info)


# 编写一个函数，传入一个列表，并统计每个数字出现的次数。
# 返回字典数据：{21:3,56:9,10:3}（阿里一轮笔试题）
print("----------------------------")
numlist = []
for i in range(5):
    new = int(input("请输入数字："))
    numlist.append(new)
print(numlist)

dictCount = {}
for k in range(len(numlist)):
    dictCount[numlist[k]] = numlist.count(numlist[k])
print(dictCount)


print("----------------------------")
# 有以下公司员工信息，将数据转换为字典方式
# 姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"] ]
names1 = {}
for p in range(len(names)):
    names1[names[p][0]] = {names[p][1], names[p][2], names[p][3], names[p][4], names[p][5], names[p][6]}
print(names1)