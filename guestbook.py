import sys
import json


def new_entry(note):
    with open("guestbook.txt", "a") as file:
        file.write(note + "\n")


def list_entries():
    with open("guestbook.txt", "r") as file:
        return [line.strip() for line in file.readlines()]


def edit_entry(index, new_content):
    entries = list_entries()

    if 1 <= index <= len(entries):
        entries[index - 1] = new_content
        with open("guestbook.txt", "w") as file:
            for entry in entries:
                file.write(entry + "\n")
    else:
        print("Invalid index")


def delete_entry(index):
    entries = list_entries()
    entries.pop(-index)
    with open("guestbook.txt", "w") as file:
        for entry in entries:
            file.write(entry + "\n")


def export_entries():
    return json.dumps(list_entries())


def export_entries():
    return json.dumps(list_entries())


def main():
    if len(sys.argv) < 2:
        print("Usage: python guestbook.py [command] [arguments...]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "new":
        if len(sys.argv) < 3:
            print("Usage: python guestbook.py new [note]")
            sys.exit(1)
        note = " ".join(sys.argv[2:])
        new_entry(note)
        print("Note added successfully!")
    elif command == "list":
        entries = list_entries()
        if entries:
            print("Guestbook entries:")
            for index, entry in enumerate(entries, start=1):
                print(f"{index}. {entry}")
        else:
            print("Guestbook is empty.")
    elif command == "edit":
        if len(sys.argv) < 4:
            print("Usage: python guestbook.py edit [index] [new_content]")
            sys.exit(1)
        index = int(sys.argv[2])
        new_content = " ".join(sys.argv[3:])
        edit_entry(index, new_content)
        print("Note edited successfully!")
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python guestbook.py delete [index]")
            sys.exit(1)
        index = int(sys.argv[2])
        delete_entry(index)
        print("Note deleted successfully!")
    elif command == "export":
        exported_entries = export_entries()
        with open("exported_guestbook.json", "w") as export_file:
            export_file.write(exported_entries)
        print("Guestbook entries exported to 'exported_guestbook.json'.")
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
