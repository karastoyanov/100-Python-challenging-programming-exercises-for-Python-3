# Question: Define a class which has at least two methods: 
# getString: to get a string from console input
# printString: to print the string in upper case. 
# Also please include simple test function to test the class methods.

class Task():
    def __init__(self):
        self.string = ""
        
    def getString(self):
        self.string = input()
    
    def printString(self):
        print(self.string.upper())

test = Task()
test.getString()
test.printString()