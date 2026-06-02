"""
TASK: 01 File Stats Tool

# Read a .txt file and compute:
Task:
- Number of lines
- Number of words
- Number of characters
- Most frequent word

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

file = open("sample.txt", "r")

text = file.read()
file.close()

lines = text.split("\n")
num_lines = len(words)

words = text.split()
num_words = len(words)

num_characters = len(text)

word_count ={}

if word in word_count:
    
