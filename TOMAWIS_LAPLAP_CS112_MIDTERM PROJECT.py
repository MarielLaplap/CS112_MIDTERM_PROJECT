class ATM:
    def __init__(self):
        # Initialize ATM with default balance, empty PIN, and an empty transaction history
        self.balance = 10000
        self.pin = ""
        self.transaction_history = []

    def display_balance(self):
        # Display the balance formatted with two decimal places
        print(f"Your balance is: ₱{self.balance:.2f}")

    def withdraw(self):
        while True:
            amount = float(input("Enter the amount to withdraw: ₱"))
            if amount > self.balance:
                print("Insufficient funds. Withdrawal failed.")
            else:
                # Update balance, display successful withdrawal, and record the transaction
                self.balance -= amount
                print(f"Withdrawal successful. Remaining balance: ₱{self.balance:.2f}")
                self.transaction_history.append(f"Withdrew ₱{amount:.2f}")
                break

    def transfer(self):
        while True:
            amount = float(input("Enter the amount to transfer: ₱"))
            if amount > self.balance:
                print("Insufficient funds. Transfer failed.")
            else:
                recipient = input("Enter the recipient's account number: ")
                if recipient:
                    # Update balance, display successful transfer, and record the transaction
                    print(f"₱{amount:.2f} transferred to {recipient}.")
                    self.balance -= amount
                    print(f"Remaining balance: ₱{self.balance:.2f}")
                    self.transaction_history.append(f"Transferred ₱{amount:.2f} to {recipient}")
                    break
                else:
                    print("Invalid recipient. Please enter a valid account number.")

    def deposit(self):
        while True:
            amount = float(input("Enter the amount to deposit: ₱"))
            if amount <= 25000:
                # Update balance, display successful deposit, and record the transaction
                self.balance += amount
                print(f"Deposit successful. Updated balance: ₱{self.balance:.2f}")
                self.transaction_history.append(f"Deposited ₱{amount:.2f}")
                break
            elif amount > 25000:
                # Display a message for deposits exceeding the limit
                print(
                    "The maximum deposit allowed at this ATM is 25,000 PHP within a 24-hour period.\n"
                    "If your deposit exceeds this limit, we recommend visiting the branch during business hours. "
                    "Thank you for your understanding."
                )

    def change_pin(self):
        while True:
            current_pin = input("Enter your current 4-digit PIN for verification: ")
            if current_pin != self.pin:
                print("Incorrect current PIN. Please try again.")
            else:
                while True:
                    new_pin = input("Enter your new 4-digit PIN: ")
                    verify_new_pin = input("Re-enter your new 4-digit PIN for verification: ")

                    if new_pin == verify_new_pin and len(new_pin) == 4 and new_pin.isdigit():
                        # Update PIN and display success message
                        self.pin = new_pin
                        print("PIN successfully changed.")
                        return  # Exit both loops when PIN change is successful
                    else:
                        print("Invalid PIN or PINs do not match. Please try again.")

    def view_transaction_history(self):
        # Display the transaction history
        print("\n===== Transaction History =====")
        for transaction in self.transaction_history:
            print(transaction)

    def run(self):
        # Set the initial PIN
        self.pin = input("Set your 4-digit PIN: ")
        while len(self.pin) != 4 or not self.pin.isdigit():
            print("Invalid PIN. Please enter a 4-digit number.")
            self.pin = input("Set your 4-digit PIN: ")

        while True:
            # Display ATM menu
            print("\n===== ATM Simulator =====")
            print("1. Display Balance")
            print("2. Withdraw Money")
            print("3. Transfer Money")
            print("4. Deposit Money")
            print("5. Change PIN")
            print("6. View Transaction History")
            print("7. Quit")

            choice = input("Enter your choice (1-7): ")

            # Process user choice
            if choice == '1':
                self.display_balance()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.transfer()
            elif choice == '4':
                self.deposit()
            elif choice == '5':
                self.change_pin()
            elif choice == '6':
                self.view_transaction_history()
            elif choice == '7':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    atm = ATM()
    atm.run()
