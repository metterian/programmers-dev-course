#%%
class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1, ')': 1,
}
#%%
def solution(S):
    opStack = ArrayStack()
    answer = []
        # Iterate over the expression for conversion
    for char in S:
        if char.isalpha():
            answer.append(char)

        elif char == '(':
            opStack.push(char)
        elif char == ')':
            if not opStack.isEmpty():
                while opStack.peek() != '(':
                    answer.append(opStack.pop())
                opStack.pop()
        else:
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[char]:
                answer.append(opStack.pop())
            opStack.push(char)

    while not opStack.isEmpty():
        answer.append(opStack.pop())
    return "".join(answer)
# solution('A+B*C')
solution('A+B*C-D/E')

# %%
