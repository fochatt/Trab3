import prim_alg


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = " ")
        print()


def create_sqr_matrix(num_rows):
    matrix = []
    for i in range(num_rows):
        matrix.append([])
        for j in range(num_rows):
            matrix[i].append(0)
    return matrix


def enter_adj_matrix(num_rows):
    matrix = create_sqr_matrix(num_rows)

    print("\nInforme o peso da aresta entre os vértices (0 se não houver aresta):\n")

    for i in range(num_rows):
        for j in range(i, num_rows):
            # if i == j:
            #     matrix[i][j] = 0
            # else:
            while True:
                try:
                    matrix[i][j] = int(input("{} e {} : ".format(i, j)))
                    matrix[j][i] = matrix[i][j]
                    break
                except ValueError:
                    print("Valor inválido")
                    
    return matrix


def create_adj_matrix(num_vertex, G):
    adjMatrix = create_sqr_matrix(num_vertex)

    if num_vertex > 1:
        for e in range(len(G)):
            i = G[e][0].pop()
            j = G[e][0].pop()
            adjMatrix[i][j] = G[e][1]
            adjMatrix[j][i] = G[e][1]

    return adjMatrix


def prompt_user():
    while True:
        num_vertex = int(input("Quantos vértices?\n R: "))

        while num_vertex == 0:
            print("\nGrafo Nulo. Insira um valor maior que zero.")
            num_vertex = int(input("Quantos vértices?\n R: "))

        adj_matriz = enter_adj_matrix(num_vertex)

        #chama algoritmos
        try:
            mst, vertex_inic = prim_alg.prim(num_vertex, adj_matriz)
            custo = prim_alg.peso_total(mst)

            print("\nVértice Inicial escolhido Randomicamente:", vertex_inic)
            print("\nMatriz de Adjacência do Grafo Informado:")
            print_matrix(adj_matriz)
            print("\nMatriz de Adjacência da Árvore Geradora Mínima:")
            print_matrix(create_adj_matrix(num_vertex, mst))
            print("\nCusto da Árvore Geradora Mínima:", custo)
            break
        
        except Exception as exc:
            print("\n{}\n".format(exc))

