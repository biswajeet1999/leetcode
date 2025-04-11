"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None
        
        head1 = head
        head2 = Node(0)
        tail2 = head2

        while head1:
            tail2.next = Node(head1.val)
            tail2 = tail2.next
            head1 = head1.next
        
        head2 = head2.next
        
        temp1 = head
        temp2 = head2

        while temp1:
            next1 = temp1.next
            next2 = temp2.next

            temp1.next = temp2
            temp2.next = next1

            temp1 = next1
            temp2 = next2
        
        temp1 = head
        temp2 = head.next

        while temp2:
            temp1Random = temp1.random
            randomClon = temp1Random.next if temp1Random else None

            temp2.random = randomClon

            temp1 = temp2.next
            temp2 = temp1.next if temp1 else None

        temp1 = head
        temp2 = head2

        while temp1:
            temp1.next = temp2.next
            temp1 = temp1.next
            temp2.next = temp1.next if temp1 else None
            temp2 = temp2.next

        return head2


    def copyRandomList(self, head):
        if head is None:
            return None
        
        head2 = Node(0)
        cur2 = head2
        cur1 = head

        while cur1:
            cur2.next = Node(cur1.val)
            cur2 = cur2.next
            cur1 = cur1.next
        
        head2 = head2.next
        cur1 = head
        cur2 = head2

        while cur1:
            copyNode = cur2
            cur2 = cur2.next

            copyNode.next = cur1.next
            cur1.next = copyNode
            cur1 = cur1.next.next

        cur1 = head
        cur2 = head.next

        while cur1:
            node = cur1
            copyNode = cur1.next

            randomNode = node.random
            randomCopyNode = randomNode.next if randomNode else None
            copyNode.random = randomCopyNode
            
            cur1 = cur1.next.next

        cur1 = head
        cur2 = head2
        while cur1:
            cur1.next = cur2.next
            cur1 = cur1.next

            cur2.next = cur1.next if cur1 else None
            cur2 = cur2.next
        return head2
        





  