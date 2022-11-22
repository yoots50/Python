user = input()
if user.split(' ')[1] == '달러':
    print(int(user.split(' ')[0]) * 1167)
elif user.split(' ')[1] == '엔':
    print(int(user.split(' ')[0]) * 1.096)
elif user.split(' ')[1] == '유로':
    print(int(user.split(' ')[0]) * 1268) 
else :
    print(int(user.split(' ')[0]) * 171)
