class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort() # 작은 순으로 정렬 (최대한 많이 사야하기 때문에)
        answer = 0
        for cost in costs:
            # 가지고 있는 코인에서 비용을 하나씩 빼줌 
            if coins - cost >= 0:
                coins -= cost
                answer += 1
            # 코인을 더이상 쓸 수 없으면 멈춤
            else :
                break
        
        return answer