# Task Automation with Python Scripts

Three real-life automation scripts built with Python.

---

## Scripts Overview

### Task 1 — Move JPG Files (`scripts/move_jpg_files.py`)
Moves all `.jpg` / `.jpeg` files from one folder to another.
- Skips non-image files automatically
- Renames duplicates with a timestamp
- **Concepts:** `os`, `shutil`, file handling

**Run:**
```bash
python scripts/move_jpg_files.py
```
Output: `output/moved_images/`

---

### Task 2 — Extract Emails (`scripts/extract_emails.py`)
Scans a `.txt` file for all email addresses using regex and saves them.
- Deduplicates emails (case-insensitive)
- Groups by domain
- Shows total vs unique count
- **Concepts:** `re`, file handling

**Run:**
```bash
python scripts/extract_emails.py
```
Input: `sample_data/emails.txt`  
Output: `output/extracted_emails.txt`

---

### Task 3 — Web Scraper (`scripts/web_scraper.py`)
Fetches a webpage and extracts the title, meta description, and H1 headings.
- Saves structured results to a text file
- **Concepts:** `requests`, `re`, file handling

**Run:**
```bash
python scripts/web_scraper.py
```
Output: `output/scraped_title.txt`

---

## Folder Structure

```
task_automation/
├── scripts/
│   ├── move_jpg_files.py
│   ├── extract_emails.py
│   └── web_scraper.py
├── sample_data/
│   ├── images/          ← put .jpg files here
│   └── emails.txt       ← input for email extractor
├── output/              ← all results saved here
├── .vscode/
│   └── launch.json      ← VS Code run configs (F5)
└── README.md
```

## How to Run in VS Code
1. Open the `task_automation` folder in VS Code
2. Press **F5**
3. Choose which task to run from the dropdown

## Install Dependency (for Script 3)
```bash
pip install requests
```

## Key Python Concepts Used
| Concept | Used In |
|---------|---------|
| `os` | All scripts — paths, folders |
| `shutil` | Script 1 — moving files |
| `re` | Scripts 2 & 3 — regex patterns |
| `requests` | Script 3 — HTTP requests |
| File handling | All scripts — read/write |
