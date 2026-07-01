# 🎮 Tic-Tac-Toe AI using Minimax Algorithm

A Python-based Tic-Tac-Toe game where a human player competes against an AI opponent. The AI uses the **Minimax algorithm**, making it an unbeatable player by evaluating all possible game states and selecting the optimal move.

## 📌 Project Overview

This project demonstrates the implementation of **Artificial Intelligence** in a classic Tic-Tac-Toe game. The AI analyzes the game board using the Minimax algorithm to determine the best possible move, ensuring optimal gameplay.

## ✨ Features

* Human vs AI gameplay
* Unbeatable AI using the Minimax algorithm
* Command-line interface
* Input validation for user moves
* Win, lose, and draw detection
* Clean and easy-to-understand Python implementation

## 🛠️ Technologies Used

* Python 3
* Standard Python Libraries

  * `math`

## 📂 Project Structure

```text
TicTacToe-AI/
│── tictactoe.py
│── README.md
│── requirements.txt
```

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/tictactoe-ai.git
```

2. Navigate to the project directory:

```bash
cd tictactoe-ai
```

3. Run the program:

```bash
python tictactoe.py
```

## 🎮 How to Play

* You play as **X**.
* The AI plays as **O**.
* Enter a number from **1 to 9** to place your mark.

Board positions:

```text
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

The game ends when:

* A player gets three marks in a row.
* The board is full, resulting in a draw.

## 🧠 Algorithm Used

### Minimax Algorithm

The Minimax algorithm is a decision-making algorithm used in two-player games. It explores all possible future game states and chooses the move that maximizes the AI's chances of winning while minimizing the opponent's chances.

### Working Process

1. Generate all possible moves.
2. Simulate each move recursively.
3. Evaluate terminal states (win, lose, or draw).
4. Assign scores to each outcome.
5. Select the move with the highest score.

## 📸 Sample Output

```text
You = X
AI = O

  |   |  
--+---+--
  |   |  
--+---+--
  |   |  

Choose position (1-9): 5

O |   |  
--+---+--
  | X |  
--+---+--
  |   |  

Choose position (1-9): 1

O |   |  
--+---+--
  | X |  
--+---+--
X |   |  

AI Wins!
```

## 🎯 Learning Outcomes

* Artificial Intelligence fundamentals
* Minimax search algorithm
* Game theory concepts
* Recursive programming
* Decision-making algorithms
* Python programming

## 🔮 Future Enhancements

* Alpha-Beta Pruning for optimization
* Graphical User Interface (GUI) using Tkinter or Pygame
* Difficulty levels (Easy, Medium, Hard)
* Score tracking
* Multiplayer mode
* Sound effects and animations

## 👨‍💻 Author

**JEJJI MUKUNDA**

B.Tech – Computer Science and Engineering (Artificial Intelligence & Machine Learning)

## 📄 License

This project is developed for educational and learning purposes.

