from settings import APP_TITLE, COLORS, WINDOW_GEOMETRY, WINDOW_MIN_SIZE


class TestAppConfiguration:
    def test_app_title_is_string(self):
        assert isinstance(APP_TITLE, str), "APP_TITLE must be a string"
        assert len(APP_TITLE) > 0, "APP_TITLE must not be empty"
        assert "Crossword" in APP_TITLE, "APP_TITLE should contain 'Crossword'"

    def test_window_geometry_format(self):
        assert isinstance(WINDOW_GEOMETRY, str), "WINDOW_GEOMETRY must be a string"
        parts = WINDOW_GEOMETRY.lower().split("x")
        assert len(parts) == 2, f"WINDOW_GEOMETRY '{WINDOW_GEOMETRY}' must be in 'width x height' format"
        assert parts[0].isdigit() and parts[1].isdigit(), "Geometry bounds must be valid integers"

    def test_window_min_size_is_tuple(self):
        assert isinstance(WINDOW_MIN_SIZE, tuple), "WINDOW_MIN_SIZE must be a tuple"
        assert len(WINDOW_MIN_SIZE) == 2, "WINDOW_MIN_SIZE must contain exactly two values (width, height)"
        min_w, min_h = WINDOW_MIN_SIZE
        assert min_w > 0 and min_h > 0, "Minimum bounds must be positive"

    def test_min_size_is_smaller_than_geometry(self):
        width_parts = WINDOW_GEOMETRY.lower().split("x")
        init_w, init_h = int(width_parts[0]), int(width_parts[1])
        min_w, min_h = WINDOW_MIN_SIZE
        assert min_w <= init_w, f"Minimum width ({min_w}) cannot be greater than initial width ({init_w})"
        assert min_h <= init_h, f"Minimum height ({min_h}) cannot be greater than initial height ({init_h})"


class TestColorPalette:
    def test_colors_is_dictionary(self):
        assert isinstance(COLORS, dict), "COLORS must be a dictionary"

    def test_colors_are_valid_hex_codes(self):
        for key, value in COLORS.items():
            assert isinstance(value, str), f"Color '{key}' must be a string"
            assert value.startswith("#"), f"Color '{key}' must start with '#'"
            assert len(value[1:]) == 6, f"Color '{key}' hex code '{value}' must be 6 characters long"
            assert all(c in "0123456789abcdefABCDEF" for c in value[1:]), f"Color '{key}' contains invalid hex characters"

    def test_required_color_keys_exist(self):
        required_keys = {
            "bg", "panel", "grid_grout", "cell_B", "cell_empty",
            "word_hl", "cell_hl", "text_main", "text_muted",
            "accent", "correct", "incorrect",
        }
        missing_keys = required_keys - set(COLORS.keys())
        assert not missing_keys, f"Missing required color keys: {missing_keys}"

    def test_color_values_are_distinct(self):
        assert COLORS["cell_empty"] != COLORS["cell_B"], "Empty cells and Blocked cells must have different colors"
        assert COLORS["correct"] != COLORS["incorrect"], "Correct and Incorrect states must have different colors"
        assert COLORS["word_hl"] != COLORS["cell_hl"], "Word highlight and Cell highlight must be different"