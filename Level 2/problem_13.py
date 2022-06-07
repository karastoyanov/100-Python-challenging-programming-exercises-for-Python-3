# Question: Write a program that accepts a sentence and calculate the number of letters and digits. 
# Suppose the following input is supplied to the program: hello world! 123 
# Then, the output should be: LETTERS 10 DIGITS 3

def solve(sentence):
    letters = []
    digits = []
    for _ in range(len(sentence)):
        current_char = sentence[_]
        if current_char.isalpha():
            letters.append(current_char)
        elif current_char.isdigit():
            digits.append(current_char)
    print(f"LETTERS {len(letters)} DIGITS {len(digits)}")

user_input = input()
solve(user_input)