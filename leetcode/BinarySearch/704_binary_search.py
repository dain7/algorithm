# 이진 검색 문제
# 이진 검색 : 정렬되어 있는 리스트에서, 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법이다.
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0 # 왼쪽 인덱스
        right = len(nums)-1 # 오른쪽 인덱스
        mid = int(len(nums)/2) # 중간 인덱스

        # 왼쪽 인덱스가 오른쪽보다 커지면 멈춤.
        while left <= right :
            # 중간값이 target보다 작으면 왼쪽을 키워줌 
            if nums[mid] < target:
                left = mid+1
                mid = int((left+right)/2)
            # 중간값이 target보다 크면 오른쪽을 내려줌
            elif nums[mid] > target:
                right = mid-1
                mid = int((left+right)/2)
            # 아니면 멈춤
            else :
                break
        
        if nums[mid] != target:
            return -1
        return mid


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left=0
        right=len(nums)-1
        
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                return mid
                
        return -1