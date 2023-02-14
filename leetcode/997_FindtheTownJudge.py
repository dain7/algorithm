# 나의 풀이

import collections

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # n이 1일 경우는 1
        if n == 1 :
            return 1
        
        trust_map = collections.defaultdict(set)
        judge = [] # 누군가를 신뢰하는 사람 저장소
        for t in trust:
            trust_map[t[1]].add(t[0])    
            judge.append(t[0])

        j = 0
        for k, i in trust_map.items():
            # 본인을 믿는 사람이 본인 제외 모두 && 누군가를 신뢰한 적이 없을 경우 -> judge
            if len(i) == n-1 and k not in judge:
                j = k
        
        return -1 if j==0 else j


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        l=[[0,0] for x in range(n+1)]
        # 0은 누군가를 신뢰하는 경우 
        # 1은 나를 신뢰하는 사람의
        for i in trust:
            l[i[1]][1]+=1
            l[i[0]][0]+=1
        for i in range(1,len(l)):
            if l[i][0]==0 and l[i][1]==n-1:
                return i    
        return -1     