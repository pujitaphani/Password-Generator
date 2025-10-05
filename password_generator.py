import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
           'p','q','r','s','t','v','w','x','y','z','A','B','C','D','E',
           'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
           'U','V','W','X','Y','Z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['!','#','$','%','&','*']

print('Welcome to Password Generator')
print("Choose difficulty level:")
print("1️⃣ Easy (letters only)")
print("2️⃣ Medium (letters + numbers)")
print("3️⃣ Hard (letters + numbers + symbols)")

level = int(input("Enter your choice (1, 2, or 3): "))

letters_required = 0
numbers_required = 0
symbols_required = 0

if level >= 1:
    letters_required = int(input("How many letters would you like to generate?: "))
if level >= 2:
    numbers_required = int(input("How many numbers would you like to generate?: "))
if level == 3:
    symbols_required = int(input("How many symbols would you like to generate?: "))


password = ''
for i in range(letters_required):
    char = random.choice(letters)
    password += char
for i in range(numbers_required):
    char = str(random.choice(numbers))
    password += char
for i in range(symbols_required):
    char = random.choice(symbols)
    password += char


password_list = list(password)
random.shuffle(password_list)


shuffled_password = ''
for char in password_list:
    shuffled_password += char

print("\n✅ Your generated password is:", shuffled_password)
