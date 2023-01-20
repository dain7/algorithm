# 내가 시도한 풀이
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = []

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    break
                answer.append([i for i in nums[i:j+1]])
        print(answer)



## Backtracking 기법
class Solution:
    def solve(self, nums, index, output, ans):
        # 만약 input 배열의 끝에 도달했다면
        if index >= len(nums):
            # only add the output if it has more than one element
            if len(output) > 1:
                ans.add(tuple(output))
            return
        
        # output이 비어있거나 or 지금 요소가 output 맨 끝보다 크다면
        if not output or nums[index] >= output[-1]:
            # ouput에 현재 요소를 추가하고 and solve를 재귀적으로 콜한다. 
            output.append(nums[index])
            self.solve(nums, index+1, output, ans)
            # return전에 output의 맨 마지막 요소를 제거한다. 
            output.pop()
        
        # output에 추가하는 것 없이 call한다 
        self.solve(nums, index+1, output, ans)

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # use a set to store the unique sub sequences
        ans = set()
        self.solve(nums, 0, [], ans)
        return [list(x) for x in ans]