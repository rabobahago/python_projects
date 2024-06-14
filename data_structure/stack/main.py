
class Stack:
    def __init__(self):
        self.arrows = []

    def push(self, arrow):
        el = self.arrows.append(arrow)
        return el

    def pop(self):
        if not self.arrows:
            return None
        el = self.arrows.pop()
        return el

    def peek(self):
        if not self.arrows:
            return None
        return self.arrows[-1]

    def size(self):
        return len(self.arrows)

def is_balanced(input_str):
    stack = Stack()
    for char in input_str:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.pop() is None:
                return False
        if char == '{':
            stack.push(char)
        elif char == '}':
            if stack.pop() is None:
                return False
        if char == '[':
            stack.push(char)
        elif char == ']':
            if stack.pop() is None:
                return False
    return stack.peek() is None
print(is_balanced('((()))'))
print(is_balanced('(())()'))
print(is_balanced(''))
