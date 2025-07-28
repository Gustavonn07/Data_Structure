class GrafoNaoDirecional:
    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_aresta(self, v1, v2):
        self.adicionar_vertice(v1)
        self.adicionar_vertice(v2)
        if v2 not in self.grafo[v1]:
            self.grafo[v1].append(v2)
        if v1 not in self.grafo[v2]:
            self.grafo[v2].append(v1)

    def remover_aresta(self, v1, v2):
        if v1 in self.grafo and v2 in self.grafo[v1]:
            self.grafo[v1].remove(v2)
        if v2 in self.grafo and v1 in self.grafo[v2]:
            self.grafo[v2].remove(v1)

    def remover_vertice(self, v):
        if v in self.grafo:
            for vizinho in self.grafo[v]:
                self.grafo[vizinho].remove(v)
            del self.grafo[v]

    def tem_conexao(self, v1, v2):
        return v1 in self.grafo and v2 in self.grafo[v1]

    def mostrar_grafo(self):
        for v, vizinhos in self.grafo.items():
            print(f"{v} -> {vizinhos}")

    def busca_em_profundidade(self, inicio, visitados=None):
        if visitados is None:
            visitados = set()
        if inicio not in self.grafo:
            return
        print(inicio)
        visitados.add(inicio)
        for vizinho in self.grafo[inicio]:
            if vizinho not in visitados:
                self.busca_em_profundidade(vizinho, visitados)

    def busca_em_largura(self, inicio):
        from collections import deque
        if inicio not in self.grafo:
            return
        visitados = set()
        fila = deque([inicio])
        while fila:
            atual = fila.popleft()
            if atual not in visitados:
                print(atual)
                visitados.add(atual)
                fila.extend(v for v in self.grafo[atual] if v not in visitados)

    def obter_vertices(self):
        return list(self.grafo.keys())

    def obter_arestas(self):
        arestas = set()
        for v, vizinhos in self.grafo.items():
            for u in vizinhos:
                if (u, v) not in arestas:
                    arestas.add((v, u))
        return list(arestas)
