---
title: Go Proxy Bingai
emoji: 🌍
colorFrom: gray
colorTo: indigo
sdk: docker
pinned: false
---
此方案会被自动删除，很有可能是因为包含了验证服务器

环境变量

需要两个必填的环境变量Space variables Public

USER_KievRPSSecAuth：随便填写一个字符串，作用是免登陆

HEADLESS：固定值 false，huggingface部署必须传这个参数，否则无法自动过机器人验证
