---
title: mygpt2
emoji: 🌍
colorFrom: purple
colorTo: green
sdk: docker
pinned: false
license: mit
app_port: 9000
---

## ADMIN_PASSWORD

新增一个机密环境变量`ADMIN_PASSWORD`

变量值随便设置一个，自己记得就行，例如`love`

如果没有设置这个环境变量，就需要控制台看密码了，每次会随机一个

## 管理员放置账号

注意：由于数据没有持久化存储，每次Factory reboot之后，都需要重新放置账号。

访问：服务器地址/getsession

你就会打开`ChatLogin-Session`页面

Email address：填写你的ChatGPT的邮箱账号

Password：填写你的ChatGPT的密码

AdminPassword：填写机密环境变量`ADMIN_PASSWORD`的值

然后点击`获取AccessToken`按钮

如果显示信息如下，说明你设置成功了

```
{"code":1,"detail":"session.json saved","email":"****@***.com","expires":"2024-05-04T07:56:04.180Z"}
```

## 其他用户访问公益网站

访问：服务器地址

输入任意6位数的`UserToken`即可开始使用
