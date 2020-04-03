str1 = '[](){([[[]]])}('
str2 = '[{{{(())}}}]((()))'
str3 = '[[[]])]'

class Stack(object):
    def __init__(self):
        super().__init__()
        self.arr = []

    def pop(self):
        if len(self.arr):
            return self.arr.pop()
        else:
            print('Stack is empty')
    
    def push(self, x):
        self.arr.append(x)
    
    def peek(self):
        return self.arr[-1]

def is_balanced(string):
    if len(string) == 0 or len(string) % 2:
        return False

    stack = Stack()
    opening_braces = ['(', '[', '{']
    closing_braces = [')', ']', '}']
    d = dict(zip(opening_braces, closing_braces))

    for brace in string:
        if brace in opening_braces:
            stack.push(brace)
        else:
            if brace != d[stack.peek()]:
                return False
            stack.pop()
    return True

print(is_balanced(str3))