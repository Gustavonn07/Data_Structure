import heapq

class GrafoDirecional:
    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_aresta(self, origem, destino, peso=1):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        if not any(dest == destino for dest, _ in self.grafo[origem]):
            self.grafo[origem].append((destino, peso))

    def remover_aresta(self, origem, destino):
        if origem in self.grafo:
            self.grafo[origem] = [
                (d, p) for d, p in self.grafo[origem] if d != destino
            ]

    def remover_vertice(self, v):
        if v in self.grafo:
            del self.grafo[v]
        for vizinhos in self.grafo.values():
            vizinhos[:] = [(dest, peso) for dest, peso in vizinhos if dest != v]

    def tem_conexao(self, origem, destino):
        return any(dest == destino for dest, _ in self.grafo.get(origem, []))

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
        for vizinho, _ in self.grafo[inicio]:
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
                fila.extend(v for v, _ in self.grafo[atual] if v not in visitados)

    def obter_vertices(self):
        return list(self.grafo.keys())

    def obter_arestas(self):
        arestas = []
        for origem, destinos in self.grafo.items():
            for destino, peso in destinos:
                arestas.append((origem, destino, peso))
        return arestas

    def dijkstra(self, inicio):
        distancias = {v: float('inf') for v in self.grafo}
        distancias[inicio] = 0
        heap = [(0, inicio)]
        predecessores = {v: None for v in self.grafo}

        while heap:
            dist_atual, atual = heapq.heappop(heap)
            if dist_atual > distancias[atual]:
                continue
            for vizinho, peso in self.grafo[atual]:
                nova_dist = dist_atual + peso
                if nova_dist < distancias[vizinho]:
                    distancias[vizinho] = nova_dist
                    predecessores[vizinho] = atual
                    heapq.heappush(heap, (nova_dist, vizinho))

        return distancias, predecessores

    def caminho_minimo(self, inicio, fim):
        distancias, predecessores = self.dijkstra(inicio)
        if distancias[fim] == float('inf'):
            return None
        caminho = []
        atual = fim
        while atual is not None:
            caminho.insert(0, atual)
            atual = predecessores[atual]
        return caminho, distancias[fim]
