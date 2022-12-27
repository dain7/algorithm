# Question
# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라 (중복X)

# Solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        # 편의상 정렬 수행
        nums.sort()
        
        # i를 기준으로 투 포인터 기법 수행
        # left, right 값이 빠져 -2를 계산
        for i in range(len(nums)-2):
            
            # 중복 제거
            # i가 이전 i와 같다면 패스한다.
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # i 이후로 투 포인터 설정
            left, right = i+1, len(nums)-1
            
            while left < right:
                
                # i, left, right를 모두 계산한다.
                all_sum = nums[i] + nums[left] + nums[right]
                
                # 합이 0보다 크다면 right (큰 쪽)을 하나 줄임
                if all_sum > 0:
                    right -= 1
                # 합이 0보다 작다면 left (작은 쪽)을 하나 키움
                elif all_sum < 0:
                    left += 1
                else:
                	# 합이 0이라면 result에 추가 
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # left, right 중복 제거
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                    
        return result