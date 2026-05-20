 Hangman Game – README

 📌 Project Title

**Python Hangman Game**

🎮 Description

This is a simple command-line Hangman game made using Python.
The program randomly selects a word from a predefined list, and the player has to guess the word one letter at a time before running out of chances.

---

 🚀 Features

* Random word selection using `random.choice()`
* Tracks guessed letters
* Shows correct and wrong guesses
* Limits wrong attempts to 6
* Displays win or lose message

---

🛠️ Technologies Used

* Python
* Random Module

---

 📂 How the Program Works

 Step 1: Import Random Module

The `random` module is used to select a random word from the list.

```python
import random
```

---

 Step 2: Create Word List

A list of predefined words is stored.

```python
words = ["apple", "tiger", "chair", "robot", "plant"]
```

---

 Step 3: Random Word Selection

The program selects one random word.

```python
word = random.choice(words)
```

---

 Step 4: Game Loop

The game continues until:

* The player guesses the word, or
* The player reaches the maximum wrong guesses.

---

 Step 5: Input Checking

The program checks:

* If the letter was already guessed
* If the guessed letter exists in the word

---

 Step 6: Display Result

* 🎉 Win message if the player guesses the word
* 💀 Lose message if attempts finish

---

 ▶️ How to Run the Program

1. Install Python on your system
2. Save the file as `hangman.py`
3. Open terminal or command prompt
4. Run the command:

```bash
python hangman.py
```

---

 💡 Example Output

```text
🎮 Welcome to Hangman Game!

Word: _ _ _ _ _
Wrong guesses left: 6

Enter a letter: a
✅ Correct guess!
```

---

 📚 Concepts Used

* Lists
* Loops
* Conditional Statements
* String Handling
* User Input
* Random Module

---

 🔮 Future Improvements

* Add difficulty levels
* Add categories for words
* Show hangman ASCII art
* Add multiplayer mode
* Store scores in a file

---
Alisha Saiyed 

Made with Python for learning and practice.