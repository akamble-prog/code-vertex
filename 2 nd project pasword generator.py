import random                       #we have imported random for randomizing the order of chracters used in password 
import string                        # string module has the digits , special symbols and  many more

def password():
    while True:
        try:
            s1 = string.ascii_uppercase      #we used this to use uppercase letters for password
            s2 = string.ascii_lowercase       #we used this to use lowercase letters for password
            digits = string.digits             #we used this to use numbersn (0-9) for password
            special_symbols = string.punctuation     #we used punctualtion to use special symblos  for password

            # Combine all the string functions into one list
            main_s=[]                       # we have defined a empty list where all the functions merege 
            main_s.extend(list(s2))

            main_s.extend(list(digits))

            main_s.extend(list(special_symbols))

            random.shuffle(main_s)    #random.shuffle is function from random module which helps us to mix all the characters in string


         

            while True:
                try:
                    plen = input("Enter the length of the password to be generated: ")               # to take input of user 
                    if plen.isdigit():                                            #to handle correction
                        plen = int(plen)                
                        break
                    else:
                        print("Invalid input. Please enter a valid positive integer.")
                except ValueError:
                    print("Invalid input. Please enter a valid positive integer.")

            random.shuffle(main_s)                                                 # random.shuffle will shuffle all   the characters in the list
            print("Here's a new password for you:")
            print("".join(main_s[0:plen]))

            # the following block is for regenerating the password again and again

            restart = input("Generate another password? (yes/no): ")
            if restart.lower() != "yes":
                print("Thank you for using the password generator. Have a great day!")
                break

        except KeyboardInterrupt:
            print("\nOperation aborted. Have a good day!")
            break

# Call the password function
password()
