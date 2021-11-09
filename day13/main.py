# 生成测试报告
import HTMLTestRunner
# 需要自己另外下载HTMLTestRunner工具，并放在python程序安装目录下Lib目录中，https://blog.csdn.net/XingLongSKY/article/details/89309729
# 并修改几处代码：https://blog.csdn.net/weixin_37579123/article/details/84900157

import unittest

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

# 加载所有测试用例
tests = unittest.defaultTestLoader.discover(r"E:\Python自动化测试\Python\20组\day13【单元测试】\任务-用代码发送邮件", pattern="Test*.py")
# "Test*.py" 加载所有以Test开头的用例文件

# 运行器来执行用例，并生成测试报告
runner = HTMLTestRunner.HTMLTestRunner(
    title="计算器的测试报告",  # 测试报告标题
    description="这是加法测试报告",  # 详细描述
    verbosity=1,  # 详细程度
    stream=open(file="测试报告.html", mode="wb")  # 测试报告写入哪个文件中
    # w+模式需要写上参数encoding="utf-8"。
    # python3 wb模式(二进制模式)不需要另外加参数：encoding="utf-8"。 https://blog.csdn.net/kingyuan666/article/details/81214954
)

# 3.运行
runner.run(tests)   # 运行结果“F.......”, 说明有一个错误(F)，7个成功.


# 4.邮件发送代码  任务1：使用代码发送邮件，并把测试报告当成附件发送给我。
# 菜鸟教程:https://www.runoob.com/python/python-email.html
# 温馨：用户名，密码：smtp授权码

# 第三方 SMTP 服务:
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "1332203911@qq.com"    # 用户名
mail_pass = "xqhsxlsaholkjaha"   # 口令 授权码

sender = '1332203911@qq.com'  # 发送账号
# receivers = '2431320433@qq'  # 收件账号
# receivers = ['2147428672@qq.com', '1332203911@qq.com']  # 可添加多个账号群发
receivers = '2147428672@qq.com'

#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header(sender, 'utf-8')
message['To'] = Header(receivers, 'utf-8')
subject = '测试报告-20组李柳蓉'   # 邮件主题
message['Subject'] = Header(subject, 'utf-8')

#邮件正文内容
message.attach(MIMEText("测试报告"))

# 构造附件1，传送当前目录下的 xxx 文件
sendfile = open('测试报告.html', encoding="utf-8").read()   # 不加encoding="utf-8"会报错
att1 = MIMEText(sendfile, 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件附件中显示什么名字，但用中文会乱码，记得加后缀
att1["Content-Disposition"] = 'attachment; filename="testReport.html"'
message.attach(att1)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25为SMTP端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("\n邮件发送成功")
except smtplib.SMTPException:
    print("\nError: 无法发送邮件")



# #邮件主题
# subject = "附件的邮件"
#
# # 发送附件
# sendfile = open("测试报告.html", "r", encoding="utf-8").read()
#
# att = MIMEText(sendfile, "base64", "utf-8")
# att["Content-Type"] = "application/octet-stream"
# att["Content-Disposition"] = "attachment;filename = 'testReport.html'"
#
# msgRoot = MIMEMultipart('related')
# msgRoot['Subject'] = subject
# msgRoot.attach(att)
#
# smtp = smtplib.SMTP()
# smtp.connect(mail_host, 25)
# smtp.login(mail_user, mail_pass)
# smtp.sendmail(sender, receivers, msgRoot.as_string())
# smtp.quit()