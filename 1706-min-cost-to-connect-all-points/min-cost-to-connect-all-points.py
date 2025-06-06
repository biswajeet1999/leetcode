class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 0:
            return 0
        visited = {tuple(point): False for point in points}

        cost = {tuple(point): float('inf') for point in points}
        cost[tuple(points[0])] = 0
        minHeap = [(0, tuple(points[0]))]

        while len(minHeap) > 0:
            curPoint = tuple(heapq.heappop(minHeap)[1])
            if visited[curPoint] == True:
                continue
            visited[curPoint] = True

            for point in points:
                if visited[tuple(point)] == True:
                    continue
                dist = abs(point[0] - curPoint[0]) + abs(point[1] - curPoint[1])
                if dist < cost[tuple(point)]:
                    cost[tuple(point)] = dist
                    heapq.heappush(minHeap, (dist, point))
        return sum(cost.values())