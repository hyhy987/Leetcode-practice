class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while nums[l] > nums[r]:
            mid = l + (r - l) // 2

            # Check if mid pointer is in left or right partition
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid

        return nums[l]