
# task 1
def feb_1(n, x=0, y=1):
    if n == 1:
        feb = 0
        print(feb)
    elif n == 2:
        feb = 1
        print(feb)
    else:
        i = 3
        while i <= n:
            feb = x + y
            x = y
            y = feb
            i += 1
        print(feb)

n = int(input("Please enter the nth term of the Fibonacci sequence: "))
feb_1(n)

#task2

List = ["wake up at 9 am", "finish all my homeworks", "go to protons", "take lunch"]

def view_1(view, List):
    if view == "yes":
        print(List)

def add_task(List, new):
    List.append(new)

def mark_task_completed(List, task_to_mark):
    if task_to_mark in List:
        List[List.index(task_to_mark)] += " (completed)"
    else:
        print("Task not found.")

def delete_task(List, rem):
    if rem in List:
        List.remove(rem)
    else:
        print("Task not found.")

while True:
    new = input("Write the task you want to add to the list (or type 'close' to exit): ")
    if new.lower() == 'close':
        break

    add_task(List, new)
    view = input("Do you want to see your list after the changes you've made? (yes/no): ")
    view_1(view, List)

    task_to_mark = input("Enter the name of the task you want to mark as done (or type 'close' to exit): ")
    if task_to_mark.lower() == 'close':
        break

    mark_task_completed(List, task_to_mark)
    view = input("Do you want to see your list after marking the task as completed? (yes/no): ")
    view_1(view, List)

    rem = input("Please enter the task you want to remove (or type 'close' to exit): ")
    if rem.lower() == 'close':
        break

    delete_task(List, rem)
    view = input("Do you want to see your list after removing the task? (yes/no): ")
    view_1(view, List)


#task3
#groupwork
#Develop a simple chat system where users can send messages to each other. This task will involve creating functions to handle sending, receiving, and displaying messages, as well as managing a list of users and their chat histories.
#  Features:
# Register User: Users can register with a unique username.
# Send Message: Users can send messages to each other.
# View Messages: Users can view all their sent and received messages.
# Groups:
# Each group consists of two members.
# Collaboration:
# Use GitHub to manage code.
# Each member works on their assigned component and collaborates through a github repository.
# Use a dictionary to store users and their chat histories. Each user will have a list of messages, where each message is represented as a dictionary containing the sender, receiver, and message text.
# Ex
# register_user("Samir")
# register_user("Osama") 
# send_message("Samir", "Osama", "Hello, Osama!") 
# view_messages("Osama")
# send_message("Osama", "Samir", "Hi, Samir!") 
