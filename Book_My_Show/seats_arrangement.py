import pandas as pd
import numpy as np

# Define seats
def seats_setting():
    try:
        # Taking the number of rows and columns in a hall.
        rows = int(input('Please Enter Number of rows: '))
        clms = int(input('Please Enter Number of columns: '))
    # This exception handle if user alpha data (non-integers)              
    except ValueError as e:
        
        print('Error: please enter integer values only.')
        seats_setting()
    
    # Logic for create seats
    seats = []    
    for row in range(1, rows+1):
        inner_list = []
        for clm in range(1, clms+1):
            inner_list.append('S')
        seats.append(inner_list)
        
    # Convert seats to pandas DataFrame to handle the data of the seats simply.
    df = pd.DataFrame(seats)
    df.index = np.arange(1,rows+1)
    df.columns = np.arange(1,clms+1)
    return rows, clms, df