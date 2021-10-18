import seats_arrangement as sa
import select_option as so
import book_ticket as bt
import statistics as stcs
import show_booked_ticket as sbt


# # Define required global variables.
# total_bookings = 0
# current_inc = 0
# cstmr_dtls = dict()


# This function for display the seats formation
def show_seets(df):
    
    print(f'\n\n{df}')


# This function works for calling particular function based on user option
def set_option(option, df, rows, clms, total_bookings, current_inc, cstmr_dtls):

    if option == 1:
        show_seets(df)
    elif option == 2:
        bt.buy_ticket(rows, clms, df)
    elif option == 3:
        stcs.statistics(total_bookings, rows, clms, current_inc)
    elif option == 4:
        sbt.show_booked_ticket(cstmr_dtls)



if __name__ == '__main__':
    print('WellcomeS')
    rows, clms, df = sa.seats_setting()

    # Infinity loop runs till user select 0.
    while True:
        option = so.options()
        set_option(option, df, rows, clms, bt.total_bookings, bt.current_inc, bt.cstmr_dtls)
        if option == 0:
            print('\n===========================================\nThank you for Visit. Wish you visit again.')
            print('===========================================')
            break


