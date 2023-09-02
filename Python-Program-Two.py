# Name: Vanessa Barajas
# Course: CIT-95
# Date: 09-01-2023
# Project Name: Python Program Two

# Assigned sample text string
text = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."

# Length Calculation
def calculate_length(text):
     return len(text)
print("The length is: ", calculate_length(text))

# Uppercase and Lowercase Conversion
def convert_case(text):
     return text.upper() + text. lower()
print("Uppercase and Lowercase: ", convert_case(text))

# Word Count
def count_words(text):
     words = text.split()
     return len(words)
print("Word Count: ", count_words(text))

# Substring Extraction
def extract_substring(text, start, end):
     return text[start:end]
print("Substring Extraction: ", extract_substring(text, 7,20))

#Word Replacement
def replace_word(text, target, replacement):
     return text.replace(target, replacement)
target_word = input("Enter target word: ")
replacement_word = input("Enter replacement word: ")
print("Word Replacement: ", replace_word(text, target_word, replacement_word))

# Whitespace Removal
def remove_whitespace(text):
     return text.strip()
print("Whitespace Removal:", remove_whitespace(text))

# Splitting into Sentences
def split_sentences(text):
     sentences = text.split('. ')
     return sentences
print("Splitting into Sentences: ", split_sentences(text))

# Word Reversal
def reverse_words(text):
     words = text.split()
     reversed_words = [word[::-1] for word in words]
     return ' '.join(reversed_words)
print("Word Reversal:", reverse_words(text))

# Character Count
def count_characters(text, char):
     return text.count(char)
target_char = input("Enter character to count: ")
print("Character Count:", count_characters(text, target_char))

# Substring Count
def count_substring(text, substring):
     return text.count(substring)
target_substring = input("Enter substring to count: ")
print("Substring Count:", count_substring(text, target_substring))

#List Creation
word_list = text.split()

# Appending
word_list.append("Pythonic")

# Insertion
word_list.insert(0, "awesome")

# Indexing and Slicing
print("Third word:", word_list[2])
print("Sublist from 6th to 9th:", word_list[5:9])

# Removal
word_list.remove("amazing")

# Sorting
word_list.sort()
print("Modified Word List: ", word_list)

# Counting
count_of_is = word_list.count("is")
print("Count of 'is': ", count_of_is)

#Joining
sentence = ' '.join(word_list)
print("Joined Sentence: ", sentence)

# Reversal
word_list.reverse()
print("Reversed Word List: ", word_list)

# Copying
copied_list = word_list.copy()
print("Copied List: ", copied_list)