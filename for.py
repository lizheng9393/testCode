"""
chengji =[88,90,98,78,68]
hegede = []
buhegede = []
for i in chengji:
    if i <70:
       buhegede.append(i)
    else:
      hegede.append(i)
print(hegede)
print(buhegede)        
zhanghao = {"username":"王美丽","chengji":88}
for i in zhanghao:
    print(i)
    print(zhanghao[i])
"""
t_usrs = [{"username":"小静","passward":"123456"},{"username":"小韩","passward":"123456"}]
u = input("请输入账号")
p = input("请输入密码")
a = 1
for i in t_usrs:
    if u == i.get("username") and p == i.get("passward"):
        print("登陆成功")
        break
    else:
       if len(t_usrs) == a:
            print("登录失败")
    a = a + 1