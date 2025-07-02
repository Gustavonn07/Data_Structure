
class Node:
    def __init__(self, data, parent=None, left_children=None, right_children=None):
        self._data = data
        self._parent = parent
        self._left = left_children
        self._right = right_children

    def set_left_child(self, child):
        self._left = child
        if child:
            child.set_parent(self)

    def get_left_child(self):
        return self._left

    def set_right_child(self, child):
        self._right = child
        if child:
            child.set_parent(self)

    def get_right_child(self):
        return self._right

    def set_parent(self, parent):
        self._parent = parent

    def get_parent(self):
        return self._parent

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data


def build_subtree(operator, left, right):
    node = Node(operator)
    node.set_left_child(left)
    node.set_right_child(right)
    return node

class BinaryTree:
    precedence = {
        '**': 3,
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1
    }

    def __init__(self, expression: str):
        if not expression:
            raise ValueError('Expressão deve ser informada')
        self._tokens = expression.split()
        self.root = None

    def generate_tree(self):
        values = []
        operators = []

        def apply_operator():
            # Pega o operador do topo e aplica aos dois últimos valores
            op = operators.pop()
            right = values.pop()
            left = values.pop()
            node = build_subtree(op, left, right)
            values.append(node)

        for token in self._tokens:
            if token.isnumeric():  # se for número (pode adaptar para floats)
                values.append(Node(token))
            elif token in self.precedence:
                # enquanto tem operador no topo com precedência maior ou igual, aplica ele
                while operators and self.precedence.get(operators[-1], 0) >= self.precedence[token]:
                    apply_operator()
                operators.append(token)
            else:
                raise ValueError(f"Token desconhecido: {token}")

        # Aplica os operadores restantes
        while operators:
            apply_operator()

        # No final, só resta a raiz
        if len(values) != 1:
            raise ValueError("Erro ao gerar árvore: expressão inválida")

        self.root = values[0]
        return self.root

    def print_inorder(self, node=None):
        if node is None:
            node = self.root
        if node.get_left_child() is None and node.get_right_child() is None:
            return node.get_data()
        left_expr = self.print_inorder(node.get_left_child())
        right_expr = self.print_inorder(node.get_right_child())
        return f'({left_expr} {node.get_data()} {right_expr})'

# Exemplo de uso
if __name__ == "__main__":
    expr = "2 + 4 * 2 - 3"
    tree = BinaryTree(expr)
    tree.generate_tree()
    print(tree.print_inorder())  # Saída: (2 + (4 * 2)) - 3

