# 두 트리노드의 끝값과 순서가 모두 같은지 확인 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        # 둘 중 하나라도  None이면 false
        if root1 is None or root2 is None:
            return False

        res1 = []
        res2 = []

        stack = [root1]
        # stack을 이용하여 오른쪽이 존재하면 스택에 넣어주고 => 왼쪽이 존재하면 넣어줌
        # 이 경우 무조건 오른쪽 => 왼쪽으로 탐색해서 순서 보장
        # 왼쪽, 오른쪽 모두 값이 없다 == 끝값이므로 res1에 넣어준다 
        while stack :
            t = stack.pop()

            if not t.left and not t.right:
                res1.append(t.val)
                continue

            if t.right:
                stack.append(t.right)

            if t.left:
                stack.append(t.left)      
  

        # 위와 동일한 알고리즘
        stack = [root2]
        while stack :
            t = stack.pop()

            if not t.left and not t.right:
                res2.append(t.val)
                continue

            if t.right:
                stack.append(t.right)

            if t.left:
                stack.append(t.left) 
        
        return res1 == res2

# 둘 다 모두 끝까지 훑기때문에 불필요한 탐색이 들어감...
# 중간에 다르면 false 리턴하는 방법...

# 동일한 알고리즘을 재귀로 합침

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        if root1 is None or root2 is None:
            return False

        def recurTree(root: Optional[TreeNode]) :
            stack = [root]
            res = []
            while stack :
                t = stack.pop()

                if not t.left and not t.right:
                    res.append(t.val)
                    continue

                if t.right:
                    stack.append(t.right)

                if t.left:
                    stack.append(t.left)      

            return res
        
        return recurTree(root1) == recurTree(root2)


# 다른 사람 풀이
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def leafs(root):
            # root가 존재하지 않으면 return
            if not root: return

            stack = [root]; leaf = []

            while stack:
                node = stack.pop()
                
                if not node:
                    continue

                stack.append(node.right)
                stack.append(node.left)

                if not (node.left or node.right):
                    leaf.append(node.val)
            return leaf
        
        return leafs(root1) == leafs(root2)

