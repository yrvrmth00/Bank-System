import platform
import os
import sys
import colorama
from colorama import Fore, Back, Style
import time
import random

platform = platform.system()
version = "1.0.0"

title_core = '''
 $$$$$$\  $$\           $$\                           $$$$$$$\                      $$\       
$$  __$$\ $$ |          $$ |                          $$  __$$\                     $$ |      
$$ /  \__|$$ | $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  $$ |  $$ | $$$$$$\  $$$$$$$\  $$ |  $$\ 
$$ |$$$$\ $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$$$$$$\ | \____$$\ $$  __$$\ $$ | $$  |
$$ |\_$$ |$$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$$$$$$$ |$$  __$$\  $$$$$$$ |$$ |  $$ |$$$$$$  / 
$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$   ____|$$ |  $$ |$$  __$$ |$$ |  $$ |$$  _$$<  
\$$$$$$  |$$ |\$$$$$$  |$$$$$$$  |\$$$$$$$\ \$$$$$$$\ $$$$$$$  |\$$$$$$$ |$$ |  $$ |$$ | \$$\ 
 \______/ \__| \______/ \_______/  \_______| \_______|\_______/  \_______|\__|  \__|\__|  \__|

This is not a real bank :v, it just a bank system simulation 
Developer : maleclouds
Github    : github.com/maleclouds
Lynk.id   : lynk.id/maleclouds
Developer Note:
Maybe next time i will change the database from txt to SQL
'''
title_global = '''
 $$$$$$\  $$\           $$\                           $$$$$$$\                      $$\       
$$  __$$\ $$ |          $$ |                          $$  __$$\                     $$ |      
$$ /  \__|$$ | $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  $$ |  $$ | $$$$$$\  $$$$$$$\  $$ |  $$\ 
$$ |$$$$\ $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$$$$$$\ | \____$$\ $$  __$$\ $$ | $$  |
$$ |\_$$ |$$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$$$$$$$ |$$  __$$\  $$$$$$$ |$$ |  $$ |$$$$$$  / 
$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$   ____|$$ |  $$ |$$  __$$ |$$ |  $$ |$$  _$$<  
\$$$$$$  |$$ |\$$$$$$  |$$$$$$$  |\$$$$$$$\ \$$$$$$$\ $$$$$$$  |\$$$$$$$ |$$ |  $$ |$$ | \$$\ 
 \______/ \__| \______/ \_______/  \_______| \_______|\_______/  \_______|\__|  \__|\__|  \__|
==============================================================================================
'''

colorama.init()

database = 'db.txt'
transactions_db = 'transactions.txt'

os.system('cls||clear')
print('''GlobeeBank [Version '''+version+'''] - Platform '''+platform+'''   ''')
print(Fore.LIGHTGREEN_EX + title_core)

def read_existing_accounts(database):
    accounts = []
    with open(database, 'r') as file:
        for line in file:
            data = line.strip().split('|')
            if len(data) == 4:
                accounts.append({
                    'name': data[0],
                    'pin': data[1],
                    'account_number': data[2],
                    'balance': float(data[3])
                })
    return accounts

def write_accounts(database, accounts):
    with open(database, 'w') as file:
        for account in accounts:
            file.write(f"{account['name']}|{account['pin']}|{account['account_number']}|{account['balance']}\n")

def find_account_by_account_number(accounts, account_number):
    for account in accounts:
        if account['account_number'] == account_number:
            return account
    return None

def log_transaction(transaction_type, from_account, to_account, amount):
    with open(transactions_db, 'a') as file:
        file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}|{transaction_type}|{from_account}|{to_account}|{amount}\n")

def read_transaction_logs(account_number):
    transactions = []
    with open(transactions_db, 'r') as file:
        for line in file:
            data = line.strip().split('|')
            if len(data) == 5:
                if data[2] == account_number or data[3] == account_number:
                    transactions.append({
                        'date': data[0],
                        'type': data[1],
                        'from': data[2],
                        'to': data[3],
                        'amount': float(data[4])
                    })
    return transactions

def transfer_funds(from_account_number, pin, to_account_number, amount):
    accounts = read_existing_accounts(database)
    
    from_account = find_account_by_account_number(accounts, from_account_number)
    to_account = find_account_by_account_number(accounts, to_account_number)
    
    if from_account and to_account:
        if from_account['pin'] == pin:
            if from_account['balance'] >= amount:
                from_account['balance'] -= amount
                to_account['balance'] += amount
                write_accounts(database, accounts)
                log_transaction("TRANSFER", from_account_number, to_account_number, amount)
                print("Transfer successful!")
                print(f"New balance for {from_account['name']}: {from_account['balance']}")
                print(f"New balance for {to_account['name']}: {to_account['balance']}")
            else:
                print("Insufficient balance to perform the transfer.")
        else:
            print("Incorrect PIN.")
    else:
        print("One or both account numbers are invalid. Please check and try again.")

def main_home(username, account_number, balance):
    os.system('cls||clear')
    print('''GlobeeBank-Account [Version '''+version+'''] - Platform '''+platform+'''   ''')
    print(Fore.LIGHTGREEN_EX + title_global + Fore.LIGHTWHITE_EX)
    def verif(username):
        
        
        with open(database, 'r') as file:
            for line in file:
                data = line.strip().split('|')
                if len(data) == 4:
                    if data[0] == username:
                        verified = True
                        
                        
                        account_number = data[2]
                        balance = float(data[3])
                        break
        
        if verified:
            main_home(username, account_number, balance)
        else:
            print("INFO: Error")
            time.sleep(2)
            main_login()

    username = username
    
    balancef = "{:,.2f}".format(balance)
    print(f''' Hi {username}!

 Account Number:
 ''' + Fore.LIGHTYELLOW_EX + account_number + Fore.LIGHTWHITE_EX + '''

 Balance:
 ''' + Fore.LIGHTGREEN_EX  + f'''${balancef}''' + Fore.LIGHTWHITE_EX + '''

 Menu:
 1. Transfer
 2. Pay Tax
 3. E-Toll
 4. Invest
 5. View Transaction Logs
 6. Logout

''')
    home_input = input(': ')

    if home_input == '1':
        from_account_number = account_number  # use the current user's account number
        pin = input("Enter your PIN: ")
        to_account_number = input("Enter recipient's account number: ")
        amount = float(input("Enter amount to transfer: "))
        transfer_funds(from_account_number, pin, to_account_number, amount)
        time.sleep(4)
        verif(username)
        main_home(username, account_number, balance)
    elif home_input == '2':
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        amount = float(input("Enter tax amount: "))
        pay_tax(account_number, pin, amount)
        main_home(username, account_number, balance)
    elif home_input == '3':
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        amount = float(input("Enter e-toll amount: "))
        e_toll(account_number, pin, amount)
        main_home(username, account_number, balance)
    elif home_input == '4':
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        amount = float(input("Enter investment amount: "))
        invest(account_number, pin, amount)
        main_home(username, account_number, balance)
    elif home_input == '5':
        transactions = read_transaction_logs(account_number)
        print("\n====================================== Transaction Logs ======================================")
        for t in transactions:
            print(f"Date: {t['date']}, Type: {t['type']}, From: {t['from']}, To: {t['to']}, Amount: ${t['amount']}")
        input("\nPress ENTER to return to the menu.")
        main_home(username, account_number, balance)
    elif home_input == '6':
        print("Logged out successfully.")
        time.sleep(1)
        main_login()
    else:
        print("Invalid input, please select a valid option.")
        time.sleep(1)
        main_home(username, account_number, balance)

def pay_tax(account_number, pin, amount):
    print("Pay Tax feature is not implemented yet.")

def e_toll(account_number, pin, amount):
    print("E-Toll feature is not implemented yet.")

def invest(account_number, pin, amount):
    print("Invest feature is not implemented yet.")

def main_login():
    print(Fore.RESET)
    os.system('cls||clear')
    print('''GlobeeBank-Login [Version '''+version+'''] - Platform '''+platform+'''   ''')
    print(Fore.LIGHTGREEN_EX + title_global + Fore.LIGHTWHITE_EX)
    print('Protect your personal data, and do not share your account PIN with anyone!')
    print("Input username and PIN")
    global username
    
    def login(username, pin):
        
        found = False
        with open(database, 'r') as file:
            for line in file:
                data = line.strip().split('|')
                if len(data) == 4:
                    if data[0] == username and data[1] == pin:
                        found = True
                        
                        account_number = data[2]
                        balance = float(data[3])
                        break
        
        if found:
            main_home(username, account_number, balance)
        else:
            print("INFO: Incorrect Username or PIN")
            time.sleep(2)
            main_login()

    username = input("Username: ")
    pin = input("PIN: ")
    login(username, pin)

def main_core():
    sys.stdout.write("\x1b]2;GlobeeBank\x07")
    sys.stdout.flush()
    input(Fore.LIGHTWHITE_EX + "Press 'ENTER' to start!")
    print(Fore.RESET)
    os.system('cls||clear')
    print('''GlobeeBank-Terminal [Version '''+version+'''] - Platform '''+platform+'''   ''')
    print(Fore.LIGHTGREEN_EX + title_global + Fore.LIGHTWHITE_EX)
    print(" ===================================== GlobeeBank Terminal =====================================")
    print("INFO: Starting the system...")
    time.sleep(0.2)
    print("INFO: Loading the system...")
    time.sleep(0.6)
    print("INFO: Finding Database "+database)
    def loading_bar(duration):
        for i in range(1, 51):
            sys.stdout.write('\r')
            sys.stdout.write(f'SYS: Loading database [{"-" * i}{" " * (50 - i)}] {i * 2}%')
            sys.stdout.flush()
            time.sleep(duration / 50)

        sys.stdout.write('\n')
        print("INFO: Loading successful!")
    loading_bar(3)
    
    main_login()

main_core()
