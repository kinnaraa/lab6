# Kinnara Bosworth
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encoder(string):
    encoded = []
    for char in string:
        encoded.append(int(char)+3)
    new_encoded = ""
    for num in encoded:
        new_encoded += str(num)
    return new_encoded


def main():
    option = ""
    while option != 3:
        print_menu()
        print()
        option = int(input("Please enter an option: "))
        if option == 1:
            string = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        elif option == 2:
            print(f"The encoded password is {encoder(string)}, and the original password is {string}.")
        elif option == 3:
            break
        print()


if __name__ == "__main__":
    main()