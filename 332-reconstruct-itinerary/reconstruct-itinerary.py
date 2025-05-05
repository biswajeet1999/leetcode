class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = {}

        for t in tickets:
            if t[0] not in graph:
                graph[t[0]] = []
            graph[t[0]].append(t[1])

        result = []
        self.dfs(graph, 'JFK', result)
        return result[::-1]

    def dfs(self, graph, src, result):
        while len(graph.get(src, [])) > 0:
            self.dfs(graph, graph[src].pop(0), result)
        result.append(src)