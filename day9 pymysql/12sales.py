import xlrd
import pymysql
from DBUtils import *

# sql = "create database 12sales character set utf8;"
# sql = "create table 12sales.12sales(日期 char(6),服装名称 char(6), 价格 float(12), 本月库存数量 int, 日销售量 int);"
# create(sql)

wb = xlrd.open_workbook(filename=r"E:\2020年每个月的销售情况.xls", encoding_override=True)

nsheet = wb.nsheets

for i in range(nsheet):
    table = wb.sheet_by_index(i)
    rows = table.nrows
    for j in range(1, rows):
        data = table.row_values(j)

        sql = "insert into 12sales.12sales values (%s, %s, %s, %s, %s)"
        param = [(str(i+1)+'月'+data[0]), data[1], float(data[2]), int(data[3]), int(data[4])]
        update(sql, param)