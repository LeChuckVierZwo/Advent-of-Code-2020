PasswordList = []
allowedPasswords = 0

with open("Passwords") as f:
    PasswordList = list(f.readlines())

"""
for i in PasswordList:
    current_password = i.split()
    minCount = current_password[0].split("-")[0]
    maxCount = current_password[0].split("-")[1]
    letter = current_password[1][0]
    count = 0
    for i in current_password[2]:
        if i == letter:
            count += 1

    if count <= int(maxCount) and count >= int(minCount):
        allowedPasswords += 1
"""

for i in PasswordList:
    current_password = i.split()
    minCount = current_password[0].split("-")[0]
    maxCount = current_password[0].split("-")[1]
    letter = current_password[1][0]
    valid = 0
    password_code = current_password[2]
    if password_code[int(minCount)-1] == letter:
        valid += 1
    if password_code[int(maxCount)-1] == letter:
        valid += 1

    if valid == 1:
        allowedPasswords += 1

print(allowedPasswords)