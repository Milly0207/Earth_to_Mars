# 5.有以下两个数，使用+，-号实现两个数的调换。
print("")
print("---5、使用+，-号实现两个数的调换两个数----------------------")
A = 27
B = 72
print("A =",A,",B =",B)
while True:
    symbol = input("输入+或-：")
    if symbol == "+" or symbol == "=":
        C = B
        D = A
        print("A =",C,",B =",D)
    elif symbol == "-" or symbol == "_":
        C = A
        D = B
        print("A =", C, ",B =", D)
    else:
        print("输入错误，请重新输入")