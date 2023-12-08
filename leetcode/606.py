class Solution:
    def tree2str(self, root):
        def pre(node):
            # node가 비어있으면 그대로 리턴
            if not node:
                return

            # 현재 노드를 넣는다.
            self.ans += str(node.val)

            # 자식 노드가 있으면 계속 추가
            if node.left or node.right:
                self.ans += "("
                pre(node.left)  # Recursive call to process the left subtree
                self.ans += ")"

            # If the current node has a right child, include parentheses
            if node.right:
                self.ans += "("
                pre(node.right)  # Recursive call to process the right subtree
                self.ans += ")"

        # 시작점
        self.ans = ""
        pre(root)  # 함수 호출
        return self.ans  # Return the final string representation of the tree