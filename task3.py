class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, item):
        node = Node(item)

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        
    def prepend(self, item):
        node = Node(item)
    
        if self.head is None:
            self.tail = node
        else:
            node.next = self.head
            
        self.head = node
        
    def delete(self, item):
        if self.head is None:
            return

        if self.head.data == item:
            self.head = self.head.next

        current = self.head
        while current.next is not None:
            if current.next.data == item:
                current.next = current.next.next
                return

            current = current.next

        return
    
    def length(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next
    
        return count


if __name__ == "__main__":
    facade = LinkedList()
    facade.append('2')
    facade.append('dsadsa')
    print(facade.length()) # 2
