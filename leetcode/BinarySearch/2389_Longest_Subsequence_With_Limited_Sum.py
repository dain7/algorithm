# 나의 풀이
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        answer = [] # 답안 저장할 리스트
        nums.sort() # '최대 서브 시퀀스의 길이'를 찾아야 하기 때문에 작은 것부터 정렬 

        while queries:
            q = queries.pop(0) # 하나씩 뽑음
            result = 0 

            # q-n이 0보다 작지 않으면 +1
            for n in nums:
                if q - n >= 0:
                    result += 1
                    q -= n
            answer.append(result)

        return answer


# 다른 사람 풀이
# 이진 검색 풀이
def answerQueries(self, A: List[int], queries: List[int]) -> List[int]:
        A = list(accumulate(sorted(A)))
        return [bisect_right(A, q) for q in queries]