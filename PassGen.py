import random
import string   

def menu():
    while True:
        print(" _____               _____            ")
        print("|  __ \             / ____|           ")
        print("| |__) |_ _ ___ ___| |  __  ___ _ __  ")
        print("|  ___/ _` / __/ __| | |_ |/ _ \ '_ \ ")
        print("| |  | (_| \__ \__ \ |__| |  __/ | | |")
        print("|_|   \__,_|___/___/\_____|\___|_| |_|")
    
        print("\nHow long should the password be? \n")
        try:
            input1 = int(input(">_ "))
        except ValueError:
            print("Unvalid lenght, try again")
            continue
        else:
            return input1

def printPwd():
    print(f"\nGenerated a {inputLenght} characters long password: \"{pwd}\" ")



while True:
    inputLenght = menu()

    letters = string.ascii_letters
    digits = string.digits
    spechars= string.punctuation

    charSet = letters + digits + spechars

    pwd = ''
    for i in range(inputLenght):
        pwd += ''.join(random.choice(charSet))

    printPwd()
    
    run_again = input("Do you want to run again? (y/n): ")
    if run_again.lower() != "y":
        break 