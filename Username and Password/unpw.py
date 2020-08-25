import json             


def login(usr):
    uN = input("Enter Username: ")
    pW = input("Enter Password: ")

    if uN in usr.keys():
        if pW == usr[uN]:
            print("\n")
            print("Welcome back ", uN)
            print("\n")
           

        else:
            print("Incorrect password.")
            print("\n")
            login(usr)
            return False

    else:
        print("\n")
        print("Hello new user, your username and password has been created, please sign in.")
        usr[uN] = pW
        login(usr)
        print("\n")
    
    writeUsers(usr)
    return True



def readUsers():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def writeUsers(usr):
    with open("users.json", "w+") as f:
            json.dump(usr, f)




users = readUsers()
success = login(users)



while not success:
    success = login(users)


