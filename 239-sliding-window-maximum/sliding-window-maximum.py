class Solution(object):
    def maxSlidingWindow(self, nums, k):
        l = 0
        q = collections.deque()
        res = []

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if r >= k -1:
                res.append(nums[q[0]])
                l += 1
        
        return res



        