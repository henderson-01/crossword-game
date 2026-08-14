import tkinter as tk
from unittest.mock import MagicMock, patch

import pytest

# Import the main app and puzzles
from main import CrosswordGame
from puzzles import PUZZLES

# --- Fixtures ---


@pytest.fixture(autouse=True)
def isolate_puzzles():
    """
    Automatically backs up and restores the global PUZZLES list for every test.
    """
    original = PUZZLES[:]
    yield
    PUZZLES[:] = original


@pytest.fixture
def app():
    """
    Creates a CrosswordGame instance for testing.
    Patches the mainloop to prevent the test from hanging.
    """
    # noinspection PyUnresolvedReferences
    with patch.object(CrosswordGame, "mainloop"):
        game = CrosswordGame()
        yield game
        try:
            game.destroy()
        except tk.TclError:
            pass


@pytest.fixture
def puzzle_data():
    """
    Returns a sample puzzle structure for testing logic without relying on external files.
    """
    return {
        "name": "Test Puzzle",
        "grid": [["A", "B", "C"], ["D", "B", "E"], ["F", "G", "H"]],
        "solution": [["A", "B", "C"], ["D", "B", "E"], ["F", "G", "H"]],
        "clues": {
            "across": [
                {"number": 1, "text": "Across Clue 1"},
                {"number": 3, "text": "Across Clue 3"},
            ],
            "down": [
                {"number": 1, "text": "Down Clue 1"},
                {"number": 2, "text": "Down Clue 2"},
            ],
        },
    }


# --- Tests ---


class TestCrosswordGameInit:
    def test_initialization(self, app):
        """Test that the game initializes with default values."""
        assert app.current_puzzle_idx == 0
        assert app.current_direction == "H"
        assert len(app.grid_cells) > 0
        assert app.puzzle_var.get() == PUZZLES[0]["name"]

    def test_ui_elements_exist(self, app):
        """Test that key UI components are created."""
        assert hasattr(app, "grid_panel")
        assert hasattr(app, "clues_panel")
        assert hasattr(app, "check_btn")
        assert hasattr(app, "status_label")


class TestPuzzleLoading:
    def test_load_puzzle_updates_state(self, app, puzzle_data):
        """Test that loading a puzzle updates the internal state."""
        PUZZLES[0] = puzzle_data
        app.load_puzzle(0)

        assert app.current_puzzle_idx == 0
        assert app.puzzle_var.get() == "Test Puzzle"
        assert len(app.clue_number_map) > 0
        assert len(app.grid_cells) > 0

    def test_load_puzzle_clears_widgets(self, app):
        """Test that loading a new puzzle properly resets and rebuilds widgets."""
        app.load_puzzle(0)

        if len(PUZZLES) > 1:
            app.load_puzzle(1)
            assert len(app.string_vars) > 0


class TestGridInteraction:
    def test_on_cell_focus(self, app, puzzle_data):
        """Test focusing a cell updates current_cell and highlights."""
        PUZZLES[0] = puzzle_data
        app.load_puzzle(0)

        app.on_cell_focus(0, 0)

        assert app.current_cell == (0, 0)
        assert app.active_clue_banner.cget("text") != "Select a cell to begin"

    def test_toggle_direction(self, app, puzzle_data):
        """Test toggling between Across and Down."""
        PUZZLES[0] = puzzle_data
        app.load_puzzle(0)

        assert app.current_direction == "H"
        app.toggle_direction()
        assert app.current_direction == "V"
        app.toggle_direction()
        assert app.current_direction == "H"


class TestKeyHandling:
    def test_type_character(self, app, puzzle_data):
        """Test typing a character into a cell."""
        PUZZLES[0] = puzzle_data
        app.load_puzzle(0)
        app.on_cell_focus(0, 0)

        mock_event = MagicMock()
        mock_event.keysym = "a"
        mock_event.char = "a"

        app._on_entry_key_press(mock_event)

        # Verify the character was successfully capitalized and inserted
        assert app.grid_cells[(0, 0)]["entry"].get() == "A"

    def test_backspace_execution(self, app, puzzle_data):
        """Test that the backspace event handler executes without throwing errors."""
        PUZZLES[0] = puzzle_data
        app.load_puzzle(0)
        app.on_cell_focus(0, 0)

        mock_event = MagicMock()
        mock_event.keysym = "BackSpace"

        # Simply call the method.
        # If an error occurs, Pytest will automatically catch it and fail the test.
        app._on_entry_key_press(mock_event)


class TestCheckAnswers:
    def test_check_answers_all_correct(self, app, puzzle_data):
        """Test checking answers when all are correct."""
        PUZZLES[0] = puzzle_data
        app.load_puzzle(0)

        # Fill the entire grid with correct answers
        for r in range(len(puzzle_data["grid"])):
            for c in range(len(puzzle_data["grid"][0])):
                if puzzle_data["grid"][r][c] != "B":
                    entry = app.grid_cells[(r, c)]["entry"]
                    entry.delete(0, "end")
                    entry.insert(0, puzzle_data["solution"][r][c])

        app.check_answers()
        status = app.status_label.cget("text")

        assert "perfect" in status.lower() or "correct" in status.lower()

    def test_check_answers_with_errors(self, app, puzzle_data):
        """Test checking answers with incorrect input."""
        PUZZLES[0] = puzzle_data
        app.load_puzzle(0)

        # Set one incorrect answer to trigger an error state
        entry = app.grid_cells[(0, 0)]["entry"]
        entry.delete(0, "end")
        entry.insert(0, "Z")

        app.check_answers()
        status = app.status_label.cget("text")

        assert (
            "0/" in status.lower()
            or "incorrect" in status.lower()
            or "error" in status.lower()
        )
