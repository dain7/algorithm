# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        answer = []
        stack = [root]
        while stack :
            s = stack.pop()
 
            if s is not None:
                answer.append(s.val)
            else : 
                break 
            
            # pop은 리스트 끝 기준이므로 나중에 탐색하는 right부터 넣어줌
            if s.right is not None:
                stack.append(s.right) 
            if s.left is not None:
                stack.append(s.left)

        return answer