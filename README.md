# BirthdayReminder

github action 生日提醒

# 使用

修改config文件夹下的people.yaml文件即可，格式见注释

需要在仓库的Settings->Secrets->Actions->New repository secret添加四个Secrets
- SENDEREMAIL：发送者的邮箱;例：`example@qq.com`
- SENDERSMTPPWD：发送者邮箱的SMTP密码
- SENDERSMTPSERVER：发送者的邮箱的SMTP地址及端口；例：`smtp.qq.com:587`；不加端口号默认为`25`端口
- RECEIVERS：接收邮件的邮箱地址，多个邮箱可以以`;`分隔；例：`example1@qq.com;example2@qq.com`

# 参考

https://github.com/2892211452/birthdayBot
https://github.com/Gungnir762/birthdayReminder

# Repository

活动一下下下下
