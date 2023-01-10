# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#### 나의 풀이
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # 트리를 순회하여 리스트에 하나씩 담아주는 로직
        def traverseTree(tree : Optional[TreeNode]) -> List :
            nodeList = []
            stack = [tree]

            while stack :
                node = stack.pop()       

                if node:
                    nodeList.append(node.val)
                    stack.append(node.right)
                    stack.append(node.left)
                else :
                    nodeList.append(None)
            return nodeList
        
        # 둘이 같으면 true 아니면 false
        return traverseTree(p) == traverseTree(q)


#### 다른 사람 풀이
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False