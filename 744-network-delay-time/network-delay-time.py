class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = self.buildGraph(n + 1, times)
        timeTaken = [float(inf)] * (n + 1)
        visited = {i: False for i in range(n + 1)}

        minHeap = [(0, k)]
        timeTaken[k] = 0

        while len(minHeap) > 0:
            delay, curVertex = heapq.heappop(minHeap)
            # if visited[curVertex] == True:
            #     continue
            
            visited[curVertex] = True

            for child, childDelay in graph[curVertex]:
                if visited[child] == True:
                    continue
                curDelay = timeTaken[curVertex] + childDelay
                if curDelay < timeTaken[child]:
                    timeTaken[child] = curDelay
                    heapq.heappush(minHeap, [curDelay, child])

        return max(timeTaken[1:]) if float('inf') not in timeTaken[1:] else -1


    def buildGraph(self, n, edges):
        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append([edge[1], edge[2]])
        return graph

 