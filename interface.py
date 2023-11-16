import prim


def imprimeMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print()


def criaMatriz(colunas):
    matriz = []
    for i in range(colunas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append(0)
    return matriz


def matrizAdj(colunas):
    matriz = criaMatriz(colunas)

    print("\nInforme o peso da aresta entre os vértices em questão(0 se não houver aresta):\n")

    for i in range(colunas):
        for j in range(i, colunas):
            # if i == j:
            #     matriz[i][j] = 0
            # else:
            while True:
                try:
                    matriz[i][j] = int(input("{} e {} : ".format(i, j)))
                    matriz[j][i] = matriz[i][j]
                    break
                except ValueError:
                    print("Valor inválido")
                    
    return matriz


def criaMatrizArvore(numVertices, G):
    adjMatrix = criaMatriz(numVertices)

    if numVertices > 1:
        for e in range(len(G)):
            i = G[e][0].pop()
            j = G[e][0].pop()
            adjMatrix[i][j] = G[e][1]
            adjMatrix[j][i] = G[e][1]

    return adjMatrix


def prompt_user():
    while True:
        numVertices = int(input("O grafo possui quantos vértices?\n R: "))

        while numVertices == 0:
            print("\nO grafo em questão é nulo. Insira um valor maior que zero.")
            numVertices = int(input("O grafo possui quantos vértices?\n R: "))

        adj_matriz = matrizAdj(numVertices)

        #chama algoritmos
        try:
            mst, inicioVertices = prim.prim(numVertices, adj_matriz)
            custo = prim.peso(mst)

            print("\nVértice Inicial:", inicioVertices)
            print("\nMatriz de Adjacência do Grafo:")
            imprimeMatriz(adj_matriz)
            print("\nMatriz de Adjacência da Árvore Geradora Mínima:")
            imprimeMatriz(criaMatrizArvore(numVertices, mst))
            print("\nO Custo da Árvore Geradora Mínima é:", custo)
            break
        
        except Exception as exc:
            print("\n{}\n".format(exc))

