
# Unbeatable Noughts and Crosses 🕹️

A Python-based **Tic Tac Toe** game with an unbeatable AI opponent, player score tracking, and leaderboard functionality. Challenge yourself against the computer and track your progress over multiple sessions!

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Gameplay](#gameplay)
- [Installation](#installation)
- [Usage](#usage)
- [Leaderboard](#leaderboard)
- [Author](#author)
- [License](#license)

---

## Overview
This project implements **Tic Tac Toe** (also known as **Noughts and Crosses**) in Python. The game includes:

- Unbeatable AI opponent.
- User-friendly console interface.
- Score saving and leaderboard tracking.
- Option to play multiple games in one session.

The AI uses a simple scoring algorithm to **block the player and maximize its chances of winning**, making it almost impossible to beat.

---

## Features
- **Single-player mode**: Play against an intelligent AI.
- **Score tracking**: Keep a cumulative score for your session.
- **Leaderboard**: Save and view top scores in a JSON-based leaderboard.
- **Input validation**: Only accepts valid moves (1–9) and prevents overwriting moves.
- **File handling**: Scores are persisted between sessions.

---

## Gameplay
1. Run the game.
2. The board will display numbers 1–9 representing positions.
3. Enter a number to place your `X` on the board.
4. The computer (`O`) will make its move automatically.
5. The first to get **three in a row** (horizontally, vertically, or diagonally) wins.
6. If all positions are filled without a winner, the game ends in a draw.

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/unbeatable-noughts-and-crosses.git
cd unbeatable-noughts-and-crosses
````

2. Ensure you have **Python 3.x** installed.

3. Run the game:

```bash
python main.py
```

---

## Usage

* Select **Play Game** from the menu.
* Input your move by entering a number (1–9).
* After each game, you can choose to **save your score**, **view the leaderboard**, or **quit**.

---

## Leaderboard

* Scores are saved in `leaderboard.txt` using JSON format.
* When saving, the player's total score is accumulated.
* Top 10 scores are displayed in descending order.

---

## Author

**Suraj Poddar**




