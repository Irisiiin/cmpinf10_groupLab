def encrypt_name(name, lucky_number):
    encrypted_name = ""
    for char in name:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - 97 + lucky_number) % 25) + 97)
            if char.isupper():
                encrypted_name += shifted_char.upper()
            else:
                encrypted_name += shifted_char
    return encrypted_name

def main():
    name = input("Please enter your nick name: ")
    lucky_number = int(input("Please enter your lucky number(1-10):"))
    if lucky_number < 1 or lucky_number > 10:
        print("The lucky number must be integer in 1-10")
        return
    encrypted_name = encrypt_name(name, lucky_number)
    print("Your encrypted_name is: ", encrypted_name)

if __name__ == "__main__":
    main()
