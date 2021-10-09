fahren = input("请输入华氏温度：")
if fahren.isalpha() :
    print("输入格式错误！")
else:
    fahren = float(fahren)
    centi = (fahren-32)/1.8
    print(fahren,"华氏度 = ",round(centi,2),"摄氏度")