class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Subtract(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Multiply(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()

class Divide(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()

class Num():
    def __init__(self, val):
        self.val = val

    def eval(self):
        return int(self.val)

class Print():
    def __init__(self, val):
        self.val = val

    def eval(self):
        print(self.val.eval())