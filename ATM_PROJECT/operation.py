# atm/operations.py

from datetime import datetime
from data import account

def display_balance():
    print(f"\n💰 Current Balance: ₹{account['balance']:.2f}\n")

def withdraw_money(amount):
    if amount <= 0:
        print("⚠️ Enter a valid amount.")
        return
    if amount > account['balance']:
        print("❌ Insufficient balance.")
        return
    account['balance'] -= amount
    record_transaction("Withdraw", amount)
    print(f"✅ Withdrawal successful! ₹{amount:.2f} withdrawn.\n")

def deposit_money(amount):
    if amount <= 0:
        print("⚠️ Enter a valid amount.")
        return
    account['balance'] += amount
    record_transaction("Deposit", amount)
    print(f"✅ Deposit successful! ₹{amount:.2f} added.\n")

def show_statement():
    print("\n📜 Transaction Statement:")
    if not account['transactions']:
        print("No transactions yet.\n")
        return
    for txn in account['transactions']:
        print(f"{txn['time']} | {txn['type']}: ₹{txn['amount']:.2f}")
    print()

def record_transaction(txn_type, amount):
    account['transactions'].append({
        "type": txn_type,
        "amount": amount,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
