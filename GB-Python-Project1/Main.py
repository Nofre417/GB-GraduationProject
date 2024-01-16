import json
import os
import datetime
class Note:
    def __init__(self, id, title, body, date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

def load_notes(filename):
    with open(filename, "r") as f:
        notes = []
        for line in f:
            note_dict = json.loads(line)
            note_dict["date"] = datetime.datetime.fromisoformat(note_dict["date"])
            notes.append(Note(note_dict["id"], note_dict["title"], note_dict["body"], note_dict["date"]))
    return notes

def save_notes(notes, filename):
    with open(filename, "w") as f:
        for note in notes:
            note_dict = note.__dict__
            note_dict["date"] = note_dict["date"].isoformat()
            f.write(json.dumps(note_dict))
            f.write("\n")

def get_notes_by_date(notes, date):
    return [note for note in notes if note.date == date]

def print_note(note):
    print("ID:", note.id)
    print("Title:", note.title)
    print("Body:", note.body)
    print("Date creating/editing:", note.date)

def print_notes(notes):
    for note in notes:
        print_note(note)

def add_note(notes):
    id = int(input("Enter note ID: "))
    title = input("Enter note title: ")
    body = input("Enter note body: ")
    date = datetime.datetime.now()
    note = Note(id, title, body, date)
    notes.append(note)

def edit_note(notes):
    id = int(input("Enter ID of note for editing: "))
    note = get_note_by_id(notes, id)
    if note is None:
        print("Note not exist with entered ID")
        return

    new_data = {}
    for field in ["title", "body"]:
        value = input(f"Enter new {field} note's (left empty to cancel editing): ")
        new_data[field] = value if value else getattr(note, field)

    note.title = new_data.get("title", note.title)
    note.body = new_data.get("body", note.body)
    note.date = datetime.datetime.now()

    print("The note was successfully edit")


def delete_note(notes):
    id = int(input("Enter ID note for delete: "))
    note = get_note_by_id(notes, id)
    if note is None:
        print("Note not exist with entered ID")
        return
    notes.remove(note)

def get_note_by_id(notes, id):
    for note in notes:
        if note.id == id:
            return note
    return None

def main():
    notes = []
    filename = "Notes.json"


    if os.path.exists(filename):
        notes = load_notes(filename)

    while True:
        print("1. Add note")
        print("2. Edit note")
        print("3. Delete note")
        print("4. Notes list")
        print("5. Exist")
        command = input("Enter command: ")

        if command == "1":
            add_note(notes)
        elif command == "2":
            edit_note(notes)
        elif command == "3":
            delete_note(notes)
        elif command == "4":
            print_notes(notes)
        elif command == "5":
            break
        else:
            print("Incorrect command")

    save_notes(notes, filename)

if __name__ == "__main__":
    main()