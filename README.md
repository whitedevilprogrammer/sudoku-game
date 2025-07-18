# Sudoku Game 🧩

A professional, console-based Sudoku puzzle game written in Python.

---

## 📸 Showcase

- [Instagram Project Post](https://www.instagram.com/p/CY_8Y1-py69/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==)
  
## 🎬 Demo

- [Instagram Demo Video](https://www.instagram.com/reel/CY_6cVHB8iN/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==)


---

## Table of Contents

- [Features](#features)
- [Getting-Started](#getting-started)
- [How-to-Play](#how-to-play)
- [File-Structure](#file-structure)
- [Technologies-Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Automatic Sudoku Board Generation:**  
  Creates a new valid Sudoku puzzle each play.
- **Interactive Command-Line Interface:**  
  Intuitive input prompts and informative feedback.
- **Mistake Tracking:**  
  Game ends after 3 incorrect attempts.
- **Solution Reveal:**  
  Option to display the correct solution at any time.
- **Victory Detection:**  
  Recognizes and celebrates successful puzzle completion.
- **Detailed Instructions:**  
  Clear rules and input format provided for all players.

---

## Getting-Started

### Prerequisites

- Python 3.6 or higher

### Installation

Clone the repository:
```bash
git clone https://github.com/whitedevilprogrammer/sudoku-game.git
cd sudoku-game
```

### Running the Game

Simply execute:
```bash
python main_sudoku.py
```

---

## How-to-Play

1. **Read the Rules:**  
   The game starts by displaying Sudoku rules and an example board.

2. **Make Your Moves:**  
   Enter moves in the format:
   ```
   row column value
   ```
   For example: `9 6 3` inserts `3` at row 9, column 6.

3. **Mistake Limit:**  
   You are allowed up to 3 mistakes. On the third, the game ends with a summary.

4. **Reveal Solution:**  
   Type `show me answer` to display the correct solution board.

5. **Winning:**  
   Fill the entire board correctly to win the game!

---

## File-Structure

```
sudoku-game/
├── main_sudoku.py   # Main game logic & CLI interface
```

---

## Technologies-Used

- **Python** (Standard Library)
  - `random` for Sudoku generation and puzzle randomization

---

## Contributing

We welcome your contributions!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

Distributed under the MIT License.  
See [LICENSE](LICENSE) for more information.

---

## Contact

- Instagram: [@whitedevilprogrammer](https://www.instagram.com/whitedevilprogrammer)
- GitHub Issues: [Submit here](https://github.com/whitedevilprogrammer/sudoku-game/issues)

---

> _Enjoy challenging your mind and improving logic skills with Sudoku in your terminal!_
