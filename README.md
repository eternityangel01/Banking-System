# Banking-System
Command-line banking system in Python — account management, deposits/withdrawals/transfers, and transaction history, built with a layered architecture (services + SQLite storage), salted PIN hashing, logging, and unit tests.
# Simple Banking System (Python CLI Project)

A command-line banking system built in Python for a first-semester project.
It allows users to create accounts, deposit and withdraw money, check their
balance, and view transaction history. All data is stored in memory using
Python dictionaries (no external database required).

## Features
- Create a new bank account (auto-generated account number + PIN protection)
- Deposit money into an account
- Withdraw money from an account (with balance check)
- Check current balance
- View full transaction history for an account
- Simple menu-driven command-line interface

## Tech Stack
- Language: Python 3
- No external libraries required (uses only Python's standard built-ins)

## Prerequisites
- Python 3.7 or higher installed on your system

To check if Python is installed, run:
```bash
python3 --version
```
or on Windows:
```bash
python --version
```
If it is not installed, download it from https://www.python.org/downloads/

## How to Run

From the project's root directory, run:
```bash
python3 bank_system.py
```
or on Windows:
```bash
python bank_system.py
```

## Usage

Once the program starts, you'll see a menu like this:

```
----------- BANKING SYSTEM -----------
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. View Transaction History
6. Exit
---------------------------------------
```

- Choose option `1` first to create an account. You'll be given an
  account number — remember it along with your PIN.
- Use options `2`–`5` to perform operations on your account (you'll be
  asked to log in with your account number and PIN each time).
- Choose option `6` to exit the program.

**Note:** Since data is stored in memory only, all accounts and balances
reset when the program is closed. This is intentional for simplicity in
this first-semester project.

## Project Structure
```
banking-system-project/
├── bank_system.py     # Main application (all logic)
└── README.md          # Project documentation (this file)
```

## Author
Abishek Achuthan
