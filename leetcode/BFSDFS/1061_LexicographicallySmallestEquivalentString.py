# 내가 시도했던 ㅜㅜ 풀이
import collections
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        # 모든 단어의 묶음을 만들어주고 싶었음....  ㅜㅜ => 여기에 실패해서 못품!
        m = collections.defaultdict(list)
        for i, j in zip(s1, s2) :
            m[i].append(j)
            m[j].append(i)

        visited = []
        for k, v in m.items():
            if k in visited :
                continue
            visited.append(k)
            for value in v :
                print(value)
                if value in visited :
                    continue
                visited.append(value)
                value_list = m[value]
                m[k].extend(value_list)
        print(m)            
        
        # 키 값을 이용해서 비교한 후 더 작은 숫자를 답에 +
        answer = ''
        for word in baseStr:
            word_list = sorted(m[word])
            if len(word_list) > 0 : 
                if word < word_list[0]:
                    answer += word
                else :
                    answer += word_list[0]
            else :
                answer += word
        
        print(answer)


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(c):
            i = ord(c) - ord('a')
            while root[i] != i:
                i = root[i]
                
            return i
        
        root = list(range(26))
        for c1, c2 in zip(s1, s2):
            r1 = find(c1)
            r2 = find(c2)
            if r1 > r2:
                r1, r2 = r2, r1

            root[r2] = r1
        
        return "".join(chr(ord('a') + find(c)) for c in baseStr)