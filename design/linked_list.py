from typing import List



# @ada indicate the other node, which is the next node of curret node.
# this size of this structure will be decided by counting the nodes that this structure has

class Node:
    
    def __init__(self, val: int, next = None) -> None:
        self.value = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if not self.head:
            return -1
        
        node = self.head
        count = 0
        while node:
            if count == index:
                return node.value
            
            node = self.head.next
            count += 1
        
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = None(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node        

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        
        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return True
        
        count = 0
        node = self.head
        prev = None
        while node and count < index:
            prev = node
            node = node.next
            count += 1
            
        if not node:
            return False
        
        prev.next = node.next
        if not prev.next:
            self.tail = prev            
            
        return True                

    def getValues(self) -> List[int]:
        node = self.head
        array = []
        while node:
            array.append(node.value)
            node = node.next
        
        return array