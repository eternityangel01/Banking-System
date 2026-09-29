# Problem Statement

## Problem Statement
Manual or unstructured handling of everyday banking operations — opening
accounts, recording deposits and withdrawals, and tracking a customer's
transaction history — is error-prone and hard to audit when done without
a structured system. Students learning software development need a
realistic, moderately complex problem to practice core concepts such as
layered application design, data persistence, input validation, secure
credential handling, and automated testing.

This project addresses that by building a **Simple Banking System**: a
command-line application that models the essential operations of a
retail bank account in a structured, testable, and secure way.

## Scope of the Project
The system is a **single-machine, command-line application** intended
for educational purposes. It covers:
- Creating and authenticating customer accounts
- Performing deposits, withdrawals, and transfers between accounts
- Persisting all account and transaction data in a local SQLite database
  (so data survives between program runs)
- Generating balance inquiries, transaction histories, and account
  summaries
- Logging all significant actions for auditing/debugging
- Automated unit tests validating the core business logic

**Out of scope:** a graphical user interface, multi-user concurrent
access over a network, integration with real banking/payment rails,
and regulatory compliance features (KYC, AML, etc.) — these are beyond
the scope of a first-semester learning project.

## Target Users
- **Primary:** Computer Science / IT students learning application
  design, database integration, and testing in Python.
- **Secondary (in-story):** A bank customer using a teller-style
  command-line terminal to manage their own account — deposits,
  withdrawals, transfers, and checking their balance/history.

## High-Level Features
1. **Account Management** — create an account with a name and a
   4-digit PIN; the system generates a unique account number.
   Login/authentication is required before any sensitive operation.
2. **Transaction Management** — deposit funds, withdraw funds (blocked
   if it would overdraw the account), and transfer funds between two
   valid accounts.
3. **Reporting & Statements** — check the current balance, view the
   full chronological transaction history, and view a summary
   (total deposits, total withdrawals, transaction count).
4. **Security** — PINs are salted and hashed (SHA-256) before being
   stored; plain-text PINs are never written to disk.
5. **Reliability & Logging** — all operations are wrapped in
   validation and exception handling, and every significant action is
   written to a log file with a timestamp.
