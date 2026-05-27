Notes Menu System

A beginner-friendly Python project that demonstrates how to build a menu-driven notes application using functions, loops, and file handling.

📌 Description

This program allows the user to:

Save notes into a text file
View saved notes
Exit the program

The menu runs continuously using a while True loop until the user chooses to exit.

🧠 Concepts Used

Functions
File Handling
open() function
Append Mode ('a')
Read Mode ('r')
while True loop
if-elif-else
User Input
Menu System

💻 Code

def save_note(note):
    file = open("notes.txt", "a")
    file.write(note + "\n")
    file.close()
    print("Note saved successfully")

def view_notes():
    file = open("notes.txt", "r")
    data = file.read()
    print(data)
    file.close()

while True:

    print("1. Save Notes")
    print("2. View Notes")
    print("3. Exit")

    Choice = int(input("Enter your choice: "))

    if Choice == 1:
        Note = input("Enter your notes: ")
        save_note(Note)

    elif Choice == 2:
        view_notes()

    elif Choice == 3:
        print("Program Ended")
        break

    else:
        print("invalid")

▶️ Example Output

1. Save Notes
2. View Notes
3. Exit

Enter your choice: 1
Enter your notes: Learn Python daily
Note saved successfully
Enter your choice: 2
Learn Python daily
