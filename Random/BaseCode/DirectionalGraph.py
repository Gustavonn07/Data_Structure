class GrafoDirecional:
    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_aresta(self, origem, destino):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        if destino not in self.grafo[origem]:
            self.grafo[origem].append(destino)

    def remover_aresta(self, origem, destino):
        if origem in self.grafo and destino in self.grafo[origem]:
            self.grafo[origem].remove(destino)

    def remover_vertice(self, v):
        if v in self.grafo:
            del self.grafo[v]
        for vizinhos in self.grafo.values():
            if v in vizinhos:
                vizinhos.remove(v)

    def tem_conexao(self, origem, destino):
        return origem in self.grafo and destino in self.grafo[origem]

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
        arestas = []
        for origem, destinos in self.grafo.items():
            for destino in destinos:
                arestas.append((origem, destino))
        return arestas
