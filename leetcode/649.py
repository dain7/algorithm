class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # deque : 앞뒤로 원소를 넣고 빼낼 수 있음 
        rQ = deque()
        dQ = deque()
        
        # index를 deque에 넣음 
        for i, c in enumerate(senate):
            if c == "R":
                rQ.append(i)
            else:
                dQ.append(i)
        
        # d와 r의 인덱스를 비교 -> 더 작은 놈이 승! 
        # 다음 라운드 진출 -> 더 작은 놈 + len(senate) 더해줌 (그 후로 다시 비교 비교 비교)
        while dQ and rQ:
            d,r = dQ.popleft(), rQ.popleft()
            
            if d < r:
                dQ.append(d+len(senate))
            else:
                rQ.append(r+len(senate))
                
        return "Radiant" if rQ else "Dire"