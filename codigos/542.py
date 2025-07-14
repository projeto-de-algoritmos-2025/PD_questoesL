from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        linhas, colunas = len(mat), len(mat[0])
        dist = [[float('inf')] * colunas for _ in range(linhas)]

        for i in range(linhas):
            for j in range(colunas):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if i > 0:
                        dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                    if j > 0:
                        dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)

        for i in range(linhas - 1, -1, -1):
            for j in range(colunas - 1, -1, -1):
                if i < linhas - 1:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j < colunas - 1:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)

        return dist