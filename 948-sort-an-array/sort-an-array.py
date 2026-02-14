class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge(arr1, arr2):
            new_arr = []
            i = 0
            j = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    new_arr.append(arr1[i])
                    i += 1
                else:
                    new_arr.append(arr2[j])
                    j += 1
            while i < len(arr1):
                new_arr.append(arr1[i])
                i += 1
            while j < len(arr2):
                new_arr.append(arr2[j])
                j += 1
            return new_arr

        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            arr_length = len(arr)
            half_length = arr_length // 2
            arr1 = arr[:half_length]
            arr2 = arr[half_length:]

            new1 = mergeSort(arr1)
            new2 = mergeSort(arr2)

            return merge(new1, new2)
        
        return mergeSort(nums)