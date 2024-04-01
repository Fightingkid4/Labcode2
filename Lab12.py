# 1
name = input("What is your name? ")
print(name.lower())
print(name.upper())
print(name.capitalize())

# 2
password = ""

while password.lower() != "secret":
    password = input("Password: ")
else:
    print("You got it!")

# 3
while True:
    password = input("Password: ")
    x = 0
    y = 0
    for i in password:
        if i.isalpha():
            x = x + 1
        elif i.isdecimal():
            y = y + 1
            
    if x >= 6 and y >= 2:
        print("Accepted")
        break
# 4
phrase = input("Please enter a phrase: ")

phrase_edit1 = phrase.replace("o", "0")
phrase_edit2 = phrase_edit1.replace("e", "3")
phrase_edit3 = phrase_edit2.replace("i", "1")
phrase_edit4 = phrase_edit3.replace("t", "7")

print(phrase_edit4, end=".")