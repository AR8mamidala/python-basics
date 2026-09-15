import json
import datetime

try:
    # Updates the Python dictionary and "r" means read mode because Python reads the JSON file
    with open("login_data.json", "r") as file:
        login_attempts = json.load(file)
except FileNotFoundError:
    # When the file is run initially, the JSON file will not exist, so the program creates the initial dictionary
    login_attempts = {
        "Heather" : {
            "failed_attempts" : 5,
            "last_login_attempt" : ""
        },
        "Aliya" : {
            "failed_attempts" : 7,
            "last_login_attempt" : ""
        },
        "Jenny" : {
            "failed_attempts" : 3,
            "last_login_attempt" : ""
        }
    }

def save_data():
    # open() opens a file and "w" means write mode so Python can put data into the file
    with open("login_data.json", "w") as file:
        # takes the dictionary and saves it into the file
        json.dump(login_attempts, file)

while True:
    print("Menu:")
    print("1. Track a login")
    print("2. View the login security summary")
    print("3. Exit")
    option = input("Choose an option (1-3): ")    
    if option=="1":
        print(login_attempts)
        username = input("Enter a username: ")
        # Getting the timestamps, datetime is a class in the datetime module
        if username in login_attempts:
            login_success = input("Was the login successful (Y/N)? ")
            login_success = login_success.upper()
            if login_success=="N":
                login_attempts[username]['failed_attempts'] = login_attempts[username]['failed_attempts'] + 1
                # json.dump() does not know how to turn datetime object into JSON so .isoformat changes it into a string
                login_attempts[username]['last_login_attempt'] = datetime.datetime.now().isoformat()
                save_data()
                print(f"{username} has {login_attempts[username]['failed_attempts']} failed login attempts.")
            elif login_success=="Y":
                login_attempts[username]['last_login_attempt'] = datetime.datetime.now().isoformat()
                save_data()
                print(f"{username} has {login_attempts[username]['failed_attempts']} failed login attempts.")
            else:
                print("Please answer the question properly.")
        else:
            print(f"The username '{username}' is not in the login tracker.")
            add_username = input("Would you like to add this username (Y/N)? ")
            add_username = add_username.upper()
            if add_username=="Y":
                login_attempts.update({username : {
                    "failed_attempts" : 0,
                    "last_login_attempt" : ""
                }})
                save_data()
                print("The username has successfully been added.")
            elif add_username=="N":
                print("The username has not been added.")
            else:
                print("Please answer the question properly.")
    elif option=="2":
        print("Login security summary:")
        for x,y in login_attempts.items():
            if y["failed_attempts"]>=5:
                print(f"{x} : {y['failed_attempts']} failed attempts - suspicious activity! - {y['last_login_attempt']}")
            else:
                print(f"{x} : {y['failed_attempts']} - {y['last_login_attempt']}")
    elif option=="3":
        print("Bye bye!")
        break
    else:
        print("Choose a valid option please.")
        continue
