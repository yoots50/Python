lock = True
print('To open the door, you have to answer the correct password')
password = input('Type password : ')

while password != 'password' :
    password = input('Wrong password')
else :
    print('Correct!')
    lock = False

if lock == False :
    print('------------------------------------------------------------------------------------------------------------------------')
    input()
