# %%
import random

# %%
# Creates a word list
word_list = ["apple", "mango", "orange", "banana", "grape"]

# %%
# prints each word and its length side by side
for word in word_list:
    print(f"{word}:{len(word)}")  # Prints each

# %%
word = random.choice(word_list)  # Randomly selects a word from the list
print(f"Random Word is {word}")
# %%
