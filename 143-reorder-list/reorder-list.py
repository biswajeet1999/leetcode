# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reorderList(self, head: Optional[ListNode]) -> None:
        # slow = head
        # fast = head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # if fast and fast.next == None:
        #     slow = slow.next
        
        # first = head
        # second = slow

        # # reverse
        # prev = None
        # cur = second
        # while cur:
        #     nxt = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = nxt
        # second = prev

        # # shuffle
        # newHead = ListNode()
        # while second:
        #     newHead.next = first
        #     first = first.next
        #     newHead = newHead.next

        #     newHead.next = second
        #     second = second.next
        #     newHead = newHead.next

        #     newHead.next = None

        # if first:
        #     newHead.next = first
        #     first.next = None
            

    def reorderList(self, head: Optional[ListNode]) -> None:
        firstHalf, secondHalf = self.splitList(head)
        secondHalf = self.reverseList(secondHalf)

        newList = ListNode()
        while firstHalf and secondHalf:
            newList.next = firstHalf
            firstHalf = firstHalf.next
            newList = newList.next

            newList.next = secondHalf
            secondHalf = secondHalf.next
            newList = newList.next
        
        if firstHalf:
            newList.next = firstHalf
        
        
    def splitList(self, head):
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next  

        firstHalf = head
        secondHalf = None       

        if fast == None:
            prev.next = None
            secondHalf = slow
        else:
            secondHalf = slow.next
            slow.next = None
        
        return firstHalf, secondHalf

    def reverseList(self, head):
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev





        