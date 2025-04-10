# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) time | O(1) space
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head == None or head.next == None:
#             return head
        
#         prev = None
#         cur = head

#         while cur != None:
#             nextP = cur.next
#             cur.next = prev
#             prev = cur
#             cur = nextP
#         return prev

# O(n) time | O(n) space
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         _, newHead = self.reverseListUtil(head)
#         return newHead

#     def reverseListUtil(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None or head.next is None:
#             return head, head
        
#         nextNode, newHead = self.reverseListUtil(head.next)
#         head.next = None
#         nextNode.next = head
#         return head, newHead

# O(n) time | O(1) space
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        curNode = head

        while curNode:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
        return prevNode