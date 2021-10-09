side1 = input("请输入第1条边长度：")
side2 = input("请输入第2条边长度：")
side3 = input("请输入第3条边长度：")
if side1.isalpha() or side2.isalpha() or side3.isalpha():
    print("输入格式错误!")
else:
    side1 = float(side1)
    side2 = float(side2)
    side3 = float(side3)
    if (side1+side2>side3) or (side1+side3>side2) or (side2+side3>side1):
        perimeter1 = side1 + side2 + side3
        # 求三角形的面积
        p = (side1 + side2 + side3) * 0.5
        area1 = (p * (p-side1) * (p-side2) * (p-side3))**0.5
        print("周长：",round(perimeter1, 2))
        print("面积：",round(area1, 2))
    else:
        print("不能构成三角形！")


