import os
import time
import subprocess

os.system('cls' if os.name == 'nt' else 'clear')

ascii_art ="""\033[91m

    ███████╗██╗   ██╗██╗     ███████╗██╗  ██╗
    ╚══███╔╝╚██╗ ██╔╝██║     ██╔════╝╚██╗██╔╝
      ███╔╝  ╚████╔╝ ██║     █████╗   ╚███╔╝ 
     ███╔╝    ╚██╔╝  ██║     ██╔══╝   ██╔██╗ 
    ███████╗   ██║   ███████╗███████╗██╔╝ ██╗
    ╚══════╝   ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝
                                 Made by MrSh4dow
"""

os.system('title Zylex v1.0')

def display_menu():
    print(ascii_art)
    print("\033[96mChoose an option:")
    print("\033[96m1. Link Bypass")
    print("\033[96m2. Option 2")
    print("\033[96m3. Option 3")
    print("\033[96m0. Exit")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            subprocess.run(["python", "cmds/bypass.py"]) 
        elif choice == '2':
            subprocess.run(["python", "cmds/option2.py"])
        elif choice == '3':
            subprocess.run(["python", "cmds/option3.py"])
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
        
        time.sleep(1)

if __name__ == "__main__":
    main()