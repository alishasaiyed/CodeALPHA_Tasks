import random

# Step 1: Predefined word list
words = ["apple", "tiger", "chair", "robot", "plant"]

# Step 2: Choose a random word
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Step 3: Create display (_ _ _)
display = ["_"] * len(word)

print("🎮 Welcome to Hangman Game!")

# Step 4: Game loop
while wrong_guesses < max_wrong and "_" in display:
    print("\nWord:", " ".join(display))
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Step 5: Check input
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Step 6: Check if guess is correct
    if guess in word:
        print("✅ Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("❌ Wrong guess!")
        wrong_guesses += 1

# Step 7: Result
if "_" not in display:
    print("\n🎉 You WON! The word was:", word)
else:
    print("\n💀 You LOST! The word was:", word)