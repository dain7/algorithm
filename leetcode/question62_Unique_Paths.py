# Question
# [m, n]까지 도달하는 경우의 수를 모두 구하라.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp
        # 1을 가진 m*n의 행렬 생성 (본인 경로니까 1로 시작)
        aux = [[1 for x in range(n)] for x in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                # i, j까지 도달하는 경우의 수는 i, j-1의 경우의 수 + i-1 + j 경우의 수
                aux[i][j] = aux[i][j-1]+aux[i-1][j]
        return aux[-1][-1]
