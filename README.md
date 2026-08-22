# 🧩 Crossword Game

**Crossword** is the experience you may have been waiting for!

Tired of boring, clunky crossword interfaces? We get it. It's a sleek, modern, and high-performance desktop game built with Python and `CustomTkinter`. It's got a dark-mode-first design, smooth keyboard navigation, and it's fast—just like the engine powering it.

---

## ⚡ Powered by Speed

Life is too short for slow package managers. That's why **Crossword** uses [uv](https://astral.sh/uv/) for lightning-fast dependency management.

---

## ✨ Why You'll Love It

* **Modern Aesthetic:** Dark mode looks sharp. The UI is clean, professional, and easy on the eyes.
* **Pro-Level Controls:** Navigate with arrow keys, hit `Backspace` to correct mistakes, and tap `Escape` to toggle between "Across" and "Down" in a flash.
* **Instant Gratification:** Get real-time color-coded feedback on your answers. No more guessing if you're right!
* **Modular Magic:** The code is split up (logic, UI, settings, puzzles, main), making it super easy to add your own themes or levels.

---

## 🛠️ Get Up and Running (in seconds!)

First, make sure you have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed. Once you have it, setting up the game is a breeze:

- **Clone the repo** (or download the files) and jump into the project folder.

- **Sync the project** (this handles everything):

   ```bash
   uv sync
   ```

- **Game on!** Run the game instantly:

   ```bash
   uv run main.py
   ```

* *(That's it. You're ready to start solving.)*

---

## 📁 Project Layout

```text
crossword/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── puzzle_submission.md
│   ├── pull_request_template.md
│   └── SECURITY.md
├── images/                 # Screenshots (Screenshot-1.png, Screenshot-2.png)
├── test/                   # Pytest suite (conftest.py, test_main.py, test_puzzles.py, test_settings.py)
├── .gitignore     
├── .python-version       
├── CODE_OF_CONDUCT.md                 
├── CONTRIBUTING.md               
├── crossword_logic.py      # Game engine / solving logic        
├── crossword_ui.py         # CustomTkinter interface      
├── LICENSE                
├── main.py                 # Entry point
├── puzzles.py              # Puzzle data
├── pyproject.toml          # uv project config & dependencies
├── README.md 
├── settings.py             # Config / themes
└── uv.lock                 # Locked dependency versions
```

---

## 🎮 How to Play

* **Click or Tab** to select your cell.
* **Type** to fill in the grid.
* **Escape** toggles your direction (Across/Down).
* **Check Answers** when you're feeling confident (or just desperate!).

---

## 📸 Screenshots of the Crossword Game

* Screenshot of the start of the game

![Screenshot-1](images/Screenshot-1.png)

* Screenshot of a completed game

![Screenshot-2](images/Screenshot-2.png)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
