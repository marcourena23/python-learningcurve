# Slot Machine
import os
import random

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def show_title():
    print("--------------------------------")
    print("    WELCOME TO THE SLOT MACHINE   ")
    print("      THEME: TROPICAL FRUITS      ")
    print("      WIN BIG WITH 3 MATCHES!       ")
    print("    Symbols: 🍍, 🍌, 🥭, 🥥, 🍉")
    print("      COIN IN, PULL THE LEVER!  ")
    print("--------------------------------")

def show_instructions():
    print("--------------------------------")
    print("        INSTRUCTIONS:                ")
    print("    - Enter your bet between 1 and 100        ")
    print("    - Pull the lever to spin      ")
    print("    - Match 3 symbols to win      ")
    print("--------------------------------")

def spin_row():
    symbols = ['🍍', '🍌', '🥭', '🥥', '🍉']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(f"Row 1: {row[0]} {row[1]} {row[2]}")
    print("\n")

def get_payout(row1, row2, row3):
    if row1 == row2 == row3:
        return 100
    elif row1 == row2 or row1 == row3 or row2 == row3:
        return 50
    else:
        return 0

def main():
    balance = 100
    clean_screen()
    show_title()
    show_instructions()
    
    while balance > 0:
        print(f"Current balance: ${balance}")
        print("--------------------------------")
        bet = input(f"Enter your bet (1-100): ")
        if not bet.isdigit():
            print("Invalid bet. Please enter a validnumber.")
            continue
        
        bet = int(bet)
        if bet < 1 or bet > 100:
            print(f"Invalid bet. Please enter a valid number between 1 and {balance}	.")
            continue
        
        balance -= bet
        
        row1 = spin_row()
        row2 = spin_row()
        row3 = spin_row()
        print("Spinning...\n\n")
        print(f"Row 1: {row1}")
        print(f"Row 2: {row2}")
        print(f"Row 3: {row3}")
        print("\n")
        
        payout = get_payout(row1, row2, row3)
        if payout > 0:
            print(f"You won ${payout}!")
        
if __name__ == "__main__": 
    main()