# main.py

from operation import display_balance, withdraw_money, deposit_money, show_statement

def main():
    while True:
        print("\n===== 🏧 ATM Menu =====")
        print("1. Display Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Show Statement")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            display_balance()
        elif choice == "2":
            try:
                amt = float(input("Enter amount to withdraw: ₹"))
                withdraw_money(amt)
            except ValueError:
                print("⚠️ Invalid input.")
        elif choice == "3":
            try:
                amt = float(input("Enter amount to deposit: ₹"))
                deposit_money(amt)
            except ValueError:
                print("⚠️ Invalid input.")
        elif choice == "4":
            show_statement()
        elif choice == "5":
            print("\n👋 Thank you for using our ATM!")
            break
        else:
            print("⚠️ Invalid option, please try again.")

if __name__ == "__main__":
    main()
