class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)

        return res 


        