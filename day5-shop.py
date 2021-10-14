'''
 Frank的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条
任务：打折：随机获得优惠券（9折10，5折5，1折2，面单1.
            单个商品打折9折10，5折5，1折2，面单1）
'''
print("=========单个商品打折===========")
import random
money = random.randint(0, 99999)
print(money)
mycart = []
a = [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9,
     0.5, 0.5, 0.5,0.5, 0.5,
     0.1, 0.1,
     0]
shop=[
    ["刀🔪", 999],
    ["斧子", 200],
    ["👍", 90000],
    ["coco", 150],
    ["枸杞", 900],
]
for index,value in enumerate(shop):
    print(index,":",value)
while True:
    chose = input("请输入要购买的商品编号：")
    if chose.isdigit():
        chose = int(chose)
        if chose < len(shop):
            if money >= shop[chose][1]:
                yesno = random.choice([0,1])     # 0:没有优惠， 1：有优惠
                if yesno == 1 and len(a) > 0:    # 有优惠，且优惠机会有剩余
                    discount = random.choice(a)  # 随机抽取优惠折扣
                    mycart.append([shop[chose][0], shop[chose][1] * discount])  # 加入购物车,金额为折扣价
                    money = money - shop[chose][1]*discount
                    print("加购成功! ", discount * 10, "折优惠。 您的余额为：", money)
                    a.remove(discount)           # 减少该折扣的优惠机会
                else:                            # 没有优惠
                    mycart.append(shop[chose])
                    money = money - shop[chose][1]
                    print("加购成功!", "您的余额为：", money)
            else:
                print("您的余额不足")
        else:
            print("商品不存在")
    elif chose == "q" or chose == "Q":
        print("-------------------")
        for index, value in enumerate(mycart):
            print(index, ":", value)
        print("您的余额为：", money)
        break
    else:
        print("输入错误，请重新输入")


print("")
print("===========总价打折=============")
import random
money = random.randint(0,99999)
money1 = money
print(money)
mycart = []
a = [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9,
     0.5, 0.5, 0.5,0.5, 0.5,
     0.1, 0.1,
     0]
shop=[
    ["刀🔪", 999],
    ["斧子", 200],
    ["👍", 90000],
    ["coco", 150],
    ["枸杞", 900],
]
for index,value in enumerate(shop):
    print(index, ":", value)
while True:
    chose = input("请输入要购买的商品编号：")
    if chose.isdigit():
        chose = int(chose)
        if chose < len(shop):
            if money1 >= shop[chose][1]:
                mycart.append(shop[chose])
                money1 = money1 - shop[chose][1]
            else:
                print("您的余额不足")
        else:
            print("商品不存在")
    elif chose == "q" or chose == "Q":
        print("-------------------")
        price = 0  # 商品总价
        for index, value in enumerate(mycart):
            print(index, ":", value)     # 查看购物车商品
            price = price + value[1]     # 计算总价
        print("商品总价：", price)
        yesno = random.choice([0,1])     # 0:没有优惠， 1：有优惠
        if yesno == 1 and len(a) > 0:    # 有优惠，且优惠机会有剩余
            discount = random.choice(a)  # 随机抽取优惠折扣
            print("恭喜您获得一张", discount * 10, "折券,", "实付金额：", price * discount)
            money = money - price * discount
        else:
            print("对不起，本单没有优惠，实付金额：", price)
            money = money - price
        print("您的余额为：", money)
        break
    else:
        print("输入错误，请重新输入")