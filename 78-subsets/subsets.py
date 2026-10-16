class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []

        def recursion(i, curr):
            nonlocal subset

            if i == len(nums):
                subset.append(curr.copy())
                return 

            else:
                recursion(i+1, curr)
                curr.append(nums[i])
                recursion(i+1, curr)
                curr.pop()
                

        recursion(0, [])

        return subset
            