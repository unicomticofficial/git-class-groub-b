balance = 50000

def withdraw():
    global balance
    amount = int(input('Enter Amount: '))
    balance = balance - amount
    print('Withdraw Amount: ', amount)
    print('New Balance', balance)

withdraw()

print(balance)

