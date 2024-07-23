users = []  # List of registered users
history = []  # Chat history

def register():
    user = input("Enter your name to register: ")
    if user not in users:
        users.append(user)
        print(f"{user} has been registered successfully.")
    else:
        print("This username is already registered.")

def send(user):
    global msg, receiver
    msg = input("Please enter the message you want to send: ")
    receiver = input("Please enter the name of the user you want to send the message to: ")
    user_activity(msg, receiver, user)

def get_username(user):
    if user in users:
        print(f"Hi {user}, you have logged in successfully.")
        return True
    else:
        print("Invalid username.")
        return False

def user_activity(msg, receiver, user):
    dict1 = {
        "Sender": user,
        "sent_to": receiver,
        "message": msg
    }
    history.append(dict1)
    return dict1

while True:
    action = input("Do you want to (1) Register or (2) Login? (Enter 1 or 2): ")
    if action == '1':
        register()
    elif action == '2':
        user = input("Enter a valid Username: ")

        if get_username(user):
            send(user)
            yes = input("Do you want to see your chatting activity (yes or no)? ")
            if yes.lower() == "yes":
                print(history)
        else:
            print("Please try again with a valid username.")
    else:
        print("Invalid option. Please enter 1 or 2.")
    
    cont = input("Do you want to continue (yes or no)? ")
    if cont.lower() != "yes":
        break
