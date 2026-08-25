""" Crossword Puzzle Data

Contains the PUZZLES list a collection of mini-crossword definitions.
Each puzzle includes a grid layout W = white cell, B = black cell,
the solution, and across/down clues with numbers and text.
"""

PUZZLES = [
    {
        "name": "1. General Knowledge",
        "grid": [
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
        ],
        "solution": [
            ["A", "B", "O", "V", "E"],
            ["W", "B", "B", "B", "N"],
            ["A", "B", "U", "S", "E"],
            ["R", "B", "B", "B", "M"],
            ["D", "A", "I", "L", "Y"],
        ],
        "clues": {
            "across": [
                {"number": 1, "text": "At a higher level or overhead"},
                {"number": 3, "text": "To misuse or mistreat"},
                {"number": 4, "text": "Occurring every day"},
            ],
            "down": [
                {"number": 1, "text": "Prize or honor received"},
                {"number": 2, "text": "Adversary or opponent"},
            ],
        },
    },
    {
        "name": "2. Common Words",
        "grid": [
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
        ],
        "solution": [
            ["B", "A", "S", "I", "C"],
            ["R", "B", "B", "B", "A"],
            ["A", "C", "T", "O", "R"],
            ["N", "B", "B", "B", "R"],
            ["D", "E", "L", "A", "Y"],
        ],
        "clues": {
            "across": [
                {"number": 1, "text": "Fundamental or simple"},
                {"number": 3, "text": "Performer in a film or play"},
                {"number": 4, "text": "To postpone or put off"},
            ],
            "down": [
                {"number": 1, "text": "Company identity or trademark"},
                {"number": 2, "text": "To transport or convey"},
            ],
        },
    },
    {
        "name": "3. Travel & Nature",
        "grid": [
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
        ],
        "solution": [
            ["C", "A", "B", "I", "N"],
            ["H", "B", "B", "B", "E"],
            ["A", "F", "T", "E", "R"],
            ["S", "B", "B", "B", "V"],
            ["E", "A", "G", "L", "E"],
        ],
        "clues": {
            "across": [
                {"number": 1, "text": "Small wooden shelter"},
                {"number": 3, "text": "Following in time or order"},
                {"number": 4, "text": "Bird of prey with keen eyesight"},
            ],
            "down": [
                {"number": 1, "text": "To pursue or follow"},
                {"number": 2, "text": "Strength of mind or will"},
            ],
        },
    },
    {
        "name": "4. Actions",
        "grid": [
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
        ],
        "solution": [
            ["D", "A", "N", "C", "E"],
            ["R", "B", "B", "B", "N"],
            ["A", "D", "M", "I", "T"],
            ["M", "B", "B", "B", "E"],
            ["A", "L", "T", "E", "R"],
        ],
        "clues": {
            "across": [
                {"number": 1, "text": "To move rhythmically to music"},
                {"number": 3, "text": "To accept or confess something"},
                {"number": 4, "text": "To modify or change"},
            ],
            "down": [
                {"number": 1, "text": "Emotional performance piece"},
                {"number": 2, "text": "To go into or inside"},
            ],
        },
    },
    {
        "name": "5. Mixed bag (1)",
        "grid": [
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
        ],
        "solution": [
            ["F", "A", "I", "T", "H"],
            ["L", "B", "B", "B", "O"],
            ["A", "D", "U", "L", "T"],
            ["M", "B", "B", "B", "E"],
            ["E", "Q", "U", "A", "L"],
        ],
        "clues": {
            "across": [
                {"number": 1, "text": "Complete trust or belief"},
                {"number": 3, "text": "Grown-up person"},
                {"number": 4, "text": "The same in size or value"},
            ],
            "down": [
                {"number": 1, "text": "Bright burning gas from a fire"},
                {"number": 2, "text": "Place to stay overnight"},
            ],
        },
    },
    {
        "name": "6. Mixed Bag (2)",
        "grid": [
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
        ],
        "solution": [
            ["G", "H", "O", "S", "T"],
            ["R", "B", "B", "B", "O"],
            ["A", "G", "E", "N", "T"],
            ["N", "B", "B", "B", "A"],
            ["D", "E", "V", "I", "L"],
        ],
        "clues": {
            "across": [
                {"number": 1, "text": "Supernatural apparition"},
                {"number": 3, "text": "Representative or spy"},
                {"number": 4, "text": "Evil spirit or fiend"},
            ],
            "down": [
                {"number": 1, "text": "Magnificent and impressive"},
                {"number": 2, "text": "Sum or whole amount"},
            ],
        },
    },
    {
        "name": "7. Body & Mind",
        "grid": [
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
        ],
        "solution": [
            ["H", "A", "B", "I", "T"],
            ["E", "B", "B", "B", "I"],
            ["A", "L", "E", "R", "T"],
            ["R", "B", "B", "B", "L"],
            ["T", "H", "E", "M", "E"],
        ],
        "clues": {
            "across": [
                {"number": 1, "text": "Routine practice or custom"},
                {"number": 3, "text": "Watchful and quick to notice"},
                {"number": 4, "text": "Central topic or subject"},
            ],
            "down": [
                {"number": 1, "text": "Vital organ that pumps blood"},
                {"number": 2, "text": "Name or heading of a work"},
            ],
        },
    },
    {
        "name": "8. Science & Math",
        "grid": [
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
        ],
        "solution": [
            ["I", "D", "E", "A", "L"],
            ["M", "B", "B", "B", "I"],
            ["A", "L", "A", "R", "M"],
            ["G", "B", "B", "B", "I"],
            ["E", "I", "G", "H", "T"],
        ],
        "clues": {
            "across": [
                {"number": 1, "text": "Perfect example or standard"},
                {"number": 3, "text": "Warning signal or bell"},
                {"number": 4, "text": "Number after seven"},
            ],
            "down": [
                {"number": 1, "text": "Mental picture or concept"},
                {"number": 2, "text": "Smallest possible amount"},
            ],
        },
    },
    {
        "name": "9. Word Play",
        "grid": [
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
        ],
        "solution": [
            ["J", "E", "W", "E", "L"],
            ["U", "B", "B", "B", "U"],
            ["D", "O", "Z", "E", "N"],
            ["G", "B", "B", "B", "C"],
            ["E", "A", "R", "T", "H"],
        ],
        "clues": {
            "across": [
                {"number": 1, "text": "Precious stone or gem"},
                {"number": 3, "text": "Set of twelve"},
                {"number": 4, "text": "The planet we live on"},
            ],
            "down": [
                {"number": 1, "text": "To decide or evaluate"},
                {"number": 2, "text": "Midday meal"},
            ],
        },
    },
    {
        "name": "10. Mixed Bag (3)",
        "grid": [
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
            ["W", "B", "B", "B", "W"],
            ["W", "W", "W", "W", "W"],
        ],
        "solution": [
            ["E", "A", "G", "E", "R"],
            ["N", "B", "B", "B", "A"],
            ["A", "G", "A", "I", "N"],
            ["C", "B", "B", "B", "G"],
            ["T", "A", "S", "T", "E"],
        ],
        "clues": {
            "across": [
                {"number": 1, "text": "Keen or enthusiastic"},
                {"number": 3, "text": "Once more"},
                {"number": 4, "text": "Flavor or a small sample"},
            ],
            "down": [
                {"number": 1, "text": "To pass into law or perform"},
                {"number": 2, "text": "Extent or variety"},
            ],
        },
    },
]
