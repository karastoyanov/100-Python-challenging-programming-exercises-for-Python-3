# Question: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether 
# they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence. 
# Example: 0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input by console.

def solve(numbers):
    res_list = []
    for _ in numbers:
        current_number = int(_, 2)
        if current_number % 5 == 0:
            res_list.append(_)
    print(*res_list, sep = ',')


input_numbers = [x for x in input().split(',')]
solve(input_numbers)

