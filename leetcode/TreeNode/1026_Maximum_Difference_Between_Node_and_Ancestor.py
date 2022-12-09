class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, mn, mx):
            if not root: return 0
            # |현재의 값-최소값|과 |현재의 값-최대값| 중 더 큰 값을 res에 저장한다. 
            # 최종적으로 가장 큰 res가 정답.
            res = max(abs(root.val - mn), abs(root.val - mx))
			
			# 최소값과 현재의 값 중 더 작은값이 최솟값에 저장, 최대값과 현재의 값 중 더 큰 값 최대값을 저장
            # 노드 중 가장 큰 수와 가장 작은 수를 계속 넘겨줌 
            mn, mx = min(mn, root.val), max(mx, root.val)

			# res와 왼쪽에서 가장 큰값, 오른쪽에서 가장 큰값 중 제일 큰 값을 찾아 리턴한다.
            return max(res, dfs(root.left, mn, mx), dfs(root.right, mn, mx))
       
        return dfs(root, root.val, root.val)