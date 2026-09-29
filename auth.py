# auth.py
import state

def login():
    try:
        account_number = int(input("Enter your account number: "))
    except ValueError:
        print("Invalid account number.")
        return None
    
    if account_number not in state.accounts:
        print("Account not found.")
        return None
    
    pin = input("Enter your PIN: ")
    if state.accounts[account_number]["pin"] != pin:
        print("Incorrect PIN.")
        return None
        
    return account_number
