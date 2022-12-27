# 나의 풀이
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        # 현재 가지고 있는 돌을 제외한 나머지를 저장해줄 리스트 
        new_capacity = []
        for c, r in zip(capacity, rocks):
            left = c - r
            new_capacity.append(left)
        
        full = 0
        new_capacity.sort() # 최대 가방의 개수를 찾아야해서 작은것부터 정렬 필요 
   
        for c in new_capacity :
            if c != 0:
                # 수용량이 추가돌보다 크다 (ex. 10, 3)
                if c > additionalRocks :
                    c -= additionalRocks # 10 - 3 = 7
                    additionalRocks = 0 # 다 썼다.
                # 수용량이 추가돌보다 작다 (ex. 3, 10)
                elif c < additionalRocks :
                    additionalRocks -= c # 10 - 3 = 7
                    c = 0 # 더 못 들어 ㅜㅜ
                else : # 같으면 0
                    c = 0
                    additionalRocks = 0
            # 수용량이 다 차면 full + 1 
            if (c == 0):
                    full += 1    

        return full

# 다른 사람 풀이
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        arr=[]
        for i in range(len(rocks)):
            arr.append(capacity[i]-rocks[i])
        arr.sort()
        
        c=0
        for i in arr:
            if(i<=additionalRocks):
                c+=1
                additionalRocks-=i 
        return c

