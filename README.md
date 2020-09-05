# Mailling Software
This is a small **Django** Project for sending Mail without going to Gmail Website. You can easily send any kind of file with the subject and plain text...
___

## Settings Configuration

In *settings file* in django project folder...
```
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True
EMAIL_HOST_USER     = '#Your gmail'
EMAIL_HOST_PASSWORD = '#Your Password'
```
> I user Gmail Account in this project

So you should user

* SMTP
* HOST
* PORT
* TLS

---
> In EMAIL_HOST_USER, you use your own 'yourmail@gmail.com' in a single quotation or double quotation. 

> In EMAIL_HOST_PASSWORD, you use your own 'password' in a single quotation or double quotation. 
---
## Password Configuration 
1. If you are not using ***2-steps verification***, you have to ***allow a less secure app*** for your Gmail account.
1. If you user ***2-steps verification***, you have to use the ***app password*** for your application. They will give you a plain text password for your particular app. You can use that password in ***EMAIL_HOST_PASSWORD*** without using your main Gmail password. 
