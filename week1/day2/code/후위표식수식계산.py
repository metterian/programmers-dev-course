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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    for char in tokenList:
        if char not in '*/-+()':
            postfixList.append(char)

        elif char == '(':
            opStack.push(char)
        elif char == ')':
            if not opStack.isEmpty():
                while opStack.peek() != '(':
                    postfixList.append(opStack.pop())
                opStack.pop()
        else:
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[char]:
                postfixList.append(opStack.pop())
            opStack.push(char)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return postfixList


def postfixEval(tokenList):
    valStack = ArrayStack()

    for token in tokenList:
        if token.isalnum():
            valStack.push(token)
        else:
            a = valStack.pop()
            b = valStack.pop()
            valStack.push(eval(token.join([str(b), str(a)])))
    return valStack.pop()
#%%
def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(map(str, tokens))
    val = postfixEval(postfix)
    return val

solution("7 * (9 - (3+2))")

# %%
