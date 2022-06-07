# Question: Write a program that computes the net amount of a bank account based a transaction log from console input. 
# The transaction log format is shown as following: D 100 W 200
# D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 
# Then, the output should be: 500

from calendar import c
from collections import deque

def solve(sequence):
    acc_log = deque()
    values = deque()
    final_sum = 0
    
    for _ in sequence:
        if _.isdigit():
            values.append(_)
        elif _.isalpha():
            acc_log.append(_)
    
    for l in range(len(acc_log)):
        for v in range(len(values)):
            current_log = acc_log.popleft()
            if current_log == "D":
                final_sum += int(values.popleft())
            else:
                final_sum -= int(values.popleft())
    print(final_sum)

user_input = [x for x in input().split()]
solve(user_input)
