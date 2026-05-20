 Simple Python Chatbot – README

 📌 Project Title

**Simple Rule-Based Chatbot in Python**

---

 🤖 Description

This is a basic rule-based chatbot created using Python.
The chatbot responds to simple user inputs like greetings and exits when the user types `"bye"`.

It works using:

* Functions
* Loops
* Conditional statements
* User input handling

---

 🚀 Features

* Greets the user
* Responds to basic messages
* Runs continuously until user exits
* Simple and beginner-friendly code

---

 🛠️ Technologies Used

* Python

---

 📂 How the Program Works

 Step 1: Define the Chatbot Function

A function named `chatbot()` is created to run the chatbot.

```python id="1xwz9q"
def chatbot():
```

---

 Step 2: Display Welcome Message

The bot tells the user how to exit.

```python id="mb4kq1"
print("🤖 Chatbot: Type 'bye' to exit")
```

---

 Step 3: Infinite Loop

The chatbot keeps running using a `while True` loop.

```python id="8f8h7g"
while True:
```

---

 Step 4: Take User Input

The program accepts input from the user and converts it to lowercase.

```python id="7n3y2r"
user = input("You: ").lower()
```

---

 Step 5: Check User Message

The chatbot checks the input using `if-elif-else` conditions.

Example:

* `"hello"` → Bot replies with greeting
* `"how are you"` → Bot replies politely
* `"bye"` → Chatbot exits

---

 Step 6: Exit the Program

When the user types `"bye"`, the loop stops using `break`.

```python id="j2x5kd"
break
```

---

▶️ How to Run the Program

1. Install Python on your computer
2. Save the file as `chatbot.py`
3. Open terminal or command prompt
4. Run the command:

```bash id="a9u3df"
python chatbot.py
```

---

 💡 Example Output

```text id="f3m9ke"
🤖 Chatbot: Type 'bye' to exit

You: hello
Bot: Hi!

You: how are you
Bot: I'm fine, thanks!

You: bye
Bot: Goodbye!
```

---

📚 Concepts Used

* Functions
* Loops
* Conditional Statements
* User Input
* String Methods

---

🔮 Future Improvements

* Add more chatbot responses
* Use AI-based responses
* Add GUI using Tkinter
* Add voice input and output
* Store chat history

---

Alisha Saiyed

Made using Python for practice and learning beginner chatbot concepts.
