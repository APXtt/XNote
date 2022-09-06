a = True
b = 'abc'

for i in range(2):
    if a == True:
        a = False
        b = '123'
        print(b)
    elif b == '123':
        print('sucess')