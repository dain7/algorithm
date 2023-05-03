class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        a1 = [i for i in set(nums1) if i not in nums2]
        a2 = [i for i in set(nums2) if i not in nums1]
        
        return [a1, a2]


def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    ans = [[], []]
    st1 = set(nums1)
    st2 = set(nums2)
    ans[0] = list(st1 - st2)
    ans[1] = list(st2 - st1)
    return ans