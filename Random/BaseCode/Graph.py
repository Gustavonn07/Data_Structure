class Grafo:
    def __init__(self, direcionado=False):
        self.grafo = {}
        self.direcionado = direcionado

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_aresta(self, origem, destino):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.grafo[origem].append(destino)
        if not self.direcionado:
            self.grafo[destino].append(origem)

    def mostrar_grafo(self):
        for vertice in self.grafo:
            print(f'{vertice} -> {self.grafo[vertice]}')

    def bfs(self, inicio):
        visitados = set()
        fila = [inicio]

        print("BFS:", end=" ")

        while fila:
            atual = fila.pop(0)
            if atual not in visitados:
                print(atual, end=" ")
                visitados.add(atual)
                fila.extend([vizinho for vizinho in self.grafo[atual] if vizinho not in visitados])
        print()

    def dfs(self, inicio, visitados=None):
        if visitados is None:
            visitados = set()
            print("DFS:", end=" ")

        print(inicio, end=" ")
        visitados.add(inicio)

        for vizinho in self.grafo[inicio]:
            if vizinho not in visitados:
                self.dfs(vizinho, visitados)

# --------------------------
# Exemplo de uso:
g = Grafo(direcionado=False)

g.adicionar_aresta("A", "B")
g.adicionar_aresta("A", "C")
g.adicionar_aresta("B", "D")
g.adicionar_aresta("C", "E")
g.adicionar_aresta("D", "E")
g.adicionar_aresta("E", "F")

g.mostrar_grafo()
g.bfs("A")
g.dfs("A")
