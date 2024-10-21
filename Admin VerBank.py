import random
import platform
import os
import sys
import colorama
from colorama import Fore, Back, Style
import time
import random

platform = platform.system()
version = "1.0.2"

title_core = '''
__     __        ____              _         _       _           _       
\ \   / /__ _ __| __ )  __ _ _ __ | | __    / \   __| |_ __ ___ (_)_ __  
 \ \ / / _ \ '__|  _ \ / _` | '_ \| |/ /   / _ \ / _` | '_ ` _ \| | '_ \ 
  \ V /  __/ |  | |_) | (_| | | | |   <   / ___ \ (_| | | | | | | | | | |
   \_/ \___|_|  |____/ \__,_|_| |_|_|\_\ /_/   \_\__,_|_| |_| |_|_|_| |_|
                       VerBank Admin Control Panel                                                

This is not a real bank :v, it just a bank system simulation 
Developer : yrvrmth00
Github    : github.com/yrvrmth00
Lynk.id   : lynk.id/yourvermouth
'''
colorama.init()

database = 'db.txt'
transactions_db = 'transactions.txt'

os.system('cls||clear')
print('''VerBank-Admin-Control-Panel [Version '''+version+'''] - Platform '''+platform+'''   ''')
print(Fore.LIGHTBLUE_EX + title_core + Fore.LIGHTWHITE_EX)
database = 'db.txt'

def read_existing_account_numbers(database):
    account_numbers = set()
    with open(database, 'r') as file:
        for line in file:
            data = line.strip().split('|')
            if len(data) == 4:
                account_numbers.add(data[2])
    return account_numbers

def generate_unique_account_number(existing_numbers):
    while True:
        account_number = ''.join(random.choices('0123456789', k=10))
        if account_number not in existing_numbers:
            return account_number

def create_account(name, pin, account_number, balance):
    with open(database, 'a') as file:
        file.write(f"{name}|{pin}|{account_number}|{balance}\n")
    print("\n\n\nINFO: Account successfully created!")
    
    print(f'''================================= Account Information ==================================
              
Account Number : {account_number}
User Name      : {name}
PIN            : {pin}
Opening Balance: ${balance}
========================================================================================''')

def main():
    sys.stdout.write("\x1b]2;VerBank Admin Control Panel\x07")
    sys.stdout.flush()
    existing_account_numbers = read_existing_account_numbers(database)
    new_account_number = generate_unique_account_number(existing_account_numbers)
    
    print("\n\n\n")
    print("====================================== Create Account ======================================")
    print(f'''User Account Number:
 {new_account_number}
''')
    user = input("New User: ")
    userpin = input("User PIN: ")
    opening_balance = input("Opening Balance: ")
    
    create_account(user, userpin, new_account_number, opening_balance)

    input("Press 'ENTER' to continue!")
    main()

if __name__ == "__main__":
    main()
