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