class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        charFreq = {}
        for task in tasks:
            charFreq[task] = charFreq.get(task, 0) + 1
        
        taskMinHeap = [[-charFreq[task], 1, task] for task in charFreq]
        heapq.heapify(taskMinHeap)
        taskQueue = []
        time = 0

        while len(taskMinHeap) > 0 or len(taskQueue) > 0:
            time += 1

            if len(taskQueue) > 0 and taskQueue[0][1] <= time:
                heapq.heappush(taskMinHeap, taskQueue.pop(0))

            if len(taskMinHeap) > 0 and taskMinHeap[0][1] <= time:
                task = heapq.heappop(taskMinHeap)
                task[0] += 1
                task[1] = time + n + 1
                if task[0] != 0:
                    taskQueue.append(task)

        return time
            

            


