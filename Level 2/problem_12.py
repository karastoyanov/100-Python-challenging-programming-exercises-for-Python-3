# Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) 
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.


def solve(a, b):
    res_list = []
    for i in range(a, b + 1):
        current_number = str(i)
        for j in range(len(current_number)):
            is_even = False
            if int(current_number[j]) % 2 == 0:
                is_even = True
                continue
            else:
                is_even = False
                break
        if is_even:
            res_list.append(current_number)
    print(*res_list, sep = ',')

solve(1000, 3000)
            


