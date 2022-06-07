# Question: Write a program that accepts a sentence and calculate the number of upper case
# letters and lower case letters. Suppose the following input is supplied to the program: 
# Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

def solve(sentence):
    lowercases = []
    uppercases = []
    for _ in range(len(sentence)):
        if sentence[_].islower():
            lowercases.append(sentence[_])
        elif sentence[_].isupper():
            uppercases.append(sentence[_])
    print(f'UPPER CASE {len(uppercases)} LOWER CASE {len(lowercases)}')


user_input = input()
solve(user_input)