class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        r = sum(nums)

        min_index = 99999
        min_value = 99999

        if n == 1:
            return 0
            
        for i, v in enumerate(nums):
            l += v
            r -= v
            n -= 1  
              
            a = math.floor(l // (i+1))
            b = 0
            
            if n != 0 :
                b = math.floor(r / n)

            if abs(a-b) < min_value:
                min_value = abs(a-b)
                min_index = i+1
        
        return min_index-1
            


# 다른 사람 풀이
class Solution:
    def minimumAverageDifference(self, a: List[int]) -> int:
        l=0
        r=sum(a)
        z=100001 # 최소 평균치 담는 변수
        y=0 # 최소 평균치인 인덱스
        n=len(a)
        
        for i in range(n-1):
            l+=a[i]
            r-=a[i]
        
            d=abs((l//(i+1))-(r//(n-i-1)))
            if d<z:
                z=d
                y=i
        
    
        if sum(a)//n<z:
            y=n-1
        
        return y
            

