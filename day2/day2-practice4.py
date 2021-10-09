num = input("请输入数值：")
if num.isalpha():
    print("数值输入格式错误！")
else:
    num = float(num)
    unit = input("请输入单位(英寸/厘米)：")
    if unit.isalpha():
        if unit == "英寸":
            print(num, "英寸 = ",num * 2.54, "厘米")
        elif unit == "厘米":
            print(num,"厘米 = ",num / 2.54, "英寸")
        else:
            print("单位输入错误！")
    else:
        print("单位输入格式错误！")
