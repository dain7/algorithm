class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        strnum = ''.join([str(i) for i in num])
        answer = str(int(strnum)+k)
        
        return [int(i) for i in answer]