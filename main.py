import random

email = "54999ralston@mustangps.org" #I have permission to use this email

number1 = (1,2,3,4,5,6,7,8,9)
number2 = (1,2,3,4,5,6,7,8,9)
number3 = (1,2,3,4,5,6,7,8,9)

Uppercase = ("A","B","C","D","E","F","G","H",
             "I","J","K","L","M","N","O","P",
             "Q","R","S","T","U","V","W","X","Y","Z")

lowercase1 = ("a","b","c","d","e","f","g","h",
              "i","j","k","l","m","n","o","p",
              "q","r","s","t","u","v","w","x","y","z")

lowercase2 = ("a","b","c","d","e","f","g","h",
              "i","j","k","l","m","n","o","p",
              "q","r","s","t","u","v","w","x","y","z")

number4 = (1,2,3,4,5,6,7,8,9)

special = ("!","@","#","$","%","^","&","*","(",")","-","_")

def generate_password(): 
    password = str(random.choice(number1)) + \
               str(random.choice(number2)) + \
               str(random.choice(number3)) + \
               random.choice(Uppercase) + \
               random.choice(lowercase1) + \
               random.choice(lowercase2) + \
               str(random.choice(number4)) + \
               random.choice(special)

    return password

# Read the contents of passwords.txt into the dictionary variable
with open("dictionary.txt", "r") as file:
    dictionary_contents = file.read().splitlines()

# Generate 10 passwords and add them to the output list
output_list = []
for _ in range(20000):
    output_list.append(generate_password())

# Add dictionary contents to the output list
output_list.extend(dictionary_contents)

# Shuffle the output list
random.shuffle(output_list)

# Print shuffled passwords
for item in output_list:
    print(item)