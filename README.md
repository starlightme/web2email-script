##基本说明##

本脚本基于Python3的语法进行编写，用于抓取指定web页面的文字信息，然后整合后发送邮件到对应的收件人。

我个人是拿来在本地用的，因为估计会经常修改。理论上也可以放到VPS上运行，但是往往VPS上的Python版本都是2，所以使用前请修改对应的语法规范

##使用方法：##

在脚本起始处填写对应的邮件设置，如果使用QQ邮箱发送，请先开启设置，详见参考引用

main函数中的URL对应你要抓取的页面，在 get_page()函数中请写入浏览器字符串

在 get_string() 函数中填写对应的正则表达式和函数进行内容的匹配和收集

##感谢:##

编写正则表达式中请教了[@Puteulanus](https://github.com/puteulanus)同学，终于写出了自己想要的效果，非常感谢

##协议：##

Apache 2.0

##引用参考：##
* [Gmail，QMail，163邮箱的 IMAP/SMTP/POP3 地址](http://blog.wpjam.com/m/gmail-qmail-163mail-imap-smtp-pop3/)
* [python发送各类邮件的主要方法](http://www.cnblogs.com/xiaowuyi/archive/2012/03/17/2404015.html)
* [Python正则表达式的七个使用范例](http://blog.jobbole.com/74844/)
* [正则表达式30分钟入门教程](http://deerchao.net/tutorials/regex/regex.htm)
