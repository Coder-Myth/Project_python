# A command-line app where you can add, view, delete,
# and mark tasks as done — basically a mini task manager that runs in the terminal.

print("Welcome to the TO DO LIST APP\n\t")


list = []


def add_task():
    list.append(input("Enter Your task:"))
    # pasṇs


def view_task():
    for i in range(len(list)):
        print(list[i])

 