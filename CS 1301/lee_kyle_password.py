def better_password(password):
    replace = {
        "o" : '0',
        "i" : '1',
        'a' : '@',
        'e' : '3',
        'A' : '4',
        'B' : '8',
        's' : '$',
    }
    stronger_password = ''
    for char in password:
        if char in replace:
            stronger_password += replace[char]
        else:
            stronger_password += char
    stronger_password += '!'
    return stronger_password

enter_password = input("Please Enter Your Password: ")
new_password = better_password(enter_password)
print("Your new strong password is:", new_password)    