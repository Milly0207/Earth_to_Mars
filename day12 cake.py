'''
生产-消费者模型
    蛋糕店有3位厨师同时负责做蛋挞，
    做完1个蛋挞就放到篮子里，篮子最多能存放500个蛋挞
    若篮子装满了，厨师需等待3秒，然后判断是否仍是已满，若未满则可继续造蛋挞

    6个顾客同时在抢购蛋挞，每人拥有3000元，蛋挞3元/个，
    当篮子里的蛋挞不够时，需等待3秒，然后判断是否有蛋挞，若有则继续抢购

    厨师每日工资 = 制作数量 * 12元
    收银器统计销售额
    统计蛋糕店今日盈利总额、生产数量、销售数量、每个厨师工资
'''
import time
from threading import Thread
from threading import Timer

price = 3       # 蛋挞售价
per_sales = 12  # 厨师做1个蛋挞的佣金
cakeNum = 0     # 可售蛋挞数量

# 厨师--------------------------------
class Chef(Thread):
    __makeNum = 0  # 厨师1制作的蛋挞数量
    sales = 0      # 厨师1工资
    name = ""

    def run(self) -> None:  # 制作蛋挞
        global cakeNum
        while True:
            if cakeNum < 500:  # 判断篮子是否已满500个
                cakeNum += 1  # 若未满，则做一个蛋挞
                self.__makeNum += 1         # 厨师制作数量+1
                cakeNum += 1
                print(self.name, "做好1个蛋挞，篮中有", cakeNum, "个蛋挞可售")
            else:
                print(self.name, "篮子已满，请稍等")
                print(self.name, "今天做了", self.getMakeNum(), "个蛋挞")
                time.sleep(3)

    def getMakeNum(self):   # 厨师1获取制作的数量
        return self.__makeNum

    def countSales(self):   # 统计厨师1今日工资
        global per_sales
        self.sales = self.__makeNum * per_sales


# 顾客--------------------------------
class Customer(Thread):
    name = ""
    money = 3000    # 余额
    number = 0    # 购买数量

    def run(self) -> None:
        global cakeNum
        global price
        while True:
            if self.money >= price:  # 判断钱是否够买1个蛋挞
                if cakeNum > 0:      # 如果钱够，判断是否还有蛋挞可售
                    self.number += 1          # 若果有，则购买，买到的蛋挞+1
                    self.money -= 1 * price   # 付款
                    cakeNum -= 1              # 可售蛋挞-1
                    print("蛋挞-1，", cakeNum, "个蛋挞可售")
                    print(self.name, "的蛋挞+1，钱包还剩", self.money, "元")
                else:
                    print(self.name, "蛋挞卖完了~ ")
                    print(self.name, "今日抢到", self.number, "个蛋挞")
                    time.sleep(3)
            else:
                print(self.name, "您的余额不足了~")
                print(self.name, "今日抢到", self.number, "个蛋挞")
                break

# 收银器-------------------------------
class SavingPot(Customer, Chef):
    earnings = 0  # 盈利总额
    paySales = 0  # 应付工资
    profit = 0    # 利润 = 盈利总额 - 应付工资

    def countEarnings(self):
        global price
        self.earnings += super().number * price
        print("今日销售额", self.earnings)

    def countPaySales(self):
        global per_sales
        self.paySales += super().getMakeNum() * per_sales
        print("今日应付厨师薪资", self.paySales)

    def countProfit(self):
        self.profit = self.earnings - self.paySales


# ----------------------------------------

chef1 = Chef()
chef2 = Chef()
chef3 = Chef()

chef1.name = "1号厨师"
chef2.name = "2号厨师"
chef3.name = "3号厨师"

cust1 = Customer()
cust2 = Customer()
cust3 = Customer()

cust1.name = "❀❀花花"
cust2.name = "绒绒"
cust3.name = "飒飒"


chef1.start()
chef2.start()
chef3.start()
cust1.start()
cust2.start()
cust3.start()



# pot = SavingPot()
# pot.countEarnings()
# pot.countPaySales()
# pot.countProfit()