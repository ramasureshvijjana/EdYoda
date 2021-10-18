
# This function works for taking an option selecting from used what they want to do.
def options():
    
    # Displaying options to end-user.
    print('\n1. Show the seets \n2. Buy a ticket \n3. Statistics \n4. Show booked tickets for user info \n0. Exit\n')
    
    #  Took this inner function for doing recursion when it raise the exception.
    #  Whenever it raises the exception I want to run the code from the try block. I won't print the above options massage. 
    #  If it raises the exception I call the inner function to repeat the process until the user gives a correct option.
    def take_option():
        
        try:
            # Taking an option from the user.
            option = int(input('Select your option:'))
            print()
            if option not in [1, 2, 3, 4, 0]:
                
                # I raise the exception when user input not in [1, 2, 3, 4, 0]
                raise Exception('Error: Please select correct option should be in [1, 2, 3, 4, 0].')
                
        # If the user does not give int values then it will handle that exception.       
        except ValueError as e:
            print('Error: please enter integer values only.')
            take_option()
            
        # If the user input not in [1, 2, 3, 4, 0] then it will handle that exception. 
        except Exception as e:
            print(e)
            take_option()
            
        # return the valu to below line.
        return option
            
    return take_option()