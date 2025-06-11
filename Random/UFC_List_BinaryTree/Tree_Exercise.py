
class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.children = []

    def add_children(self, node):
        node.parent = self
        self.children.append(node)

class Tree:
    def __init__(self, root):
        self.root = Node(root)

    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        print('  ' * level + f'- {node.data}')
        for child in node.children:
            self.display(child, level + 1)

    def find(self, data, node=None):
        if node is None:
            node = self.root
        if node.data == data:
            return node
        for child in node.children:
            found = self.find(data, child)
            if found:
                return found
        return None

    def insert(self, parent_data, new_node):
        parent_node = self.find(parent_data)
        if parent_node:
            parent_node.add_children(new_node)
        else:
            print(f"Nó com valor '{parent_data}' não encontrado.")

    def depth_search(self, value, node=None):
        if node is None:
            node = self.root

        if node.data == value:
            if node.parent:
                print(f"Pai de '{node.data}': {node.parent.data}")
            else:
                print(f"'{node.data}' é a raiz e não tem pai.")
            return node

        for child in node.children:
            result = self.depth_search(value, child)
            if result:
                return result

        return None



tree = Tree("Raiz")

tree.insert("Raiz", Node("Filho 1"))
tree.insert("Raiz", Node("Filho 2"))
tree.insert("Filho 1", Node("Neto 1"))
tree.insert("Filho 1", Node("Neto 2"))
tree.insert("Neto 1", Node("Bisneto 1"))
tree.insert("Bisneto 1", Node("Tetraneto 1"))
tree.insert("Bisneto 1", Node("Tetraneto 2"))
tree.insert("Neto 1", Node("Bisneto 2"))

tree.depth_search("Tetraneto 2")
tree.depth_search("Raiz")
tree.depth_search("Filho 1")

tree.display()

