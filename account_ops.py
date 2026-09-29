# account_ops.py
import state

def create_account():
    name = input("Enter your name: ")
    pin = input("Set a 4-digit PIN: ")
    
    account_number = state.next_account_number
    state.next_account_number += 1
    
    state.accounts[account_number] = {
        "name": name,
        "pin": pin,
        "balance": 0,
        "history": []
    }
    state.accounts[account_number]["history"].append("Account created")
    
    print("\nAccount created successfully!")
    print(f"Your account number is: {account_number}")
    print("Please remember this number along with your PIN.")
