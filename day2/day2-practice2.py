radius = input("请输入圆的半径：")
if radius.isalpha():
    print("输入格式错误！")
else:
    radius = float(radius)
    perimeter = 2 * 3.14 * radius
    perimeter = round(perimeter,2)
    area = radius * perimeter * 0.5
    area = round(area,2)
    print("周长：",perimeter,"面积：",area)