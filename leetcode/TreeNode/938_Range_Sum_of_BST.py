# 트리노드 내에서 low 와 high사이에 존재하는 값을 더해 리턴해라.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0

        # stack에 넣어 하나씩 처리한다. 
        stack = [root]
        while stack:
            tree = stack.pop()

            # 현재 값이 low보다 크고 high보다 작으면 res에 더해라
            if tree.val >= low and tree.val <= high:
                res += tree.val
            
            # left가 존재하면 stack에 넣어라 
            if tree.left:
                stack.append(tree.left)
            
            # right가 존재하면 stack 넣어라
            if tree.right:
                stack.append(tree.right)

        return res


# 다른 사람 풀이
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root == None: return 0
        # val이 high보다 크면 val보다 작은 왼쪽만 탐색하면 됨.
        if root.val > high: return self.rangeSumBST(root.left,low,high)
        # val이 low보다 작으면 오른쪽만 탐색하면 됨.
        if root.val < low: return self.rangeSumBST(root.right,low,high)
        # 재귀를 통해 더해준다. 
        return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)      
                   