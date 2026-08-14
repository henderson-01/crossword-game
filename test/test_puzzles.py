from puzzles import PUZZLES


class TestPuzzleDataIntegrity:
    """Tests to ensure all puzzle data is well-formed and consistent."""

    def test_puzzles_is_not_empty(self):
        assert len(PUZZLES) > 0, "PUZZLES list should not be empty"

    def test_each_puzzle_has_required_keys(self):
        for i, puzzle in enumerate(PUZZLES):
            assert "name" in puzzle, f"Puzzle {i} missing 'name'"
            assert "grid" in puzzle, f"Puzzle {i} missing 'grid'"
            assert "solution" in puzzle, f"Puzzle {i} missing 'solution'"
            assert "clues" in puzzle, f"Puzzle {i} missing 'clues'"

    def test_grid_is_rectangular(self):
        for i, puzzle in enumerate(PUZZLES):
            grid = puzzle["grid"]
            if not grid:
                continue
            row_len = len(grid[0])
            for j, row in enumerate(grid):
                assert len(row) == row_len, (
                    f"Puzzle {i} ('{puzzle['name']}'): Row {j} has length {len(row)}, expected {row_len}"
                )

    def test_solution_matches_grid_dimensions(self):
        for i, puzzle in enumerate(PUZZLES):
            grid = puzzle["grid"]
            solution = puzzle["solution"]
            assert len(grid) == len(solution), (
                f"Puzzle {i}: Grid rows ({len(grid)}) != Solution rows ({len(solution)})"
            )
            for r in range(len(grid)):
                assert len(grid[r]) == len(solution[r]), (
                    f"Puzzle {i}: Row {r} width mismatch"
                )

    def test_grid_and_solution_chars_match_structure(self):
        for i, puzzle in enumerate(PUZZLES):
            grid = puzzle["grid"]
            solution = puzzle["solution"]
            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    grid_char = grid[r][c]
                    sol_char = solution[r][c]
                    if grid_char == "B":
                        assert sol_char == "B", (
                            f"Puzzle {i} ({r},{c}): Grid is 'B' but Solution is '{sol_char}'"
                        )
                    else:
                        assert sol_char.isalpha() and sol_char.isupper(), (
                            f"Puzzle {i} ({r},{c}): Solution '{sol_char}' is not an uppercase letter"
                        )

    def test_clues_are_valid(self):
        for i, puzzle in enumerate(PUZZLES):
            clues = puzzle.get("clues", {})
            for direction in ["across", "down"]:
                if direction not in clues:
                    continue
                for j, clue in enumerate(clues[direction]):
                    assert "number" in clue, (
                        f"Puzzle {i} {direction} clue {j} missing 'number'"
                    )
                    assert "text" in clue, (
                        f"Puzzle {i} {direction} clue {j} missing 'text'"
                    )
                    assert isinstance(clue["number"], int)
                    assert isinstance(clue["text"], str)

    def test_clue_numbers_are_unique_per_direction(self):
        for i, puzzle in enumerate(PUZZLES):
            clues = puzzle.get("clues", {})
            for direction in ["across", "down"]:
                if direction not in clues:
                    continue
                numbers = [c["number"] for c in clues[direction]]
                assert len(numbers) == len(set(numbers)), (
                    f"Puzzle {i} {direction}: Duplicate clue numbers found"
                )


class TestPuzzleSpecifics:
    def test_first_puzzle_name(self):
        from puzzles import PUZZLES

        assert PUZZLES[0]["name"] == "1. General Knowledge"

    def test_grid_size_consistency(self):
        from puzzles import PUZZLES

        for i, puzzle in enumerate(PUZZLES):
            grid = puzzle["grid"]
            rows = len(grid)
            for row in grid:
                assert len(row) == rows, f"Puzzle {i} is not a square grid"
