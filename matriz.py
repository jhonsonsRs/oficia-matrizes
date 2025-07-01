def atribuirValoresParaMatriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range (linhas):
        for j in range (colunas):
            matriz[i][j] = int(input(f"Digite o valor da posição [{i + 1}] [{j + 1}]: "))
    return matriz

def somarMatrizes(matrizA, matrizB):
    linhasA = len(matrizA)
    colunasA = len(matrizA[0])
    matrizC = [[0] * colunasA for _ in range(linhasA)]
    for i in range (linhasA):
        for j in range (colunasA):
            matrizC[i][j] = matrizA[i][j] + matrizB[i][j]
    return matrizC

def subtrairMatrizes(matrizA, matrizB):
    linhasA = len(matrizA)
    colunasA = len(matrizA[0])
    matrizC = [[0] * colunasA for _ in range(linhasA)]
    for i in range (linhasA):
        for j in range (colunasA):
            matrizC[i][j] = matrizA[i][j] - matrizB[i][j]
    return matrizC


linhasA = int (input("informe a quantidade de linhas da matriz A: "))
colunasA = int (input("informe a quantidade de colunas da matriz A: "))

linhasB = int (input("informe a quantidade de linhas da matriz B: "))
colunasB = int (input("informe a quantidade de colunas da matriz B: "))

if linhasA != linhasB or colunasA != colunasB:
    print('Erro: as matrizes precisam ter o mesmo tamanho para este exemplo')
else:
    matrizA = [[0] * colunasA for _ in range(linhasA)]
    matrizB = [[0] * colunasB for _ in range(linhasB)]
    
    matrizA = atribuirValoresParaMatriz(matrizA)
    print(matrizA)

    matrizB = atribuirValoresParaMatriz(matrizB)
    print(matrizB)

    print(somarMatrizes(matrizA, matrizB))
    print(subtrairMatrizes(matrizA, matrizB))