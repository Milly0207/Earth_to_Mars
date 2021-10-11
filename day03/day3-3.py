# 6.实现登录系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
print("")
print("---6、登录系统，三次密码输入错误，锁定系统---------------------")
username = 'root'
password = 'admin'
i = 1
while 1==1:
    if i<=3:
        input_username = input("请输入用户名：")
        input_password = input("请输入密码：")
        if input_username == username and input_password == password:
            print("登录成功！")
            exit()
        else:
            print("用户名或密码错误")
            i += 1
    else:
        print("你已输错3次，系统将锁定")
        exit()