
# This function works for show the statistical information.
def statistics(total_bookings, rows, clms, current_inc):
    
    # Print total seat bookings
    print('Number of purchased tickets:', total_bookings)
    
    # Calculating total seats
    total_seats = rows * clms
    print('Percentage:', (total_bookings / total_seats) * 100 )
    
    # Calculating current income
    print('Current income:', current_inc)
    
    #### Calculating Total income ####
    
    total_inc = 0
    # Finding middle row for cost confirmation.
    half_st_posn = int(rows / 2)

    # Logic for find total income       
    if total_seats > 60:
        total_inc = (half_st_posn * clms * 10) + ((rows - half_st_posn) * clms * 8)
    else:
        total_inc = total_seats * 10
        
    print('Total income:', total_inc)