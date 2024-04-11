# Bailey Watkins
def encode(password):
    encoded_password = ""
    for char in password:
        newchar = str(int(char) + 3)
        encoded_password += str(int(newchar) % 10)
    return encoded_password
    
#Katarina Neal(added decoder)
def decoder(password):
    result = ''
    for digit in password:
        new_digit = str((int(digit) - 3) % 10)
        result += new_digit
    return result
    
