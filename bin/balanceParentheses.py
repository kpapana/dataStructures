"""
Program to check if parentheses are Balanced

"""

from stack import Stack


def is_balanced(input_string=''):
    s = Stack()
    open_parentheses = ['[', '(', '{']
    close_parentheses = [']', ')', '}']
    for item in input_string:
        if item in open_parentheses:
            s.push(item)
        elif item in close_parentheses and not s.is_empty():
            if s.pop() != open_parentheses[close_parentheses.index(item)]:
                return False
        else:
            return False
    if s.is_empty():
        return True
    else:
        return False


print(is_balanced('{[{}]}'))
