class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        
        a_counter = {}
        b_counter = {}

        for v in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            a_counter[v] = a.count(v)
            b_counter[v] = b.count(v)
 
        return sum([a for a in a_counter.values()]) == sum([a for a in b_counter.values()])