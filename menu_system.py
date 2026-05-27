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

    else:
        print("invalid")

        
        

