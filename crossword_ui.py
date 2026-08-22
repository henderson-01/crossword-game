""" Crossword UI User Interface Mixin

Provides the CrosswordUI mixin responsible for constructing the entire
crossword interface: a top bar puzzle selector, grid panel clue
banner, interactive cell grid, controls, and a clues panel Across
and Down lists.

When combined with CrosswordLogic via multiple inheritance, this class
supplies _build_grid() and _populate_clues() at runtime.
"""

import tkinter as tk
from typing import TYPE_CHECKING, Any

import customtkinter as ctk

from puzzles import PUZZLES
from settings import COLORS

if TYPE_CHECKING:
    from crossword_logic import Direction


class CrosswordUI:
    current_puzzle_idx: int
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
    grid_cells: dict[tuple[int, int], dict[str, Any]]
    clue_number_map: dict[tuple[int, int], int]
    string_vars: dict[tuple[int, int], tk.StringVar]
    clue_texts: dict[str, dict[int, str]]
    clue_btns: dict[str, dict[int, ctk.CTkButton]]
    current_direction: str
    current_cell: tuple[int, int] | None

    if TYPE_CHECKING:
        # Methods provided by CrosswordLogic mixin / ctk.CTk at runtime.
        def on_puzzle_select(self, value: str) -> None: ...
        def check_answers(self) -> None: ...
        def _on_key_press(self, event: tk.Event) -> None: ...
        def toggle_direction(self) -> None: ...
        def on_cell_focus(self, r: int, c: int) -> None: ...
        def on_clue_click(self, number: int, direction: Direction) -> None: ...
        def _on_entry_key_press(self, event: tk.Event) -> str | None: ...
        def bind(
            self,
            sequence: str | None = None,
            func: Any | None = None,
            add: bool | str | None = None,
        ) -> str: ...

    def setup_ui(self) -> None:
        top_frame = ctk.CTkFrame(
            self, fg_color=COLORS["panel"], corner_radius=0, height=60
        )
        top_frame.grid(row=0, column=0, sticky="ew")
        top_frame.grid_columnconfigure(1, weight=1)

        title_lbl = ctk.CTkLabel(
            top_frame,
            text="CROSSWORD",
            font=("Helvetica", 20, "bold"),
            text_color=COLORS["accent"],
        )
        title_lbl.grid(row=0, column=0, sticky="w", padx=25, pady=15)

        selector_frame = ctk.CTkFrame(top_frame, fg_color="transparent")
        selector_frame.grid(row=0, column=2, sticky="e", padx=25)

        ctk.CTkLabel(
            selector_frame,
            text="Puzzle:",
            font=("Helvetica", 14),
            text_color=COLORS["text_muted"],
        ).pack(side="left", padx=(0, 10))

        self.puzzle_var = ctk.StringVar(value=PUZZLES[0]["name"])
        self.puzzle_menu = ctk.CTkOptionMenu(
            selector_frame,
            values=[p["name"] for p in PUZZLES],
            variable=self.puzzle_var,
            command=self.on_puzzle_select,
            width=250,
            font=("Helvetica", 13),
            fg_color=COLORS["bg"],
            button_color=COLORS["bg"],
            button_hover_color=COLORS["cell_empty"],
        )
        self.puzzle_menu.pack(side="left")

        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.grid(row=1, column=0, sticky="nsew", padx=25, pady=25)

        main_frame.grid_columnconfigure(0, weight=5)
        main_frame.grid_columnconfigure(1, weight=3)
        main_frame.grid_rowconfigure(0, weight=1)

        self.grid_panel = ctk.CTkFrame(
            main_frame, fg_color=COLORS["panel"], corner_radius=12
        )
        self.grid_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        self.grid_panel.grid_columnconfigure(0, weight=1)
        self.grid_panel.grid_rowconfigure(1, weight=1)

        self.active_clue_banner = ctk.CTkLabel(
            self.grid_panel,
            text="Select a cell to begin",
            font=("Helvetica", 18, "bold"),
            text_color=COLORS["accent"],
            anchor="center",
            corner_radius=8,
            fg_color=COLORS["bg"],
        )
        self.active_clue_banner.grid(
            row=0, column=0, sticky="ew", padx=20, pady=(20, 0), ipady=10
        )

        self.grid_frame = ctk.CTkFrame(
            self.grid_panel, fg_color=COLORS["grid_grout"], corner_radius=0
        )
        self.grid_frame.grid(row=1, column=0, padx=20, pady=20)

        ctrl_frame = ctk.CTkFrame(self.grid_panel, fg_color="transparent")
        ctrl_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 20))

        self.check_btn = ctk.CTkButton(
            ctrl_frame,
            text="✓ Check Answers",
            command=self.check_answers,
            font=("Helvetica", 14, "bold"),
            fg_color=COLORS["accent"],
            hover_color="#2A70A6",
            height=40,
        )
        self.check_btn.pack(side="left")

        self.status_label = ctk.CTkLabel(
            ctrl_frame,
            text="",
            font=("Helvetica", 14),
            text_color=COLORS["text_main"],
        )
        self.status_label.pack(side="left", padx=15)

        self.dir_label = ctk.CTkLabel(
            ctrl_frame,
            text="Direction: Across",
            font=("Helvetica", 13),
            text_color=COLORS["text_muted"],
        )
        self.dir_label.pack(side="right")

        self.clues_panel = ctk.CTkFrame(main_frame, fg_color="transparent")
        self.clues_panel.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        self.clues_panel.grid_columnconfigure(0, weight=1)
        self.clues_panel.grid_rowconfigure(1, weight=1)
        self.clues_panel.grid_rowconfigure(3, weight=1)

        ctk.CTkLabel(
            self.clues_panel, text="Across", font=("Helvetica", 16, "bold"), anchor="w"
        ).grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.across_scroll = ctk.CTkScrollableFrame(
            self.clues_panel,
            fg_color=COLORS["panel"],
            corner_radius=10,
            scrollbar_button_color=COLORS["cell_empty"],
        )
        self.across_scroll.grid(row=1, column=0, sticky="nsew", pady=(0, 15))

        ctk.CTkLabel(
            self.clues_panel, text="Down", font=("Helvetica", 16, "bold"), anchor="w"
        ).grid(row=2, column=0, sticky="w", pady=(0, 5))

        self.down_scroll = ctk.CTkScrollableFrame(
            self.clues_panel,
            fg_color=COLORS["panel"],
            corner_radius=10,
            scrollbar_button_color=COLORS["cell_empty"],
        )
        self.down_scroll.grid(row=3, column=0, sticky="nsew")

        self.bind("<Key>", self._on_key_press)
        self.bind("<Escape>", lambda e: self.toggle_direction())

    def _build_grid(self) -> None:
        puzzle = PUZZLES[self.current_puzzle_idx]
        rows = len(puzzle["grid"])
        cols = len(puzzle["grid"][0])

        self.grid_cells = {}
        clue_map: dict[tuple[int, int], int] = {}
        current_num = 1

        for r in range(rows):
            for c in range(cols):
                if puzzle["grid"][r][c] == "B":
                    continue
                is_across_start = (
                    (c == 0 or puzzle["grid"][r][c - 1] == "B")
                    and c + 1 < cols
                    and puzzle["grid"][r][c + 1] != "B"
                )
                is_down_start = (
                    (r == 0 or puzzle["grid"][r - 1][c] == "B")
                    and r + 1 < rows
                    and puzzle["grid"][r + 1][c] != "B"
                )

                if is_across_start or is_down_start:
                    clue_map[(r, c)] = current_num
                    current_num += 1

        for r in range(rows):
            for c in range(cols):
                cell_type = puzzle["grid"][r][c]

                cell_frame = ctk.CTkFrame(
                    self.grid_frame, corner_radius=0, width=42, height=42
                )
                cell_frame.grid(row=r, column=c, padx=1, pady=1)
                cell_frame.grid_propagate(False)

                if cell_type == "B":
                    cell_frame.configure(fg_color=COLORS["cell_B"])
                else:
                    cell_frame.configure(fg_color=COLORS["cell_empty"])

                if (r, c) in clue_map:
                    num_label = ctk.CTkLabel(
                        cell_frame,
                        text=str(clue_map[(r, c)]),
                        font=("Helvetica", 10, "bold"),
                        text_color=COLORS["text_muted"],
                    )
                    num_label.place(x=3, y=1)

                var = tk.StringVar()
                self.string_vars[(r, c)] = var
                entry = ctk.CTkEntry(
                    cell_frame,
                    font=("Helvetica", 18, "bold"),
                    justify="center",
                    textvariable=var,
                    border_width=0,
                    fg_color="transparent",
                    text_color=COLORS["text_main"],
                    corner_radius=0,
                )
                entry.place(
                    relx=0.5, rely=0.55, anchor="center", relwidth=1.0, relheight=0.8
                )

                entry.bind(
                    "<FocusIn>", lambda e, row=r, col=c: self.on_cell_focus(row, col)
                )
                entry.bind("<Key>", self._on_entry_key_press)
                entry.bind("<KeyPress>", lambda e: self.status_label.configure(text=""))

                self.grid_cells[(r, c)] = {
                    "entry": entry,
                    "frame": cell_frame,
                    "row": r,
                    "col": c,
                }

        self.clue_number_map = clue_map

    def _populate_clues(self) -> None:
        puzzle = PUZZLES[self.current_puzzle_idx]
        if "clues" not in puzzle:
            return

        across_data = sorted(
            puzzle["clues"].get("across", []), key=lambda x: x.get("number", 0)
        )
        down_data = sorted(
            puzzle["clues"].get("down", []), key=lambda x: x.get("number", 0)
        )

        for clue in across_data:
            num = clue["number"]
            text = clue["text"]
            self.clue_texts["H"][num] = text

            btn = ctk.CTkButton(
                self.across_scroll,
                text=f"{num}. {text}",
                font=("Helvetica", 13),
                anchor="w",
                fg_color="transparent",
                text_color=COLORS["text_main"],
                hover_color=COLORS["cell_empty"],
                command=lambda n=num: self.on_clue_click(n, "H"),
            )
            btn.pack(fill="x", pady=2, padx=5)
            self.clue_btns["H"][num] = btn

        for clue in down_data:
            num = clue["number"]
            text = clue["text"]
            self.clue_texts["V"][num] = text

            btn = ctk.CTkButton(
                self.down_scroll,
                text=f"{num}. {text}",
                font=("Helvetica", 13),
                anchor="w",
                fg_color="transparent",
                text_color=COLORS["text_main"],
                hover_color=COLORS["cell_empty"],
                command=lambda n=num: self.on_clue_click(n, "V"),
            )
            btn.pack(fill="x", pady=2, padx=5)
            self.clue_btns["V"][num] = btn
