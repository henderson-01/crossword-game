""" Crossword Logic

Core game logic for the crossword application. The CrosswordLogic class manages
puzzle state, cell navigation, direction toggling, keyboard input, and answer
validation. Designed to be combined with a UI mixin CrosswordUI that provides
_build_grid() and _populate_clues() at runtime.

Responsibilities:
  - Loading and resetting puzzles grid, clues, UI state
  - Navigating between cells typing, backspace, arrow keys, Enter, Escape
  - Highlighting the active word and its corresponding clue
  - Toggling between Across and Down direction
  - Validating user answers against the puzzle solution
"""

import tkinter as tk
from typing import TYPE_CHECKING, Any, Literal

import customtkinter as ctk

from puzzles import PUZZLES
from settings import COLORS

Direction = Literal["H", "V"]


class CrosswordLogic:
    current_puzzle_idx: int
    puzzle_var: ctk.StringVar
    current_cell: tuple[int, int] | None
    current_direction: Direction
    clue_number_map: dict[tuple[int, int], int]
    clue_texts: dict[str, dict[int, str]]
    clue_btns: dict[str, dict[int, ctk.CTkButton]]
    string_vars: dict[tuple[int, int], tk.StringVar]
    grid_frame: ctk.CTkFrame
    across_scroll: ctk.CTkScrollableFrame
    down_scroll: ctk.CTkScrollableFrame
    status_label: ctk.CTkLabel
    active_clue_banner: ctk.CTkLabel
    dir_label: ctk.CTkLabel
    grid_cells: dict[tuple[int, int], dict[str, Any]]

    if TYPE_CHECKING:
        # Methods provided by CrosswordUI mixin at runtime.
        def _build_grid(self) -> None: ...
        def _populate_clues(self) -> None: ...

    def load_puzzle(self, idx: int) -> None:
        self.current_puzzle_idx = idx
        self.puzzle_var.set(PUZZLES[idx]["name"])
        self.current_cell = None
        self.current_direction = "H"
        self.clue_number_map = {}
        self.clue_texts = {"H": {}, "V": {}}
        self.clue_btns = {"H": {}, "V": {}}
        self.string_vars = {}

        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        for widget in self.across_scroll.winfo_children():
            widget.destroy()
        for widget in self.down_scroll.winfo_children():
            widget.destroy()

        self.status_label.configure(text="")
        self.active_clue_banner.configure(
            text="Select a cell to begin", text_color=COLORS["text_muted"]
        )

        self._build_grid()
        self._populate_clues()
        self.dir_label.configure(text="Direction: Across")

    def on_clue_click(self, number: int, direction: Direction) -> None:
        if self.current_direction != direction:
            self.current_direction = direction
            self.dir_label.configure(
                text=f"Direction: {'Down' if direction == 'V' else 'Across'}"
            )

        target_cell: tuple[int, int] | None = None
        for (cr, cc), num in self.clue_number_map.items():
            if num == number:
                target_cell = (cr, cc)
                break

        if target_cell and target_cell in self.grid_cells:
            self.current_cell = target_cell
            self.grid_cells[target_cell]["entry"].focus_set()
            self.highlight_current_word()

    def on_cell_focus(self, r: int, c: int) -> None:
        self.current_cell = (r, c)
        self.highlight_current_word()

    def highlight_current_word(self) -> None:
        if not self.current_cell:
            return

        self._reset_all_highlights()

        r, c = self.current_cell
        start_r, start_c, end_r, end_c = self._get_word_bounds(r, c)

        word_cells = self._get_word_cells(start_r, start_c, end_r, end_c)
        self._highlight_cells(word_cells, COLORS["word_hl"])

        self.grid_cells[(r, c)]["frame"].configure(fg_color=COLORS["cell_hl"])

        self._update_active_clue(start_r, start_c)

    def _reset_all_highlights(self) -> None:
        for cell_data in self.grid_cells.values():
            cell_data["frame"].configure(fg_color=COLORS["cell_empty"])

        for d in ["H", "V"]:
            for btn in self.clue_btns[d].values():
                btn.configure(fg_color="transparent", text_color=COLORS["text_main"])

    def _get_word_bounds(self, r: int, c: int) -> tuple[int, int, int, int]:
        puzzle = PUZZLES[self.current_puzzle_idx]
        rows = len(puzzle["grid"])
        cols = len(puzzle["grid"][0])

        start_r, start_c = r, c
        end_r, end_c = r, c

        if self.current_direction == "H":
            while start_c > 0 and puzzle["grid"][r][start_c - 1] != "B":
                start_c -= 1
            while end_c < cols - 1 and puzzle["grid"][r][end_c + 1] != "B":
                end_c += 1
        else:
            while start_r > 0 and puzzle["grid"][start_r - 1][c] != "B":
                start_r -= 1
            while end_r < rows - 1 and puzzle["grid"][end_r + 1][c] != "B":
                end_r += 1

        return start_r, start_c, end_r, end_c

    def _get_word_cells(
        self, start_r: int, start_c: int, end_r: int, end_c: int
    ) -> list[tuple[int, int]]:
        cells = []
        if self.current_direction == "H":
            for col in range(start_c, end_c + 1):
                if (start_r, col) in self.grid_cells:
                    cells.append((start_r, col))
        else:
            for row in range(start_r, end_r + 1):
                if (row, start_c) in self.grid_cells:
                    cells.append((row, start_c))
        return cells

    def _highlight_cells(self, cells: list[tuple[int, int]], color: str) -> None:
        for cell in cells:
            self.grid_cells[cell]["frame"].configure(fg_color=color)

    def _update_active_clue(self, start_r: int, start_c: int) -> None:
        clue_num = self.clue_number_map.get((start_r, start_c))

        if clue_num and clue_num in self.clue_texts[self.current_direction]:
            dir_text = "Across" if self.current_direction == "H" else "Down"
            clue_text = self.clue_texts[self.current_direction][clue_num]
            self.active_clue_banner.configure(
                text=f"{clue_num or ''} {dir_text or ''}: {clue_text or ''}",
                text_color=COLORS["text_main"],
            )
            active_btn = self.clue_btns[self.current_direction][clue_num]
            active_btn.configure(fg_color=COLORS["word_hl"], text_color="#FFFFFF")

    def toggle_direction(self) -> None:
        self.current_direction = "V" if self.current_direction == "H" else "H"
        self.dir_label.configure(
            text=f"Direction: {'Down' if self.current_direction == 'V' else 'Across'}"
        )
        self.highlight_current_word()

    def _on_key_press(self, event: tk.Event) -> None:
        if event.keysym == "Escape":
            self.toggle_direction()

    def _on_entry_key_press(self, event: tk.Event) -> str | None:
        if not self.current_cell:
            return None

        r, c = self.current_cell
        entry = self.grid_cells[(r, c)]["entry"]

        if event.keysym == "BackSpace":
            if entry.get() == "":
                self.move_cursor(-1)
            else:
                entry.delete(0, tk.END)
            return None

        if event.keysym == "Return":
            self.move_cursor(1)
            return None

        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.move_cursor_arrow(event.keysym)
            return None

        char = event.char
        if len(char) == 1 and char.isalpha():
            entry.delete(0, tk.END)
            entry.insert(0, char.upper())
            self.move_cursor(1)
            return "break"
        return None

    def move_cursor(self, step: int) -> None:
        if not self.current_cell:
            return
        r, c = self.current_cell
        puzzle = PUZZLES[self.current_puzzle_idx]
        rows, cols = len(puzzle["grid"]), len(puzzle["grid"][0])

        while True:
            if self.current_direction == "H":
                c += step
                if c < 0 or c >= cols or puzzle["grid"][r][c] == "B":
                    return
            else:
                r += step
                if r < 0 or r >= rows or puzzle["grid"][r][c] == "B":
                    return

            if (r, c) in self.grid_cells:
                self.current_cell = (r, c)
                self.grid_cells[(r, c)]["entry"].focus_set()
                self.highlight_current_word()
                break

    def move_cursor_arrow(self, direction: str) -> None:
        if not self.current_cell:
            return
        r, c = self.current_cell
        puzzle = PUZZLES[self.current_puzzle_idx]
        rows, cols = len(puzzle["grid"]), len(puzzle["grid"][0])

        deltas: dict[str, tuple[int, int]] = {
            "Up": (-1, 0),
            "Down": (1, 0),
            "Left": (0, -1),
            "Right": (0, 1),
        }
        r += deltas[direction][0]
        c += deltas[direction][1]

        if 0 <= r < rows and 0 <= c < cols and puzzle["grid"][r][c] != "B":
            self.current_cell = (r, c)
            self.grid_cells[(r, c)]["entry"].focus_set()
            self.highlight_current_word()

    def on_puzzle_select(self, value: str) -> None:
        for i, p in enumerate(PUZZLES):
            if p["name"] == value:
                self.load_puzzle(i)
                break

    def check_answers(self) -> None:
        puzzle = PUZZLES[self.current_puzzle_idx]
        correct_count = 0
        total_white_cells = len(self.grid_cells)
        total_filled_cells = 0

        for cell_data in self.grid_cells.values():
            cell_data["frame"].configure(fg_color=COLORS["cell_empty"])

        for (r, c), cell_data in self.grid_cells.items():
            expected = puzzle["solution"][r][c].upper()
            user_char = cell_data["entry"].get().upper()

            if user_char == "":
                continue

            total_filled_cells += 1
            if user_char == expected:
                correct_count += 1
                cell_data["frame"].configure(fg_color=COLORS["correct"])
            else:
                cell_data["frame"].configure(fg_color=COLORS["incorrect"])

        self._update_status_display(
            correct_count, total_white_cells, total_filled_cells
        )

    def _update_status_display(
        self, correct_count: int, total_white_cells: int, total_filled_cells: int
    ) -> None:
        if correct_count == total_white_cells:
            self.status_label.configure(
                text="✓ Perfect! All answers correct.", text_color="#4ade80"
            )
        elif total_filled_cells == 0:
            self.status_label.configure(
                text="Fill in the grid to begin!", text_color=COLORS["text_muted"]
            )
        else:
            self.status_label.configure(
                text=f"{correct_count}/{total_white_cells} correct",
                text_color="#fb923c",
            )
