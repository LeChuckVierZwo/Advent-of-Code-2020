import re

with open("passports") as f:
    passports = f.read().split("\n\n")

valid = 0
valid_content = 0

def check_height(s):
    height = re.match(r"^(\d{1, })(cm|in)$", s)
    if height:
        if height[2] == "cm" and 150 <= int(height[1]) <= 193:
            return True
        elif height[2] == "in" and 59 <= int(height[1]) <= 76:
            return True
    return False


for passport in passports:
    current_passport = passport.replace("\n", " ")
    passport_content = {"byr" : lambda s: len(s) == 4 and 1920 <= int(s) <= 2002,
                        "iyr" : lambda s: len(s) == 4 and 2010 <= int(s) <= 2020,
                        "eyr" : lambda s: len(s) == 4 and 2020 <= int(s) <= 2030,
                        "hgt" : check_height,
                        "hcl" : lambda s: re.match(r"#[a-f0-9]{6}", s),
                        "ecl" : lambda s: s in ["amb", "blu", "brn", "gry", "grn", "hlz", "oth"],
                        "pid" : lambda s: len(s) == 9 and s.isdigit()
                        }
    valid_passport = False
    for content in passport_content:
        if content in current_passport:
            valid_passport = True
            fun = passport_content[content]
            if fun():
                valid += 1
                valid_passport = False
        else:
            valid_passport = False
            break
    if valid_passport:
        valid += 1

print(valid)