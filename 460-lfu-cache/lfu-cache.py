class LFUCache:

    def __init__(self, capacity: int):
        self.lookup = {}
        self.freqList = {}
        self.size = 0
        self.capacity = capacity
        self.leastFreq = 1

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        
        node, curFreq = self.lookup[key]
        updatedFreq = curFreq + 1

        if updatedFreq not in self.freqList:
            self.freqList[updatedFreq] = DoublyLinkedList()

        self.freqList[curFreq].remove(node)
        self.freqList[updatedFreq].insertAtFirst(node)
        self.lookup[key] = (node, updatedFreq)

        if (self.freqList[curFreq].isEmpty()):
            del self.freqList[curFreq]
            self.leastFreq = min(self.freqList.keys())

        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node, freq = self.lookup[key]
            updatedFreq = freq + 1
            node.value = value
            self.lookup[key] = (node, updatedFreq)
            
            if updatedFreq not in self.freqList:
                self.freqList[updatedFreq] = DoublyLinkedList()
            
            self.freqList[freq].remove(node)
            self.freqList[updatedFreq].insertAtFirst(node)
            
            if (self.freqList[freq].isEmpty()):
                del self.freqList[freq]
                self.leastFreq = min(self.freqList.keys())
            return

        if self.capacity == self.size:
            removedNode = self.freqList[self.leastFreq].removeFromLast()
            del self.lookup[removedNode.key]

            if (self.freqList[self.leastFreq].isEmpty()):
                del self.freqList[self.leastFreq]
            self.size -= 1
        
        node = Node(key, value)
        freq = self.leastFreq = 1
        self.lookup[key] = (node, freq)

        if freq not in self.freqList:
            self.freqList[freq] = DoublyLinkedList()
        self.freqList[freq].insertAtFirst(node)
        self.size += 1






class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertAtFirst(self, node):
        if self.head is None:
            self.head = self.tail = node
            return
        
        node.next = self.head
        self.head.prev = node
        self.head = node
    
    def removeFromLast(self):
        if self.head is None:
            return
        
        if self.head == self.tail:
            node = self.head
            self.head = self.tail = None
            return node

        node = self.tail
        self.tail = self.tail.prev
        node.next = node.prev = None
        self.tail.next = None
        return node

    
    def remove(self, node):
        if self.head == self.tail == node:
            self.head = self.tail = None
            return
        
        if self.head == node:
            self.head = self.head.next
            self.head.prev = None
            node.next = None
            node.prev = None
            return
        
        if self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
            node.next = node.prev = None
            return
        
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        node.next = node.prev = None

    def isEmpty(self):
        return self.head == None

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        