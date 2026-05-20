 Stock Portfolio Tracker – README

📌 Project Title

**Stock Portfolio Tracker in Python**

---

 📈 Description

This is a simple Python-based Stock Portfolio Tracker that allows users to:

* Enter stock names and quantities
* Calculate total investment value
* Store the result in a text file

The program uses a predefined dictionary of stock prices and calculates the investment amount based on user input.

---

 🚀 Features

* Predefined stock prices
* User input for stock selection
* Quantity-based investment calculation
* Total investment tracking
* Saves output to a text file
* Beginner-friendly project

---

🛠️ Technologies Used

* Python

---

📂 How the Program Works

 Step 1: Create Stock Price Dictionary

A dictionary stores stock names and their prices.

```python id="g7d2ka"
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}
```

---

 Step 2: Initialize Total Investment

A variable is created to store the total investment amount.

```python id="k9f4sd"
total_investment = 0
```

---

 Step 3: Take User Input

The program asks the user to enter:

* Stock name
* Quantity

```python id="q3m8pl"
stock = input("Enter stock name: ").upper()
```

---

Step 4: Validate Stock Name

The program checks whether the stock exists in the dictionary.

```python id="w2n6tx"
if stock not in stock_prices:
```

---

 Step 5: Calculate Investment

Investment is calculated using:

\text{Investment} = \text{Stock Price} \times \text{Quantity}

Example:
If `TSLA = 250` and quantity is `2`

250 \times 2 = 500

---

 Step 6: Add to Total Investment

The investment amount is added to the total.

```python id="m8v1ca"
total_investment += investment
```

---

 Step 7: Save Result to File

The total investment value is saved in `portfolio.txt`.

```python id="d6x4re"
with open("portfolio.txt", "w") as file:
```

---

 ▶️ How to Run the Program

1. Install Python on your system
2. Save the file as `portfolio_tracker.py`
3. Open terminal or command prompt
4. Run the command:

```bash id="t4z8yb"
python portfolio_tracker.py
```

---

 💡 Example Output

```text id="p7n5qs"
📈 Stock Portfolio Tracker

Enter stock name (or type 'done' to finish): TSLA
Enter quantity: 2
✅ TSLA added worth $500

Enter stock name (or type 'done' to finish): AAPL
Enter quantity: 1
✅ AAPL added worth $180

💰 Total Investment Value = 680
📁 Result saved in portfolio.txt
```

---

 📚 Concepts Used

* Dictionary
* Loops
* Conditional Statements
* File Handling
* User Input
* Arithmetic Operations

---

 🔮 Future Improvements

* Add real-time stock prices using APIs
* Save complete portfolio details
* Add profit/loss calculation
* Create graphical charts
* Build GUI version using Tkinter

---

Alisha Saiyed

Made using Python for learning basic portfolio tracking and file handling concepts.
