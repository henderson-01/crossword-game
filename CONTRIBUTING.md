# 🤝 Contributing to Crossword Project

First off, thank you for considering contributing to **Crossword**! 🧩

I want to make this the sleekest, fastest, and most enjoyable desktop crossword experience out there. Whether you're fixing a bug, tweaking the UI, or just dropping in a massive new puzzle pack, your help is incredibly appreciated.

## ⚡ Quick Start: The Dev Environment

I use [uv](https://astral.sh/uv/) because life is too short for slow installations. To get your development environment up and running:

1. **Fork and clone** this repository to your local machine.
2. **Navigate** to the project directory:

```bash
cd crossword

```

1. **Sync the project** to instantly grab all dependencies (like `CustomTkinter`):

```bash
uv sync

```

1. **Run the game** to make sure everything works:

```bash
uv run main.py

```

1. **Run the tests** to make sure your environment is set up correctly:

```bash
uv run pytest

```

All tests should pass. If they don't, check the Issues tab or ask for help before proceeding.

## 💡 How You Can Help

There are several ways you can level up Crossword. Here are the most common ways to contribute:

### 1. Adding New Puzzles (The Easiest Way to Start!)

You don't need to be a Python wizard to add new content. Puzzles are handled in `puzzles.py` using a simple JSON structure.

* Check out the existing formats in `puzzles.py`.
* Create your own crossword grid and clues.
* Submit a PR with your new puzzle pack! Make sure your clues are clever and your grids are solvable.

### 2. Squashing Bugs 🐛

Notice a typo? Did the grid crash when you hit a weird key combo?

* **Check the Issues tab** to see if it's already been reported.
* If not, open a new issue detailing how to reproduce the bug.
* If you know how to fix it, submit a Pull Request referencing the issue!

### 3. Feature Requests & UI Tweaks ✨

Have an idea for a new feature (like a timer, a hint system, or a new color scheme for `settings.py`)?

* Please open an issue to discuss your idea *before* you spend hours coding it. We want to make sure it aligns with the dark-mode-first, high-performance vision of the game.

## 🛠️ The Pull Request Process

Ready to submit your code? Awesome. Here is the workflow:

1. **Create a branch** for your feature or bugfix:

```bash
git checkout -b feature/your-amazing-feature

```

1. **Make your changes.** Keep your code clean, readable, and Pythonic. If you are modifying the UI, ensure it still looks great in our signature dark mode.
2. **Commit your changes** with a clear, descriptive commit message:

```bash
git commit -m "Add: New 10x10 Sci-Fi puzzle pack"

```

1. **Run the tests and linter** before pushing:

```bash
uv run pytest
uv run ruff check .

```

Make sure all tests pass and there are no linting errors. If you're adding a new feature or fixing a bug, please include tests for your changes.

1. **Push to your fork:**

```bash
git push origin feature/your-amazing-feature

```

1. **Open a Pull Request** against our `main` branch. Provide a brief description of what you changed and why. If it's a visual change (like a UI tweak), a screenshot in the PR description is highly encouraged!

## 📜 Coding Guidelines

* **Keep it modular:** Respect the project layout. UI/Game logic stays in `main.py`, configurations belong in `settings.py`, and data goes in `puzzles.py`.
* **Performance matters:** Crossword is built for speed. Avoid blocking the main `CustomTkinter` event loop with heavy synchronous tasks.
* **Be kind:** We're all here to build something fun. Be respectful in your issue reports and code reviews.

## 🧪 Testing

* Tests live in the `test/` directory.
* Run all tests with `uv run pytest`.
* New features and bugfixes should include tests where applicable.
* **All tests must pass before a PR is merged.** If your PR breaks existing tests, please fix them before requesting a review.

---

*Thanks for helping us build Crossword. Happy coding!* 💻🚀
