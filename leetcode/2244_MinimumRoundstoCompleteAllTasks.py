# ㄴㅏ의 풀이 (실패.. ㅎ )
# 10에서 4가 되어야 하는데 5로 나옴 => 3,3,2,2 가 아니라 2,2,2,2,2 
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        tasks.sort()
        answer = 0

        while tasks : 
            count = 0

            num = tasks.pop(0)
            count += 1

            while tasks:
                if tasks[0] != num:
                    break
                tasks.pop(0)
                count += 1

            if count == 1 :
                answer = -1
                return answer
            
            if (count % 3 == 0):
                answer += count // 3
            elif  ((count % 3) % 2 == 0):
                answer += (count//3) + (count%3)//2
            else :
                answer += count // 2
     
        return answer

# 숫자 최소 패턴이 3, 2, 3 + 2 혹은 3 + 2 + 2 그래서 2와 4를 빼준 후  계산
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        frequency = Counter(tasks)
        res = 0
        for freq in frequency.values():
            if freq == 1:
                return -1
            elif (freq-2) % 3 == 0:
                res += (freq-2) // 3 + 1
            elif (freq - 4) % 3 == 0:
                res += (freq - 4) // 3 +2
            elif freq % 3 == 0:
                res += freq // 3
            else:
                res += freq // 2
        return res