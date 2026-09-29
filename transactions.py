# transactions.py
import state
from auth import login

def deposit():
    account_number = login()
    if account_number is None:
        return
    try:
        amount = float(input("Enter amount to deposit: "))
    except ValueError:
        print("Invalid amount.")
        return
    if amount <= 0:
        print("Amount must be positive.")
        return
        
    state.accounts[account_number]["balance"] += amount
    state.accounts[account_number]["history"].append(f"Deposited: +{amount}")
    print(f"Deposited {amount}. New balance: {state.accounts[account_number]['balance']}")

def withdraw():
    account_number = login()
    if account_number is None:
        return
    try:
        amount = float(input("Enter amount to withdraw: "))
    except ValueError:
        print("Invalid amount.")
        return
    if amount <= 0:
        print("Amount must be positive.")
        return
        
    current_balance = state.accounts[account_number]["balance"]
    if amount > current_balance:
        print("Insufficient balance.")
        return
        
    state.accounts[account_number]["balance"] -= amount
    state.accounts[account_number]["history"].append(f"Withdrew: -{amount}")
    print(f"Withdrew {amount}. New balance: {state.accounts[account_number]['balance']}")

def check_balance():
    account_number = login()
    if account_number is None:
        return
        
    name = state.accounts[account_number]["name"]
    balance = state.accounts[account_number]["balance"]
    print(f"\nAccount Holder: {name}")
    print(f"Account Number: {account_number}")
    print(f"Current Balance: {balance}")

def view_history():
    account_number = login()
    if account_number is None:
        return
        
    history = state.accounts[account_number]["history"]
    if len(history) == 0:
        print("No transactions found.")
        return
        
    print(f"\n--- Transaction History for Account {account_number} ---")
    for index, transaction in enumerate(history, start=1):
        print(f"{index}. {transaction}")
