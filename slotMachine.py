# Slot Machine
import os

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
    print("    - Insert coins to play        ")
    print("    - Pull the lever to spin      ")
    print("    - Match 3 symbols to win      ")
    print("--------------------------------")

def spin_row():
    pass

def print_row(row):
    pass

def get_payout(row):
    pass

def main():
    balance = 100
    clean_screen()
    show_title()
    show_instructions()
    
    while balance > 0:
        bet = input(f"Enter your bet (1-100): ")
        if not bet.isdigit():
            print("Invalid bet. Please enter a validnumber.")
            continue

if __name__ == "__main__":
    
    main()