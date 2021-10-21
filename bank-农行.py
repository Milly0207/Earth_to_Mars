import random
bank = {}
info = '''
    ------------账户信息------------
    卡类型: {type}
    账  号: {account}
    姓  名: {username}
    密  码: {password}
    地  址:
        国 家: {country}
        省 份: {province}
        街 道: {street}
        门牌号: {door}
    账户余额: {money} 元
    开 户 行: {bank_name}
    -------------------------------
'''
bank_name = '中国农业银行北京昌平支行'

def welcome():
    print("****************************")
    print("*    中国农业银行账户管理系统   *")
    print("*--------------------------*")

    choice = {'1': '开户', '2': '存钱', '3': '取钱', '4': '转账', '5': '查询', '6': '退出'}
    welcome_item = '''*          {}、{}          *'''
    keys = choice.keys()
    for i in keys:
        print(welcome_item.format(i, choice[i]))
    print("****************************")

# 查看信息
def look_myinfo(username):
    user = bank[username]
    print(info.format(
        type=user['type'],
        username=username,
        account=user['account'],
        password='*'*len(user['password']),
        country=user['country'],
        province=user['province'],
        street=user['street'],
        door=user['door'],
        money=user['money'],
        bank_name=user['bank_name']
    ))

# 1、开户----------------------------------------------------
def add_user():
    type = add_user_type()
    username = input("用户名")
    password = passwd()
    country = input("国家")
    province = input("省份")
    street = input("街道")
    door = input("门牌号")

    status = bank_add_user(type, username, password, country, province, street, door)
    if status == 1:
        print("开户成功,下面是你的账户信息:")
        look_myinfo(username)
    elif status == 2:
        print("该用户已存在")
    elif status == 3:
        print("用户已满，请到其他银行开户")

# 选择开户类型
def add_user_type():
    print("\n本行账户分为金卡和普通卡：\n"
          "1.金卡：最大转账额为5万，转出最大5万，转入没限制\n"
          "2.普通卡：最大转账额为2万，转出最大2万，转入没限制\n")
    while True:
        type = input("请输入开户类型：")
        if type == '1':
            return '金卡'
        elif type == '2':
            return '普通卡'
        else:
            print("输入错误")

# 输入密码
def passwd():
    while True:
        passwd = input("密码")
        if passwd.isdigit() and len(passwd) == 6:
            return passwd
        else:
            print("请输入六位数字密码")

# 系统处理开户
def bank_add_user(type, username, password, country, province, street, door):
    if len(bank) >= 100:
        return 3
    elif username in bank:
        return 2
    else:
        bank[username] = {
            'type': type,
            'account': random.randint(10000000, 99999999),
            'password': password,
            'country': country,
            'province': province,
            'street': street,
            'door': door,
            'money': round(0, 2),
            'bank_name': bank_name
        }
        return 1

# 2、存钱----------------------------------------------------
def save_money():
    username = input("请输入用户名:")
    addmoney = input("请输入存款金额:")
    add = bank_add_money(username, addmoney)

    if add:
        print("存钱成功")
        print("下面是您的存款信息:")
        look_myinfo(username)
    else:
        print("用户不存在")

# 增加账户余额
def bank_add_money(username,addmoney):
    if username in bank:
        bank[username]['money'] += float(addmoney)
        return True
    else:
        return False

# 3、取钱----------------------------------------------------
def draw_money():
    username = input("请输入用户名:")
    password = input("请输入密码：")
    money = input("请输入取款金额:")
    reduce = bank_reduce_money(username, password, money)
    if reduce == 0:
        print("取款成功,以下是您的账户信息:")
        look_myinfo(username)
    elif reduce == 1:
        print("用户不存在")
    elif reduce == 2:
        print("密码错误")
    elif reduce == 3:
        print("账户余额不足")

# 减少账户余额
def bank_reduce_money(username, password,money):
    if username in bank:
        if password == bank[username]['password']:
            if float(money) <= bank[username]["money"]:
                bank[username]['money'] -= float(money)
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

# 4、转账----------------------------------------------------
def transfer():
    username = input("请输入转出账户用户名:")
    password = input("请输入转出账户密码：")
    username1 = input("请输入转入账户用户名:")
    money = input("请输入转账金额:")
    transfer = bank_transfer(username, password, username1, money)
    if transfer == 1:
        print("账号输入错误")
    elif transfer == 2:
        print("密码输入错误")
    elif transfer == 3:
        print("余额不足")
    elif transfer == 4:
        print("转账金额超出限制")
    else:
        print("转账成功，下面是您的账户信息:")
        look_myinfo(username)

# 处理转账
def bank_transfer(username,password,username1,money):
    if username in bank and username1 in bank:
        if password == bank[username]['password']:
            if float(money) <= bank[username]['money']:
                if (bank[username]['type'] == '金卡' and float(money) <= 50000) or (bank[username]['type'] == '普通卡' and float(money) <= 20000):
                    bank[username]['money'] -= float(money)
                    bank[username1]['money'] += float(money)
                else:
                    return 4
            else:
                return 3
        else:
            return 2
    else:
        return 1

# 5、查询----------------------------------------------------
def query():
    username = input("请输入用户名:")
    password = input("请输入密码：")
    if username in bank:
        if password == bank[username]['password']:
            look_myinfo(username)
        else:
            print("密码输入错误")
    else:
        print("该用户不存在")


#######################################################
while True:
    welcome()
    chose = input("请输入您要办理的业务:")
    if chose == "1":
        add_user()
    elif chose == "2":
        save_money()
    elif chose == "3":
        draw_money()
    elif chose == "4":
        transfer()
    elif chose == "5":
        query()
    elif chose == "6":
        print("欢迎您再次使用该系统，再见！")
        break
    else:
        print("输入错误！")