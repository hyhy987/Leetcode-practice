class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid 
                else:
                    left = mid + 1

            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid 
                else:
                    right = mid - 1
            
        if nums[left] == target:
            return left
        else:
            return -1 