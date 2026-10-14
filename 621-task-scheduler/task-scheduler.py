import heapq 
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = {}
        for elem in tasks:
            count[elem] = 1 + count.get(elem, 0)

        queue = deque()
        time = 0 
        heap = []
        
        for key, value in count.items():
            heapq.heappush_max(heap, value)

        while heap or queue:
            time += 1
            
            if queue and queue[0][1] == time:
                new = queue.popleft()
                heapq.heappush_max(heap, new[0])
                
            if heap:
                val = heapq.heappop_max(heap)
                val -= 1

                if val == 0:
                    continue
                else:
                    queue.append((val, time + n + 1))

        return time 






