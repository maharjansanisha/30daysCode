import random
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
symb = '@#$%'
num = '0123456789'
ambigChar = '}{[]()/.'

length = int(input('Password Length: '))
print('Your new password: ')

password = ''

for pw in range(length):
    password += random.choice(lowercase+uppercase+symb+num+ambigChar)

print(password)
    



