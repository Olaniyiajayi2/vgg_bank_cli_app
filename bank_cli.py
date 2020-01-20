## This is a python app for bank operation
print('Welcome!!!, Please respond to the following prompt')

dict_1 = {'create accont': 1, 'transaction': 2}
def what_to_do():
    global dict_1
    print('Press 1 to create an account')
    print('Press 2 to perform a transaction')
    action = eval(input('>>>'))
    return action

response_1 = what_to_do()

balance = 0.0

database = {'Olaniyi': {'Email':'ajayiolaniyi@hotmail.com', 'Password': 123456, 'Balance': 135},
            'Tobi': {'Email': 'olaniyi@gmail.com', 'Password': 263528, 'Balance': 230}}

def create_account():
    global database
    print('Please create a user account')
    username = input('Enter username: ')
    email = input('Enter your email address: ')
    if '@' not in email or '.com' not in email:
        print('Email address not valid')
        create_account()
    else:
        password = input('Enter a strong password:')
        database[username] = {'Email':email, 'Password':password, 'Balance':balance}
        print('Congrats!! You have created an account')
        print('Press 1 To perform  a transaction or 2 to cancel')
        action = eval(input('>>>'))
        if action == 1:
            transaction()
        else:
            print('Thank you for banking with us')


def balance():
    print('Enter usernme to continue:')
    name = input('>>>')
    balance = database[name]['Balance']
    print('Your account balance is {}'.format(balance))
    print('Press 1 to perform another transaction')
    print('Press any key to exit')
    action_ = eval(input('>>>'))
    if action_ == 1:
        transaction()
    else:
        print('Thank you for banking with us')

def deposit():
    print('Enter usernme to continue:')
    name = input('>>>')
    print('Please enter the amount you want to deposit')
    amount = eval(input('>>>'))
    database[name]['Balance'] += amount
    print('You have deposited {} into your account, your new balance is {}'.format(amount, database[name]['Balance']))
    print('Press 1 to perform another transaction')
    print('Press any key to exit')
    action_ = eval(input('>>>'))
    if action_ == 1:
        transaction()
    else:
        print('Thank you for banking with us')


def withdrawal():
    print('Enter Username to continue:')
    name = input('>>>')
    print('Please enter the amount you want to withdraw')
    amount = eval(input('>>>'))
    if amount > database[name]['Balance']:
        print('You do not have sufficient balance, please deposit')
        print('Press 1 to deposit')
        print('Press 2 to exit')
        action_5 = eval(input('>>>'))
        if action_5 == 1:
            deposit()
        else:
            transaction()
    elif amount < database[name]['Balance']:
        print('You have withdran {}, thank you for banking with us.'.format(amount))
        print('thank you for banking with us, your balace is {}'.format(database[name]['Balance'] - amount))
        print('Press 1 to perform another transaction')
        print('Press any key to exit')
        action_ = eval(input('>>>'))
        if action_ == 1:
            transaction()
        else:
            print('Thank you for banking with us')

def transfer():
    print('Enter username to continue:')
    name = input('>>>')
    print('Enter recipient email address')
    rep_email = input('>>>')
    print('Enter amount to transfer')
    amount = eval(input('>>>'))
    if amount > database[name]['Balance']:
        print('Insufficient funds')
        transaction()
    elif amount < database[name]['Balance']:
        print('Congratulations, you have sent {} to {}, your balance is {}'.format(amount, rep_email, database[name]['Balance'] - amount))
        print('Press 1 to perform another transaction')
        print('Press any key to exit')
        action_ = eval(input('>>>'))
        if action_ == 1:
            transaction()
        else:
            print('Thank you for banking with us')


def transaction():
    global database
    print('Enter username')
    name = input('>>>')
    print('Enter password')
    action_3 = eval(input('>>>'))
    if name in database and action_3 == database[name]['Password']:
        print('Press 1 for Balance')
        print('Press 2 for deposit')
        print('Press 3 for withdrawal')
        print('Press 4 for transfer')
        action_4 = eval(input('>>>'))
        if action_4 == 1:
            balance()
        elif action_4 == 2:
            deposit()
        elif action_4 == 3:
            withdrawal()
        elif action_4 == 4:
            transfer()
    else:
        print("Incorrect Username or Password, please input a valid password")
        transaction()
    return name



if response_1 == 1:
    create_account()
else:
    transaction()
