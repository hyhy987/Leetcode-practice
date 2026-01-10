# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        begin = 1
        end = n
        while begin < end:
            mid = begin + (end - begin) / 2
            num = guess(mid)
            if (num == -1 or num == 0):
                end = mid 
            if (num == 1):
                begin = mid + 1
        return begin 
        