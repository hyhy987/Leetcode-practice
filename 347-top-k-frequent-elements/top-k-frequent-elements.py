class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap = dict()
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        hashlist = list(hashmap.items())
        hashlist = sorted(hashlist, key=lambda x: x[1], reverse=True)

        res = []
        if hashlist == None:
            return []

        for i in range(k):
            res.append(hashlist[i][0])
        return res