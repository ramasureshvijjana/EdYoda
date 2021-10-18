
# It show the recently booked ticket details
def show_booked_ticket(cstmr_dtls):
    print('Name: ', cstmr_dtls.get('name'))
    print(f'Gender: ', cstmr_dtls.get('gender'))
    print(f'Age: ', cstmr_dtls.get('age'))
    print(f'Ticket Price: $', cstmr_dtls.get('ticket_cost'))
    print(f'Phone no: ', cstmr_dtls.get('phone_no'))