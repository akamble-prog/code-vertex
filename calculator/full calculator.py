    #I am going to make a simple calculator

    #to perfrom simple arthimatic calculations



def main():
 while True:
    try:

        

        num1=float(input("Enter a number:"))         # we are using num1 as variable to store the 1st value of user input
        num2=float (input("Enter an another number:"))  # we are using num2 as variable to store the 2nd value of user input

        operations=input("Enter arithimatic fucntions(+,*,/,-)")  


            # now to switch between operations we will use loops 

        if operations=="+":

         print("The addition between given numbers is :",num1+num2)

        elif operations=="-":
            print("The subtraction between given number is  :",num1-num2)

        elif operations=="*":
            print("The multiplycation between given numbers is :",num1*num2)

        elif operations=="/":

         if num2!=0:
             print("The division between given numbers is:",num1/num2)
         else:
            print("Error: Division by zero is not allowed.")
                    
    except ValueError:
     print("Option choosed is invalid")
    print("Please choose a valid option  ")
     
    restart=input("Do you want to start another instance?, yes or no:").lower()
    if restart.lower() != "yes":
        print("thank you for using calculator")
        break
       
if __name__=="__main__":    

 main()

