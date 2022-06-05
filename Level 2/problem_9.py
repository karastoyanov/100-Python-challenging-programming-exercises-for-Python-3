# Question£º Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence
# capitalized. Suppose the following input is supplied to the program:
# Hello world Practice makes perfect Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT


def solve(lines):
    result = "".join(lines)
    print(result.upper())
    

user_input = [x for x in input().split("\n")]
solve(user_input)