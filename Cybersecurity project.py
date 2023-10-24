import random
import string

user_database = {}

def generate_password(l=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(l))
    return password

def user_registration(username, password):
    if username in user_database:
        print("Username already exists. Please choose another one.")
    else:
        user_database[username] = password
        print("Registration is successful.")

def two_f_a(username, password):
    if username in user_database and user_database[username] == password:
        otp = str(random.randint(1000, 9999))
        print("Authentication code sent to email", otp)
            
        user_input = input("Enter the authentication code: ")
        if user_input == otp:
            print("Authentication successful.")
        else:
            print("Authentication failed. Invalid code.")
            
    else:
        print("Login failed. Invalid username or password.")


while True:
    print("\nOptions:")
    print("1. Register a new user")
    print("2. Login with 2FA")
    print("3. Exit")
        
    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter a username: ")
        password = generate_password()
        print("Generated password:", password)
        user_registration(username, password)
            
    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        two_f_a(username, password)
            
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")    
           

while True:
    ch = input("Do you wish to access password manager (y/n)?")
    if ch == "y":
        passwords = user_database
        while True:
            print("\nPassword Manager Menu:")
            print("1. View Passwords")
            print("2. Edit Password")
            print("3. Delete Password")
            print("4. Exit")
            
            choice = input("Enter your choice: ")

            if choice == "1":
                print("\nSaved Passwords:")
                for key, value in passwords.items():
                    print(key,":", value)

            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                passwords[username] = password
                print("Password for", username, "updated.")

            elif choice == "3":
                username = input("Enter username to delete: ")
                if username in passwords:
                    del passwords[username]
                    print("Password for ", username, "deleted.")
                else:
                    print("No password found for ", username)

            elif choice == "4":
                print("Exiting Password Manager.")
                break

            else:
                print("Invalid choice. Please select a valid option.")
    else:
        break







