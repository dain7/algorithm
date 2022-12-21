class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # list를 value로 가지는 dict 생성
        self.graph = collections.defaultdict(list) 

        group_mapping = {}

        # graph를 꾸며준다.
        for (u, v) in dislikes:
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        # 방문을 세는 visited
        visited = set()
        for i in range(1, N + 1): 
            # 재방문은 세지 않음
            if i in visited: continue
            
            # i와 group인지 true/false
            stack = [(i, 0)] 
            while stack:  
                tmp_stack = []
                while stack:                               
                    cur_node, group = stack.pop() # 1, 0 => 2, 1 => 3, 1 ... 
                    if cur_node in group_mapping and group != group_mapping[cur_node]: 
                        return False

                    if cur_node in visited: continue # 방문했던 애다

                    group_mapping[cur_node] = group # group_mapping[1] = 0 => group_mapping[2] =  1... 
                    visited.add(cur_node) 
                    for child in self.graph[cur_node]: # child : 2,3
                        tmp_stack.append((child, not group)) # not group으로 계속 반대로 넣어줌. (부모와)
                stack = tmp_stack            
        return True  