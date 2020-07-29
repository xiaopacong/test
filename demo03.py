
def checkname(username,password):
    if len(username)>=6 and len(username)<=10:
        if username[0] in "qwertyuiopasdfghjklzxcvbnm":
             if len(password)>=8 and len(password)<=12:
                return "账号密码正确，登入成功"  
             else:
                 return "密码长度输入错误，请重新输入8-12位密码"  
        else:
            return "账号输入错误，请重新首位以小写字母开头的账号"            
    else:
        return "您的账号长度不匹配，请重新输入6-10位账号"


checkname("1111","a4444")

