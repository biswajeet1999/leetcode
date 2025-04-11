# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        mergedList = ListNode()
        lastNode = mergedList
        minHeap = []

        print(lists)

        for lst in lists:
            if lst is not None:
                heapq.heappush(minHeap, NodeWrapper(lst))
        
        while len(minHeap) > 0:
            minNode = heapq.heappop(minHeap)
            lastNode.next = minNode.node
            lastNode = lastNode.next

            if minNode.node.next:
                heapq.heappush(minHeap, NodeWrapper(minNode.node.next))

        return mergedList.next
        
        