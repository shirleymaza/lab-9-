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

#my code
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    

def main():
    while True:
        menu()
        option = input("Please enter an option: ")
        if option == '1':
            password = input("Please enter your password to encode: ")
            new = encode(password)
            print("Your password has been encoded and stored!")
        elif option == '2':
            print(f"The encoded password is {new}, and the original password is {password}.")
        elif option == '3':
            break


if __name__ == "__main__":
    main()