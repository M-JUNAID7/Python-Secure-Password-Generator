import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("Welocme to Password Genetator")
n_letters = int(input("How many letter you want in your password : "))
n_numbers = int(input("How many numbers you need in you password : "))
n_symbols = int(input("How many symbols you need in your password : "))

password = []

for i in range(n_letters):
    char = random.choice(letters)
    password.append(char) 

for i in range(n_numbers):
    numbe = random.choice(numbers)
    password.append(numbe)

for i in range(n_symbols):
    symb = random.choice(symbols)
    password.append(symb)
   
random.shuffle(password)



final_password = ""
for i in password:
    final_password += i
print(f"Your Password is :  {final_password} ")    
