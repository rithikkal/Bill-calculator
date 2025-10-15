def calculate_return(total_bill, amount_paid):
    # calculate balance to return
    return amount_paid - total_bill

# main program
bill = 2.50
paid = 4.00

# call the function and store the returned value
balance = calculate_return(bill, paid)

# display the result
print("The shopkeeper should return $", balance)