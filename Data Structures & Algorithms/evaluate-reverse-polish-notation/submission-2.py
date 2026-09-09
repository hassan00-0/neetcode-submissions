class Solution:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b):
        return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+" : self.add, "-": self.subtract, "*": self.multiply, "/": self.divide}
        for i in tokens:
            if i in operations:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(operations[i](num1, num2))
            else:
                stack.append(int(i))
        return stack[0]