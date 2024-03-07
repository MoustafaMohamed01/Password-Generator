import string
import random

lower_case = list(string.ascii_lowercase)
upper_case = list(string.ascii_uppercase)
digits = list(string.digits)
punctuation = list(string.punctuation)


character_number = input("Enter how many characters for password: ")

while True:
    try:
        character_number = int(character_number)
        if character_number < 6:
            print("You need at least 6 characters")
            character_number = input("Enter how many characters for password: ")
        
        else:
            break
    
    except:
        print("Enter numbers only")
        character_number = input("Enter how many characters for password: ")


part1 = round(character_number * (30/100))
part2 = round(character_number * (20/100))

password = []

for i in range(part1):
    password.append(lower_case[i])
    password.append(upper_case[i])

for i in range(part2):
    password.append(digits[i])
    password.append(punctuation[i])

random.shuffle(password)

password = "".join(password[0:])

print(password)



