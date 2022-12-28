# 나의 풀이
from heapq import *

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []

        # heap에 -를 붙여 넣어줌 (역순으로 하려고)
        for p in piles:
            heappush(heap, -p)

        # 하나씩 뽑아 (가장 큰 수) 계산해준 다음에 다시 넣음 * k번
        for _ in range(k):
            h = -heappop(heap)
            heappush(heap, -(h-floor(h/2)))
        
        return -sum(heap)

# 다른 사람 풀이
def minStoneSum(self, A, k):
        A = [-a for a in A]
        heapq.heapify(A)
        
        for i in xrange(k):
            heapq.heapreplace(A, A[0] / 2)
        return -sum(A)