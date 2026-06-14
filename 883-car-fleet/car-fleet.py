class Solution(object):
    def carFleet(self, target, position, speed):
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs = sorted(pairs)[::-1]
        stack = []

        for p, s in pairs:
            stack.append(float(target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

        