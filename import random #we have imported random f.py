import random
import string

def password():
    while True:
        try:
            s1 = string.ascii_uppercase
            s2 = string.ascii_lowercase
            digits = string.digits
            special_symbols = string.punctuation

            # Combine all the string functions into one list
            main_s = list(s1) + list(s2) + list(digits) + list(special_symbols)

            while True:
                try:
                    plen = input("Enter the length of the password to be generated: ")
                    if plen.isdigit():
                        plen = int(plen)
                        break
                    else:
                        print("Invalid input. Please enter a valid positive integer.")
                except ValueError:
                    print("Invalid input. Please enter a valid positive integer.")

            random.shuffle(main_s)
            print("Here's a new password for you:")
            print("".join(main_s[:plen]))

            restart = input("Generate another password? (yes/no): ")
            if restart.lower() != "yes":
                print("Thank you for using the password generator. Have a great day!")
                break

        except KeyboardInterrupt:
            print("\nOperation aborted. Have a good day!")
            break

# Call the password function
password()
