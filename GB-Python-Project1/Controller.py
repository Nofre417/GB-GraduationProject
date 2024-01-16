import os
import Model

def start():
    notes = []
    filename = "Notes.json"


    if os.path.exists(filename):
        notes = Model.load_notes(filename)

    while True:
        print("1. Add note")
        print("2. Edit note")
        print("3. Delete note")
        print("4. Notes list")
        print("5. Exist")
        command = input("Enter command: ")

        if command == "1":
            Model.add_note(notes)
        elif command == "2":
            Model.edit_note(notes)
        elif command == "3":
            Model.delete_note(notes)
        elif command == "4":
            Model.print_notes(notes)
        elif command == "5":
            break
        else:
            print("Incorrect command")

    Model.save_notes(notes, filename)