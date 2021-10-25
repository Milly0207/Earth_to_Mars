import xlrd

file = xlrd.open_workbook(filename=r"E:\2020年每个月的销售情况.xls", encoding_override=True)

dict_month_num = {}  # 月总销量字典
dict_single_sale_num = {}  # 每种商品的年总销量
list_single_sale_num = []

dict_single_sale_money = {}  # 每种商品的年总额
list_single_sale_money = []

dict = {}  # 总销量字典
dict_sale_year = {}   # 商品年销量字典
dict_sale_month = {}  # 商品月销量字典
dict2 = {}  # 总销售额字典
dict_money_year = {}  # 商品月销售额字典
dict_money_month = {}  # 商品月销量字典

# 计算所有商品的 年总销量、月销售总量、年销售总额、月销售总额
total_num = 0  # 年总销量
total_sale = 0  # 年销售总额
for i in range(0, 12):
    table = file.sheet_by_index(i)
    rows = table.nrows
    month_num = 0     # 月销量
    sale1 = float(0)  # 月销售额
    for j in range(1, rows):
        date = table.row_values(j)
        month_num += date[4]
        sale1 = sale1 + date[2] * date[4]
    dict_month_num[i+1] = int(month_num)
    total_num += int(month_num)
    total_sale += sale1
    dict_money_month[i + 1] = round(sale1, 2)
# print('月总销量dict_month_num:', dict_month_num)
# print('全年所有商品总销量total_num:', total_num, '件')  # 22299
# print("每月所有商品总销售额dict_money_month:", dict_money_month)
print("全年所有商品总销售额total_sale:", round(total_sale, 2), "元")  # 2400069


# 获取全部商品种类
sort = {}  # 商品种类
for j in range(12):
    table = file.sheet_by_index(j)
    rows = table.nrows
    for i in range(1, rows):
        date = table.row_values(i)
        sort[date[1]] = date[1]
# print("所有商品种类:", sort)

print("")
print('每种衣服的年销售量、销售额占比:')
# 统计每种商品的销量、销售额
for key, value in sort.items():
    # 将当前商品每月销量汇总到一起：
    # {'羽绒服': {1: 239, 2: 239, 3: 229, 4: 99, 5: 239, 6: 219, 7: 160, 8: 239, 9: 20, 10: 30, 11: 239, 12: 229}}
    dict_sale_year = {key: {}}
    dict_sale_month = dict_sale_year[key]

    dict_money_year = {key: {}}
    dict_money_month = dict_money_year[key]

    sale_year = 0   # 年销量
    money_year = 0  # 年销售额
    for i in range(0, 12):
        table = file.sheet_by_index(i)
        rows = table.nrows
        sale_month = 0  # 月销量
        sale_money_by_month = 0  # 月销售额
        for j in range(1, rows):
            date = table.row_values(j)
            if date[1] == key:
                sale_year += date[4]
                sale_month += date[4]
                sale_money_by_month += date[2] * date[4]
                money_year += date[2] * date[4]
        dict_sale_month[i+1] = int(sale_month)  # 记录每月销量
        dict_money_month[i+1] = round(sale_money_by_month, 2)  # 记录每月销售额

    print('【', key, '】', '\n销售量占比:', round((sale_year/total_num)*100, 2), "%")
    print('销售额占比:', round((money_year / total_sale) * 100, 2), "%")

    # 将所有商品及每月销量、销售额汇总到一起
    for a, b in dict_sale_year.items():
        dict[a] = b
    for c, d in dict_money_year.items():
        dict2[c] = d

print("")
# print('总销量字典dict:', dict)
print("")
# print('总销售额字典dict2:', dict2)


# 计算销量最高、最低的衣服
print("")
for i in dict:
    single_sale_num = 0
    for j in dict[i]:
        single_sale_num += dict[i][j]
    list_single_sale_num.append(single_sale_num)
    # print(i, single_sale_num)
    dict_single_sale_num[i] = single_sale_num

for i in dict_single_sale_num:
    if dict_single_sale_num[i] == max(list_single_sale_num):
        print('全年最畅销的衣服:', i, ',共', dict_single_sale_num[i], '件')
    if dict_single_sale_num[i] == min(list_single_sale_num):
        print('全年销量最低的衣服:', i, ',共', dict_single_sale_num[i], '件')
print("")


# 计算每种衣服的月销售（件数）占比
for i in dict:
    # print(dict[i])     # xx12个月的销售数据
    for j in dict[i]:
        a = dict[i][j]   # xx第n月的销量
        for k in dict_month_num:  # 第n月的总销量
            rate = a / dict_month_num[k]
        print(i, j, '月份销量占比:', round((rate * 100), 2), '%')

season_saleNum = {

}
# 每个季度最畅销的衣服
dict_season1_saleNum = {}
dict_season2_saleNum = {}
dict_season3_saleNum = {}
dict_season4_saleNum = {}
for i in dict:
    season_saleNum = 0
    for j in dict[i]:
        if j == 1 or j == 2 or j == 3:
            season_saleNum += dict[i][j]
            dict_season1_saleNum[i] = season_saleNum
        if j == 4 or j == 5 or j == 6:
            season_saleNum += dict[i][j]
            dict_season2_saleNum[i] = season_saleNum
        if j == 7 or j == 8 or j == 9:
            season_saleNum += dict[i][j]
            dict_season3_saleNum[i] = season_saleNum
        if j == 10 or j == 11 or j == 12:
            season_saleNum += dict[i][j]
            dict_season4_saleNum[i] = season_saleNum
print('第一季度销售数据', dict_season1_saleNum)
print('第二季度销售数据', dict_season2_saleNum)
print('第三季度销售数据', dict_season3_saleNum)
print('第四季度销售数据', dict_season4_saleNum)

#---------------------------------------
# 全年的销售总额  √
# 每种衣服的销售（件数）占比  √
# 每件衣服的月销售（件数）占比  √
# 每件衣服的销售额占比  √
# 每个季度最畅销的衣服
# 最畅销的衣服是那种  √
# 全年销量最低的衣服  √





