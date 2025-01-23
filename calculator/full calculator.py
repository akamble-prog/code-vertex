    #I am going to make a simple calculator

    #to perfrom simple arthimatic calculations



def main():
 while True:
    try:

        

        num1=float(input("Enter a number:"))         # we are using num1 as variable to store the 1st value of user input
        num2=float (input("Enter an another number:"))  # we are using num2 as variable to store the 2nd value of user input

        operations=input("Enter arithimatic fucntions(+,*,/,-)")  


            # now to switch between operations we will use conditons 

        if operations=="+":

         print("The addition between given numbers is :",num1+num2)   # it will print the addition

        elif operations=="-":
            print("The subtraction between given number is  :",num1-num2)  # it will print subtraction

        elif operations=="*":
            print("The multiplycation between given numbers is :",num1*num2) # it will print multiplycation

        elif operations=="/":

         if num2!=0:
             print("The division between given numbers is:",num1/num2) # it will print division
         else:
            print("Error: Division by zero is not allowed.")  # if any number is divided by zero this error will be thrown
                    
    except ValueError:   # it will be used to handel invalid inputs by user
     print("Option choosed is invalid")
    print("Please choose a valid option  ")

     # and the following code of block will restart the enitire code multiple times
    restart=input("Do you want to start another instance?, yes or no:").lower()
    if restart.lower() != "yes":
        print("thank you for using calculator")
        break
       
if __name__=="__main__":    

 main()

