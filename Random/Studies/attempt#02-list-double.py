class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head

        if self.head:
            self.head.previous = new_node

        self.head = new_node

    def remove(self, value):
        current = self.head

        while current:
            if current.value == value:
                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.previous = current.previous

                return  # remove o primeiro que encontrar
            current = current.next

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current.value
            current = current.next
        return None

    def exibe(self):
        if not self.head:
            print("Lista vazia")
            return

        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

dll = DoublyLinkedList()
dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.exibe()        # 30 <-> 20 <-> 10 <-> None
dll.remove(20)
dll.exibe()        # 30 <-> 10 <-> None
print(dll.search(10))  # 10
print(dll.search(20))  # None
