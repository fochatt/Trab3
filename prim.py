from random import randint


def peso(G):
    peso = 0
    for i in G:
        peso += i[1]
    return peso


def prim(V, adjMatrix):
    if V == 1:
        return [[{0, 0}, 0]], 0

    verticeInicio = vertice = randint(0, V-1)
    MST = []
    aresta = []
    visitado = set()
    arestaMin = [set(), float('inf')]

    while(len(MST) < V-1):
        visitado.add(vertice)

        for r in range(V):
            if adjMatrix[vertice][r] != 0:
                aresta.append([{vertice, r}, adjMatrix[vertice][r]])

        for e in range(len(aresta)):
            if aresta[e][1] < arestaMin[1] and not aresta[e][0].issubset(visitado):
                arestaMin = aresta[e]

        # verifica se o grafo é desconexo
        if arestaMin == [set(), float('inf')]:
            raise Exception("O Grafo é Desconexo")

        aresta.pop(aresta.index(arestaMin))
        MST.append(arestaMin)
        aux_set = arestaMin[0].copy()
        aux_set.remove(aux_set.intersection(visitado).pop())

        #vertice from arestaMin that is not in visitado
        vertice = aux_set.pop()
        arestaMin = [set(), float('inf')]

    return MST, verticeInicio