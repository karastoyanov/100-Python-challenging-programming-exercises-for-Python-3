# Question: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program: 9 Then, the output should be: 11106

def solve(number):
    a = number
    result = int("%s" % a) + int("%s%s" % (a, a)) + int("%s%s%s" % (a, a, a)) + int("%s%s%s%s" % (a, a, a, a))
    print(result)
    

user_input = int(input())
solve(user_input)