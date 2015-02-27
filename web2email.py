# -*- coding: UTF-8 -*-

import urllib.request
import re
import smtplib  
from email.mime.text import MIMEText  

mailto_list=["***@xxx.com"] #收件人邮箱
mail_host="smtp.xxx.com"  #设置服务器
mail_user="***"    #用户名
mail_pass="**** "   #密码或者口令
mail_postfix="xxx.com"  #发件箱的后缀
    
#爬取页面的html代码    

def get_page(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','***')      #缺省部分填上浏览器字符串
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html

#取对应的字符串，可以使用正则表达式或者字符串函数

def get_string(html):
    result = ''
    list = re.findall(r'***',html)
    #目的不同，处理方法不同且不唯一，缺省部分为正则，写得太渣就不放了
    for string in list:
        match = re.search(r'***', string)
        result = result + match.group(1) + '\n'
    return result

#发送邮件

def send_mail(to_list,sub,content):  
    me = "hello"+"<"+mail_user+"@"+mail_postfix+">"           #hello可以替换成其他字符
    msg = MIMEText(content,_subtype='plain',_charset='utf-8') #转换成相同的代码  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host)  
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except Exception as e:  
        print(str(e))  
        return False        

#主函数

if __name__ == '__main__':
    url = "****"
    html = get_page(url)
    string = get_string(html)
    if send_mail(mailto_list,"脚本推送",string):  
        print("发送成功")  
    else:  
        print("发送失败")
