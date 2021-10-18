import start as st

# Define required global variables.
total_bookings = 0
current_inc = 0
cstmr_dtls = dict()


def buy_ticket(rows, clms, df):
    
    try:
        print(f'Instruction : Row value must be less than {rows} and column value should be less than {clms}')
        row = int(input('Please Enter row Number: '))
        clm = int(input('Please Enter columns Number: '))

        if row > rows and clm > clms:
            raise Exception(f'Error: row value must be < {rows} and column value should be < {clms}')
    except ValueError as e:
        print('Error: please enter integer values only.')
        buy_ticket(rows, clms, df)
    except Exception as e:
        print(e)
        buy_ticket(rows, clms, df)

    if df[clm][row] == 'S':

        cost = 0
        half_st_posn = int(rows / 2)
        total_seats = rows * clms
        global current_inc, total_bookings 
        if total_seats > 60:
            if row <= half_st_posn:
                current_inc += 10
                cost = 10
            else:
                current_inc += 8
                cost = 8
        else:
            current_inc += 10
            cost = 10

        print(f'The price of the seat is: $ {cost}  Are you sure want to book ticket. Type Yes or No')
        

        if final_decition():

            name = input("Please enter your name: ")
            gender = input("Please enter your gender: ")
            age = input("Please enter your age: ")
            phone_no = input("Please enter your phone number: ")

            global cstmr_dtls
            cstmr_dtls['name'] = name
            cstmr_dtls['gender'] = gender
            cstmr_dtls['age'] = age
            cstmr_dtls['phone_no'] = phone_no
            cstmr_dtls['ticket_cost'] = cost

            df[clm][row] = 'B'
            total_bookings += 1
            print('\n===================================================\n')
            print(f'Congratulations...!! {name}. Your ticket booked successfully.\nYour Seet Number: ({row}-{clm})')
            print('\n===================================================\n')

            st.show_seets(df)
        else:
            pass

    elif df[clm][row] == 'B':
        print('Error: Your selection already booked. Please select another seet.')
        buy_ticket(rows, clms, df)



def final_decition():

    decition = input().upper()

    try:

        if decition in ['YES', 'NO']:
            if decition == 'YES':
                return True
            else:
                return False
        else:
            raise ValueError('ERROR: Your value should be in [YES, NO]')

    except ValueError as e:
        print(e)
        final_decition()
