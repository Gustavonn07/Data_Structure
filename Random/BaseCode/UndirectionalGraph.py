import heapq

class GrafoNaoDirecional:
    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_aresta(self, v1, v2, peso=1):
        self.adicionar_vertice(v1)
        self.adicionar_vertice(v2)
        if not any(v == v2 for v, _ in self.grafo[v1]):
            self.grafo[v1].append((v2, peso))
        if not any(v == v1 for v, _ in self.grafo[v2]):
            self.grafo[v2].append((v1, peso))

    def mostrar_grafo(self):
        for v, vizinhos in self.grafo.items():
            print(f"{v} -> {vizinhos}")

    def dijkstra(self, inicio):
        distancias = {v: float('inf') for v in self.grafo}
        distancias[inicio] = 0
        heap = [(0, inicio)]  # (distância acumulada, vértice)
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
            return None  # Sem caminho
        caminho = []
        atual = fim
        while atual is not None:
            caminho.insert(0, atual)
            atual = predecessores[atual]
        return caminho, distancias[fim]
