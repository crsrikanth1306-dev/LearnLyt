"""
LearnLyt - Knowledge Retention Tool
A beginner-friendly, menu-driven Python project.

Features:
- Add, view, search, update, and delete knowledge notes
- Organize notes by subject/category
- Store data persistently in learnlyt_data.json
- Display simple summary reports

Run:
    python learnlyt.py
"""

import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path(__file__).with_name("learnlyt_data.json")


def load_notes():
    """Load saved notes from JSON. Return an empty list if no data exists yet."""
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read the saved data file. Starting with an empty list.")
        return []


def save_notes(notes):
    """Save all notes to JSON so they remain available after restarting the program."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4, ensure_ascii=False)


def next_id(notes):
    return max((note.get("id", 0) for note in notes), default=0) + 1


def get_non_empty(prompt, current=None):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        if current is not None:
            return current
        print("This field cannot be empty. Please try again.")


def add_note(notes):
    print("\n--- Add Knowledge Note ---")
    title = get_non_empty("Enter note title: ")
    category = get_non_empty("Enter subject/category: ")
    content = get_non_empty("Enter key points or note content: ")
    note = {
        "id": next_id(notes),
        "title": title,
        "category": category,
        "content": content,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    notes.append(note)
    save_notes(notes)
    print(f"Note saved successfully! Note ID: {note['id']}")


def show_note(note):
    print("-" * 55)
    print(f"ID       : {note['id']}")
    print(f"Title    : {note['title']}")
    print(f"Category : {note['category']}")
    print(f"Content  : {note['content']}")
    print(f"Created  : {note.get('created_at', 'Unknown')}")
    print(f"Updated  : {note.get('updated_at', 'Unknown')}")


def view_notes(notes):
    print("\n--- All Knowledge Notes ---")
    if not notes:
        print("No notes saved yet. Choose option 1 to add your first note.")
        return
    for note in notes:
        show_note(note)
    print("-" * 55)


def search_notes(notes):
    print("\n--- Search Notes ---")
    keyword = get_non_empty("Enter a title, category, or keyword: ").casefold()
    matches = [
        note for note in notes
        if keyword in note.get("title", "").casefold()
        or keyword in note.get("category", "").casefold()
        or keyword in note.get("content", "").casefold()
    ]
    if not matches:
        print("No matching notes found.")
        return
    print(f"Found {len(matches)} matching note(s):")
    for note in matches:
        show_note(note)


def find_note_by_id(notes, note_id):
    return next((note for note in notes if note.get("id") == note_id), None)


def ask_note_id():
    try:
        return int(input("Enter note ID: ").strip())
    except ValueError:
        print("Please enter a valid numeric ID.")
        return None


def update_note(notes):
    print("\n--- Update Knowledge Note ---")
    note_id = ask_note_id()
    if note_id is None:
        return
    note = find_note_by_id(notes, note_id)
    if not note:
        print("No note exists with that ID.")
        return

    print("Press Enter to keep the current value.")
    note["title"] = get_non_empty(f"Title [{note['title']}]: ", note["title"])
    note["category"] = get_non_empty(f"Category [{note['category']}]: ", note["category"])
    note["content"] = get_non_empty(f"Content [{note['content']}]: ", note["content"])
    note["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    save_notes(notes)
    print("Note updated successfully.")


def delete_note(notes):
    print("\n--- Delete Knowledge Note ---")
    note_id = ask_note_id()
    if note_id is None:
        return
    note = find_note_by_id(notes, note_id)
    if not note:
        print("No note exists with that ID.")
        return
    confirm = input(f"Delete '{note['title']}'? (y/n): ").strip().lower()
    if confirm == "y":
        notes.remove(note)
        save_notes(notes)
        print("Note deleted.")
    else:
        print("Delete cancelled.")


def show_report(notes):
    print("\n--- LearnLyt Summary Report ---")
    print(f"Total notes: {len(notes)}")
    if not notes:
        print("Add notes to see category summaries.")
        return
    category_counts = {}
    for note in notes:
        category = note.get("category", "Uncategorized")
        category_counts[category] = category_counts.get(category, 0) + 1
    print("Notes by category:")
    for category, count in sorted(category_counts.items(), key=lambda item: item[0].casefold()):
        print(f"  {category}: {count}")
    latest = max(notes, key=lambda note: note.get("updated_at", ""))
    print(f"Most recently updated: {latest.get('title', 'Untitled')} ({latest.get('updated_at', 'Unknown')})")


def print_menu():
    print("\n" + "=" * 42)
    print("          LEARNLYT")
    print("       Knowledge Retention Tool")
    print("=" * 42)
    print("1. Add a knowledge note")
    print("2. View all notes")
    print("3. Search notes")
    print("4. Update a note")
    print("5. Delete a note")
    print("6. View summary report")
    print("0. Exit")


def main():
    notes = load_notes()
    print("Welcome to LearnLyt!")
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_note(notes)
        elif choice == "2":
            view_notes(notes)
        elif choice == "3":
            search_notes(notes)
        elif choice == "4":
            update_note(notes)
        elif choice == "5":
            delete_note(notes)
        elif choice == "6":
            show_report(notes)
        elif choice == "0":
            print("Your notes are saved. Keep learning with LearnLyt!")
            break
        else:
            print("Invalid option. Please choose from the menu.")


if __name__ == "__main__":
    main()
