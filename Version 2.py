import json

# Create empty dictionary to store usernames and passwords
passwords = {}

# Load passwords from file if it exists
try:
    with open('passwords.json', 'r') as f:
        passwords = json.load(f)
except FileNotFoundError:
   pass 

def menu():
    choice = input("""Select your option:
1. Add new password
2. Get password
3. Exit
Option: """)
    return choice

def add_password():
    username = input("Enter username: ")
    password = input("Enter password: ")
    print("Password saved.")
    passwords[username] = password

    # Save passwords to file
    with open('passwords.json', 'w') as f:
        json.dump(passwords, f)

def get_password():
    username = input("Enter username: ")
    if username in passwords:
        print(f"Password for {username}: {passwords[username]}")
    else:
        print("Username not found.")

def main():
    while True:
        choice = menu()
        if choice == "1":
            add_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

# Call the main function to start the program
main()


