# 📚 LearnLyt – Knowledge Retention Tool

➜ LearnLyt is a Python-based console application designed to help users store, manage, and retrieve learning notes efficiently. It provides features to add, view, search, update, and delete notes, along with a summary report to track stored knowledge.

## ✨ Features

- ➕ **Add Notes:** Create and save notes with titles, content, and categories.
- 📖 **View Notes:** Display saved learning notes.
- 🔍 **Search Notes:** Find notes using relevant keywords.
- ✏️ **Update Notes:** Modify existing notes when information changes.
- 🗑️ **Delete Notes:** Remove notes that are no longer needed.
- 📊 **Summary Report:** View the total number of notes, category-wise counts, and the most recently updated note.
- 💾 **Data Persistence:** Store notes in a JSON file so they remain available between sessions.

## 🛠️ Technologies Used

- 🐍 Python 3.9+
- 📋 JSON
- 📅 Python date and time utilities

➜ No third-party Python packages are required.

## 🚀 Installation and Execution

**Step 1:** Install Python 3.9 or later.

**Step 2:** Clone or download this repository.

**Step 3:** Open the project folder in a terminal.

**Step 4:** Run the following command:

```bash
python learnlyt.py
```

**Step 5:** Follow the menu displayed in the terminal to manage your learning notes.

## 📂 Project Structure

```text
LearnLyt/
│
├── learnlyt.py
├── learnlyt_data.json
└── README.md
```

➜ `learnlyt_data.json` is created or updated by the application to store notes. It may not exist until the application saves data.

## ⚙️ How It Works

1. ➜ The user launches the application.
2. ➜ The menu displays the available note-management operations.
3. ➜ The user can add, view, search, update, or delete notes.
4. ➜ Notes are stored in a JSON file.
5. ➜ The summary report displays note statistics and the most recently updated note.
6. ➜ Saved data can be accessed again when the application is run later.

## 📊 Summary Report

The application provides a summary containing:

- 📝 Total number of saved notes.
- 📚 Category-wise note counts.
- 🕒 Most recently updated note.

## 🧪 Sample Usage

1. ➜ Launch LearnLyt.
2. ➜ Add a note with a title, content, and category.
3. ➜ View all saved notes.
4. ➜ Search for a note using a keyword.
5. ➜ Update or delete a note when required.
6. ➜ Generate the summary report to review your stored notes.

## 🔮 Future Enhancements

- ↳ Add a graphical user interface.
- ↳ Support exporting notes to PDF.
- ↳ Add reminders for reviewing notes.
- ↳ Include sorting and filtering options.
- ↳ Add automated tests for note-management operations.

---

**📚 LearnLyt – Save your knowledge, strengthen your learning.**
