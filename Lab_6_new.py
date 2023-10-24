def encode_password(password):
    encoded_password = ""
    for digit in password:
        new_digit = str((int(digit) + 3) % 10)
        encoded_password += new_digit
    return encoded_password

def decode_password(password):
    decoded_password = ""
    for digit in password:
        new_digit=str((int(digit)-3)%10)
        decoded_password+=new_digit
    return decoded_password

def main():
    while True:
        print("Menu")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print("Your password has been encoded and stored!")
        elif choice == "2":
            password = input("Please enter your password to decode: ")
            decoded_password=decode_password(password)
            print("Your password has been decoded and stored!")
        elif choice == "3":
            break


if __name__ == '__main__':
    main()
