"""
Convert a number to binary using stack

input: 985
output: 1111011001

"""

from stack import Stack


def to_binary(input_num):
    s=Stack()
    binary_op = ''
    while input_num>0:
        s.push(input_num%2)
        input_num = input_num // 2

    while not s.is_empty():
        binary_op += str(s.pop())
    return binary_op


print(to_binary(985))
print(int('1111011001',2))
