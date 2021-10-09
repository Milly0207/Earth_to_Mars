score = input("请输入分数：")
if score.isdigit():
    score = int(score)
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "E"
    print("您的分数等级为：",grade)
else:
    print("输入格式错误！")