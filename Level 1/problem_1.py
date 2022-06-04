#Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included). 
# The numbers obtained should be printed in a comma-separated sequence on a single line.


def solve(a, b):
    numbers_list = []
    for number in range(a, b + 1):
        if number % 7 == 0 and number % 5 != 0:
            numbers_list.append(number)
    print([x for x in numbers_list], sep = ', ')


solve(2000, 3200)