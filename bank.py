import random
print("****************************")
print("*     中国银行账户管理系统     *")
print("****************************")
print("*          1、开户          *")
print("*          2、存钱          *")
print("*          3、取钱          *")
print("*          4、转账          *")
print("*          5、查询          *")
print("*          6、再见          *")
print("****************************")

# 开户逻辑
bank = {}  # 空的银行账户数据库
# 'Frank': {'account': 10936377, 'password': '123', 'country': '中国', 'province': '山东', 'street': '蓝翔', 'door': '001'},
bank_name = "中国银行M78分行"
# 传入参数添加到字典里面
def bank_add(account,username,password,country,province,street,door):
    if username in bank:  # 说明用户已存在
        return 2
    elif len(bank) >= 100:
        return 3
    else:
        bank[username] = {
            "account": account,
            "password": password,
            "country": country,
            "province": province,
            "street": street,
            "door": door,
            "money": 0,
            "bank_name": bank_name
        }
        return 1
def useradd():
    account = random.randint(10000000, 99999999)
    username = input("请输入您的用户名:")
    password = input("请输入您的用户密码:")
    print("下面请输入你的详细地址:")
    country = input("\t\t请输入您的国家:")
    province = input("\t\t请输入您的省份:")
    street = input("\t\t请输入您的街道:")
    door = input("\t\t请输入您的门牌号:")
    add = bank_add(account, username, password, country, province, street, door)
    if add == 3:
        print("数据库已满请到其他银行开户")
    elif add == 2:
        print("请输入其他用户名:")
    elif add == 1:
        print("开户成功,下面是你的详细信息:")
        info = '''
        ------------个人信息------------
        用户名: %s
        账 号: %s
        密 码: ******
        国 籍: %s
        省 份: %s
        街 道: %s
        门牌号: %s
        余 额: %s 元
        开户行名称: %s
        ------------------------------
        '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))

#--------------------------------------------------------------------------------------
# 存钱
def save_money():
    username = input("请输入用户名:")
    account = input("请输入账号:")
    addmoney = input("请输入存款金额:")
    add = add_money(username, addmoney)
    if add == 1:
        print("存钱成功")
        print("下面是您的存款信息:")
        info = '''
        --------------存款信息--------------
        用户名：%s
        账 号: %s
        存款金额: %s 元
        账户余额: %s 元
        ----------------------------------
        '''
        print(info % (username, account, addmoney, bank[username]['money']))
    elif add == False:
        print("用户不存在")

# 增加账户余额
def add_money(username,addmoney):
    if username in bank:
        bank[username] = {
            "account": bank[username]["account"],
            "password": bank[username]["password"],
            "country": bank[username]["country"],
            "province": bank[username]["province"],
            "street": bank[username]["street"],
            "door": bank[username]["door"],
            "money": bank[username]['money'] + int(addmoney),
            "bank_name": bank_name
        }
        return 1
    else:
        return False

#--------------------------------------------------------------------------------------
# 取钱
def draw_money():
    username = input("请输入用户名:")
    account = input("请输入账号:")
    password = input("请输入密码：")
    money = input("请输入取款金额:")
    reduce = reduce_money(username, account, password, money)
    if reduce == 0:
        print("取款成功,以下是您的取款信息:")
        info = '''
        --------------取款信息--------------
        用户名：%s
        账 号: %s
        取款金额: %s 元
        账户余额: %s 元
        ----------------------------------
        '''
        print(info % (username, account, money, bank[username]['money']))
    elif reduce == 1:
        print("用户不存在")
    elif reduce == 2:
        print("密码错误")
    elif reduce == 3:
        print("账户余额不足")

# 减少账户余额
def reduce_money(username, account, password,money):
    if username in bank:
        if password == bank[username]['password']:
            if float(money) <= bank[username]["money"]:
                bank[username] = {
                    "account": bank[username]["account"],
                    "password": bank[username]["password"],
                    "country": bank[username]["country"],
                    "province": bank[username]["province"],
                    "street": bank[username]["street"],
                    "door": bank[username]["door"],
                    "money": bank[username]['money'] - float(money),
                    "bank_name": bank_name
                }
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

#--------------------------------------------------------------------------------------
# 转账
def transfer():
    username = input("请输入转出账户用户名:")
    account = input("请输入转出账户账号:")
    password = input("请输入转出账户密码：")
    username1 = input("请输入转入账户用户名:")
    account1 = input("请输入转入账户账号:")
    money = input("请输入转账金额:")
    transfer = transfer_process(username, account, password, username1, account1, money)
    if transfer == 1:
        print("账号输入错误")
    elif transfer == 2:
        print("密码输入错误")
    elif transfer == 3:
        print("余额不足")
    else:
        print("转账成功，下面是您的转账信息:")
        info = '''
        --------------转账信息--------------
        转出账户用户名: %s
        转出账户账号: %s
        转入账户用户名: %s
        转入账户账号: %s
        转 账 金 额: %s 元
        账 户 余 额: %s 元
        ----------------------------------
        '''
        print(info % (username, account, username1, account1, money, bank[username]['money']))
# 处理转账
def transfer_process(username,account,password,username1,account1,money):
    if username in bank and username1 in bank:
        if password == bank[username]['password']:
            if float(money) <= bank[username]['money']:
                bank[username] = {
                    "account": bank[username]["account"],
                    "password": bank[username]["password"],
                    "country": bank[username]["country"],
                    "province": bank[username]["province"],
                    "street": bank[username]["street"],
                    "door": bank[username]["door"],
                    "money": bank[username]['money'] - float(money),
                    "bank_name": bank_name
                }
                bank[username1] = {
                    "account": bank[username1]["account"],
                    "password": bank[username1]["password"],
                    "country": bank[username1]["country"],
                    "province": bank[username1]["province"],
                    "street": bank[username1]["street"],
                    "door": bank[username1]["door"],
                    "money": bank[username1]['money'] + float(money),
                    "bank_name": bank_name
                }
            else:
                return 3
        else:
            return 2
    else:
        return 1

#--------------------------------------------------------------------------------------
# 查询
def query():
    username = input("请输入用户名:")
    account = input("请输入账号:")
    password = input("请输入密码：")
    if username in bank:
        if password == bank[username]['password']:
            info = '''
            ------------当前账户信息------------
            账   号: %s
            密   码: ******
            余   额: %s 元
            居住地址: %s
            开 户 行: %s
            ----------------------------------
            '''
            print(info % (account, bank[username]['money'], bank[username]['country']+bank[username]['province']+bank[username]['street']+bank[username]['door'], bank[username]['bank_name']))
        else:
            print("密码输入错误")
    else:
        print("该用户不存在")

#######################################################

while 1:
    index = int(input("请输入您的操作:"))
    if index == 1:
        print("1、开户")
        useradd()
        print(bank)
    elif index == 2:
        print("2、存钱")
        save_money()
        print(bank)
    elif index == 3:
        print("3、取钱")
        draw_money()
        print(bank)
    elif index == 4:
        print("4、转账")
        transfer()
        print(bank)
    elif index == 5:
        print("5、查询")
        query()
        print(bank)
    elif index == 6:
        print("bye~")
        exit()
    else:
        print("输入错误")

