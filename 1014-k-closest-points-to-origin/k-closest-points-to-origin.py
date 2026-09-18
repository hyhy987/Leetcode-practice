import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [] 
        res = []
        
        def euclidean(points):
            return math.sqrt((points[0]-0)**2 + (points[1]-0)**2)

        for i in range(k):
            distance = euclidean(points[i])
            distances.append([distance, i])

        heapq.heapify_max(distances)

        for i in range(len(points[k:])):
            distance = euclidean(points[k+i])
            if distances[0][0] > distance: 
                heapq.heappush_max(distances, [distance, k+i])
                heapq.heappop_max(distances)


        for elem in distances:
            res.append(points[elem[1]])

        return res

