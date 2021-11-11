f = open(file='baidu_x_system.log', encoding='utf-8')

# 取出每一行的ip放入lists中
lists = []
for r in f.readlines():   # readlines() https://www.runoob.com/python/file-readlines.html
    lists.append(r.split(" ")[0])  # 获取该行第一个空格前的字符串

# print("lists", lists)

# 结果统计在字典中
countList = {}
for i in lists:   # 遍历列表，进行统计
    if i not in countList:
        countList[i] = 1
    elif i in countList:
        countList[i] += 1

# print("countList", countList)

for a, b in countList.items():  # 遍历字典，打印结果
    print(a, '操作了', b, '次')
