class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = self.buildGraph(n, flights)
        return self.shortestPath(graph, src, dst, k + 1, n)

    def buildGraph(self, n, edges):
        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append([edge[1], edge[2]])
        return graph
    
    def shortestPath(self, graph, src, dst, k, n):
        cost = [float('inf') for i in range(n)]
        minHeap = [[0, src, 0]]
        cost[src] = 0

        while len(minHeap) > 0:
            curK, curCity, curCost = heapq.heappop(minHeap)

            if curK > k:
                continue

            for child in graph[curCity]:
                costToChild = curCost + child[1]
                childK = curK + 1
                if costToChild < cost[child[0]] and childK <= k:
                    cost[child[0]] = costToChild
                    heapq.heappush(minHeap, [childK, child[0], costToChild])
        
        return cost[dst] if cost[dst] != float('inf') else -1