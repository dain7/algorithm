# 내 문제풀이
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        c_list = list(c.values())
        for a in c_list:
            if c_list.count(a) > 1:
                return False
        return True


# 다른 사람 풀이
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        
        # create a hash map
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        # 숫자별로 겹치는 수가 다 달라야하기 때문에 둘의 길이가 같음
        if len(set(dic.values())) != len(set(arr)):
            return False
        return True