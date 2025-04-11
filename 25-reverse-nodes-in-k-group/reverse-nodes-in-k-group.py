
class Solution:
    # def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
    #     cur = head
    #     newHead = None
    #     previousBlockTail = ListNode()

    #     while True:
    #         kthNode = self.getKthNode(cur, k)

    #         if kthNode is None:
    #             if newHead is None:
    #                 return cur
    #             else:
    #                 previousBlockTail.next = cur
    #                 break

    #         nextBlockStartNode = kthNode.next
    #         reversedListHead = self.reverse(cur, kthNode)

    #         previousBlockTail.next = reversedListHead
    #         previousBlockTail = cur
    #         cur.next = None

    #         if newHead is None:
    #             newHead = reversedListHead


    #         cur = nextBlockStartNode

    #     return newHead

    # def getKthNode(self, head, k):
    #     while k > 1 and head:
    #         head = head.next
    #         k -= 1
    #     return head
    
    # def reverse(self, head, tail):
        # tail.next = None
        # prev = None
        # cur = head

        # while cur:
        #     nxt = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = nxt
        # return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        newHead = None
        cur = head
        prevBlockLastNode = None

        while True:
            kthNode = self.getKthNode(cur, k)
            
            if kthNode is None:
                break

            nextBlockFirstNode = kthNode.next

            curBlockFirstNode, curBlockLastNode = self.reverse(cur, kthNode)

            if newHead == None:
                newHead = curBlockFirstNode

            if prevBlockLastNode is not None:
                prevBlockLastNode.next = curBlockFirstNode
            prevBlockLastNode = curBlockLastNode
            curBlockLastNode.next = nextBlockFirstNode

            cur = nextBlockFirstNode

        return newHead

    def getKthNode(self, head, k):
        while head and k > 1:
            head = head.next
            k -= 1
        return head

    def reverse(self, head, tail):
        prev = None
        cur = head

        while prev != tail:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev, head