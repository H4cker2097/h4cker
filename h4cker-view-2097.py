import time
import os
import random
import sys

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
    {CYAN}{BOLD}Welcome to the  H4CKEr6_2097 TOOL!{RESET}
"""
    print(title)

def loading_spinner():
    spinner = "|/-\\"
    for _ in range(10):
        for char in spinner:
            sys.stdout.write(f"\r{YELLOW}[*] Loading {char} {RESET}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + " " * 20 + "\r")  # Clear the line after spinner

def stylized_count(action, count):
    return f"{GREEN}[H4CKER] {action} {count} completed! {RESET}"

def progress_bar(current, total):
    bar_length = 40
    filled_length = int(bar_length * current // total)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write(f"\r{BLUE}[H4CKER] Progress: |{bar}| {current}/{total} completed.{RESET}")
    sys.stdout.flush()

def perform_action(platform, action, count, post_link=None, vote_name=None):
    print(f"{GREEN}[*] H4CKER is initiating {action} for: {platform.upper()} - {post_link if post_link else vote_name}...{RESET}")
    loading_spinner()

    for i in range(1, count + 1):
        time.sleep(random.uniform(0.05, 0.2))  # Speed up to make it feel snappy
        print(stylized_count(action, i))
        progress_bar(i, count)
    print(f"\n{GREEN}[!] H4CKER has completed {action} for {platform.upper()} with {count} operations!{RESET}")

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

def validate_instagram_link(link):
    if link.startswith("https://www.instagram.com"):
        return True
    else:
        print(f"{RED}Invalid Instagram link! Please provide a valid link .{RESET}")
        return False

def validate_telegram_link(link):
    if link.startswith("https://t.me/"):
        return True
    else:
        print(f"{RED}Invalid Telegram link! Please provide a valid link .{RESET}")
        return False

def display_main_menu():
    print(f"{CYAN}{BOLD}============================================={RESET}")
    print(f"{YELLOW}Select a platform to proceed:{RESET}")
    print(f"{MAGENTA}1: Instagram{RESET}")
    print(f"{MAGENTA}2: Telegram{RESET}")
    print(f"{MAGENTA}3: Help{RESET}")
    print(f"{MAGENTA}4: Exit{RESET}")
    print(f"{CYAN}{BOLD}============================================={RESET}")

def display_instagram_menu():
    print(f"{CYAN}{BOLD}============================================={RESET}")
    print(f"{YELLOW}Select Instagram action:{RESET}")
    print(f"{MAGENTA}1: Post View{RESET}")
    print(f"{MAGENTA}2: Post Like{RESET}")
    print(f"{MAGENTA}3: Story View{RESET}")
    print(f"{MAGENTA}4: Back{RESET}")
    print(f"{CYAN}{BOLD}============================================={RESET}")

def display_telegram_menu():
    print(f"{CYAN}{BOLD}============================================={RESET}")
    print(f"{YELLOW}Select Telegram action:{RESET}")
    print(f"{MAGENTA}1: View {RESET}")
    print(f"{MAGENTA}2: Reaction {RESET}")
    print(f"{MAGENTA}3: Vote {RESET}")
    print(f"{MAGENTA}4: Back{RESET}")
    print(f"{CYAN}{BOLD}============================================={RESET}")

def perform_instagram_action(action_type):
    while True:  # Loop until the user decides to go back to the main menu
        if action_type == '1':
            views = get_valid_input(f"{YELLOW}Enter the number of views (100-2000): {RESET}", 100, 2000)
            post_link = input(f"{YELLOW}Enter Instagram post link: {RESET}")
            if validate_instagram_link(post_link):
                perform_action("Instagram", "Post View", views, post_link)
                return  # Return to main menu after action
        elif action_type == '2':
            likes = get_valid_input(f"{YELLOW}Enter the number of likes (50-1000): {RESET}", 50, 1000)
            post_link = input(f"{YELLOW}Enter Instagram post link: {RESET}")
            if validate_instagram_link(post_link):
                perform_action("Instagram", "Post Like", likes, post_link)
                return  # Return to main menu after action
        elif action_type == '3':
            story_views = get_valid_input(f"{YELLOW}Enter the number of story views (100-2000): {RESET}", 100, 2000)
            post_link = input(f"{YELLOW}Enter Instagram story link: {RESET}")
            if validate_instagram_link(post_link):
                perform_action("Instagram", "Story View", story_views, post_link)
                return  # Return to main menu after action

def perform_telegram_action(action_type):
    while True:  # Loop until the user decides to go back to the main menu
        if action_type == '1':
            views = get_valid_input(f"{YELLOW}Enter the number of views (100-2000): {RESET}", 100, 2000)
            post_link = input(f"{YELLOW}Enter Telegram post link: {RESET}")
            if validate_telegram_link(post_link):  # Validate the link here
                perform_action("Telegram", "View 2097", views, post_link)
                return  # Return to main menu after action
            else:
                print(f"{RED}Invalid link! Please enter a valid link again.{RESET}")
        elif action_type == '2':
            reactions = get_valid_input(f"{YELLOW}Enter the number of reactions (50-1000): {RESET}", 50, 1000)
            post_link = input(f"{YELLOW}Enter Telegram post link: {RESET}")
            if validate_telegram_link(post_link):  # Validate the link here
                perform_action("Telegram", "Reaction 2097", reactions, post_link)
                return  # Return to main menu after action
            else:
                print(f"{RED}Invalid link! Please enter a valid link again.{RESET}")
        elif action_type == '3':
            votes = get_valid_input(f"{YELLOW}Enter the number of votes (10-500): {RESET}", 10, 500)
            post_link = input(f"{YELLOW}Enter Telegram post link: {RESET}")
            if validate_telegram_link(post_link):  # Validate the link here
                vote_name = input(f"{YELLOW}Enter the name for the vote: {RESET}")
                perform_action("Telegram", "Vote 2097", votes, post_link, vote_name)
                return  # Return to main menu after action
            else:
                print(f"{RED}Invalid link! Please enter a valid link again.{RESET}")

def main():
    clear_screen()
    print_title()
    print(f"{MAGENTA}Welcome to the  H4CKER_2097 TOOL!{RESET}")
    
    while True:
        display_main_menu()
        platform_choice = input(f"{CYAN}Choose platform (1-4): {RESET}")
        
        if platform_choice == '1':  # Instagram
            while True:
                display_instagram_menu()
                instagram_choice = input(f"{CYAN}Enter Instagram action (1-4): {RESET}")
                
                if instagram_choice in ['1', '2', '3']:
                    perform_instagram_action(instagram_choice)
                elif instagram_choice == '4':
                    break
                else:
                    print(f"{RED}Invalid choice. Please try again.{RESET}")

        elif platform_choice == '2':  # Telegram
            while True:
                display_telegram_menu()
                telegram_choice = input(f"{CYAN}Enter Telegram action (1-4): {RESET}")

                if telegram_choice in ['1', '2', '3']:
                    perform_telegram_action(telegram_choice)
                elif telegram_choice == '4':
                    break
                else:
                    print(f"{RED}Invalid choice. Please try again.{RESET}")

        elif platform_choice == '3':  # Help
            print(f"{GREEN}This tool allows you to perform various actions on Instagram and Telegram.{RESET}")
            print(f"{YELLOW}For contact support , @H4CKER_2097 .{RESET}")
            input(f"{CYAN}Press Enter to return to the main menu...{RESET}")

        elif platform_choice == '4':  # Exit
            print(f"{GREEN}Thank you for using H4CKER_2097 TOOL!{RESET}")
            break
        
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")

if __name__ == "__main__":
    main()
