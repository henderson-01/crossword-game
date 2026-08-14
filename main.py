from __future__ import annotations

import tkinter as tk
from typing import Any

import customtkinter as ctk

from crossword_logic import CrosswordLogic, Direction
from crossword_ui import CrosswordUI
from settings import APP_TITLE, COLORS, WINDOW_GEOMETRY, WINDOW_MIN_SIZE


class CrosswordGame(ctk.CTk, CrosswordUI, CrosswordLogic):
    current_puzzle_idx: int
    grid_cells: dict[tuple[int, int], dict[str, Any]]
    current_direction: Direction
    current_cell: tuple[int, int] | None
    clue_number_map: dict[tuple[int, int], int]
    clue_texts: dict[str, dict[int, str]]
    clue_btns: dict[str, dict[int, ctk.CTkButton]]
    string_vars: dict[tuple[int, int], tk.StringVar]

    puzzle_var: ctk.StringVar
    puzzle_menu: ctk.CTkOptionMenu
    grid_panel: ctk.CTkFrame
    active_clue_banner: ctk.CTkLabel
    grid_frame: ctk.CTkFrame
    check_btn: ctk.CTkButton
    status_label: ctk.CTkLabel
    dir_label: ctk.CTkLabel
    clues_panel: ctk.CTkFrame
    across_scroll: ctk.CTkScrollableFrame
    down_scroll: ctk.CTkScrollableFrame

    def __init__(self) -> None:
        super().__init__()

        self.title(APP_TITLE)
        self.geometry(WINDOW_GEOMETRY)
        self.minsize(*WINDOW_MIN_SIZE)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        ctk.set_appearance_mode("Dark")
        self.configure(fg_color=COLORS["bg"])
        self.current_puzzle_idx = 0
        self.grid_cells = {}
        self.current_direction = "H"
        self.current_cell = None
        self.clue_number_map = {}
        self.clue_texts = {"H": {}, "V": {}}
        self.clue_btns = {"H": {}, "V": {}}
        self.string_vars = {}
        self.setup_ui()
        self.load_puzzle(0)


if __name__ == "__main__":
    app = CrosswordGame()
    app.mainloop()
