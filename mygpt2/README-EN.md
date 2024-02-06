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

Add a new secret environment variable `ADMIN_PASSWORD`

Set the variable value to anything, as long as you remember it, for example, `love`

If you haven't set this environment variable, you will need to check the console for the password, which will be randomized each time.

## Administrator Account Placement

Note: Since the data is not persistently stored, accounts need to be placed again after each Factory reboot.

Visit: server address/getsession

This will open the `ChatLogin-Session` page.

Email address: Enter your ChatGPT's email address.

Password: Enter your ChatGPT's password.

AdminPassword: Enter the value of the secret environment variable `ADMIN_PASSWORD`.

Then click on the `获取AccessToken` button.

If the message appears as follows, you have set up successfully.

```
{"code":1,"detail":"session.json saved","email":"****@***.com","expires":"2024-05-04T07:56:04.180Z"}
```

## Other Users Access the Public Welfare Website

Visit: server address

Enter any 6-digit `UserToken` to start using.