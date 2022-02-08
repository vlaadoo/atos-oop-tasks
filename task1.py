class Stack:

    class Node:
        def __init__(self, value, nextNode):
            self.value = value
            self.nextNode = nextNode
    
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top is None
    
    def push(self, value):
        self.top = Stack.Node(value, self.top)
    
    def pop(self):

        if self.isEmpty():
            raise EmptyStackException

        val = self.top.value
        self.top = self.top.nextNode

        return val

if __name__ == "__main__":
    s = Stack()
    s.push('1')
    s.push('22')
    s.push('33')
    s.push('4')
    s.push('56')
    s.push('6')
    s.push('77')

    while not s.isEmpty():
        print(s.pop())