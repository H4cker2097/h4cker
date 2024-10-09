import os

# ANSI escape codes for colors and styles
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
BLUE = "\033[34m"
BOLD = "\033[1m"
RESET = "\033[0m"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_title():
    title = f"""
{BLUE}{BOLD}        .--.
       |o_o |
       |:_/ |
      //   \\ \\
     (|     | )
    /'\\_   _/`\\
    \\___)=(___/

{MAGENTA}               {BOLD}H4CKER_2097 TOOL{RESET}
{YELLOW}==================================================
    {CYAN}{BOLD}Welcome to the H4CKEr6_2097 TOOL!{RESET}
"""
    print(title)

def get_valid_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"{RED}Please enter a number between {min_value} and {max_value}.{RESET}")
        except ValueError:
            print(f"{RED}Invalid input! Please enter a valid number.{RESET}")

def display_main_menu():
    print(f"{CYAN}{BOLD}============================================={RESET}")
    print(f"{YELLOW}Select a platform to proceed:{RESET}")
    print(f"{MAGENTA}1: Instagram{RESET}")
    print(f"{MAGENTA}2: Telegram{RESET}")
    print(f"{MAGENTA}3: Help{RESET}")
    print(f"{MAGENTA}4: Exit{RESET}")
    print(f"{CYAN}{BOLD}============================================={RESET}")

def main():
    clear_screen()
    print_title()
    
    while True:
        display_main_menu()
        choice = get_valid_input(f"{YELLOW}Enter your choice (1-4): {RESET}", 1, 4)

        if choice in [1, 2]:  # Instagram or Telegram
            platform = "Instagram" if choice == 1 else "Telegram"
            print(f"{GREEN}You selected {platform}.")
            print(f"{YELLOW}If you want the code, watch the video carefully to find the code inside the video.")
            print(f"{YELLOW}VIDEO LINK: https://youtu.be/NfUqaWyjcPo")
            
            while True:
                input_code = input(f"{YELLOW}\nPlease enter a 4-digit code to proceed (or enter 3 for Help, 4 to Exit): {RESET}\n")
                
                if input_code == "3":
                    print(f"{CYAN}For help, you can contact me on:\n"
                          f"Telegram: @H4CKER_2097\n"
                          f"Instagram: @H4CKER_2097{RESET}")
                elif input_code == "4":
                    print(f"{GREEN}Exiting the tool. Goodbye!{RESET}")
                    return  # Exit the program
                else:
                    print(f"{RED}All codes wrong! Please try again.{RESET}")

        elif choice == 3:
            print(f"{CYAN}For help, you can contact me on:\n"
                  f"Telegram: @H4CKER_2097\n"
                  f"Instagram: @H4CKER_2097{RESET}")
        elif choice == 4:
            print(f"{GREEN}Exiting the tool. Goodbye!{RESET}")
            break

if __name__ == "__main__":
    main()
