def spin_row():
    symbols = ['🍒', '🍉', '🍈', '🔔', '⭐']

def print_row():
    pass

def get_payout():
    pass

def main():
    balance = 100
    print("***********************")
    print("Welcome to python game")
    print("Symbols: 🍒 🍉 🍈 🔔 ⭐") # emojis = windows + ;
    print("***********************")

    while balance > 0:
        print(f"current balance: {balance}")
        print("***********************")

        bet = input("place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid amount!")
            continue
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()

if __name__ == '__main__':
    main()