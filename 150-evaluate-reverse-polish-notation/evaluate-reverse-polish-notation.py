import operator

class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/':lambda a, b: int(float(a)/b)}
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                num1 = stack.pop()
                num2 = stack.pop()

                op = operators[tokens[i]]
                res = op(num2, num1)
                stack.append(res)

        return stack[0]
                
        