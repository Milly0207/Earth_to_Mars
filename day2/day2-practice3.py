year = input("请输入年份：")
if year.isdigit():
    year = int(year) % 4
    if year != 0:
        print("不是闰年")
    else:
        print("是闰年")
else:
    print("输入格式错误！")