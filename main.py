# main.py
from account_ops import create_account
from transactions import deposit, withdraw, check_balance, view_history

def show_menu():
    print("\n----------- BANKING SYSTEM -----------")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. View Transaction History")
    print("6. Exit")
    print("---------------------------------------")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            view_history()
        elif choice == "6":
            print("Thank you for using the Banking System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
