class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # key : 방 넘버 value : 해당 방에 있는 키 
        key_map = collections.defaultdict(list)

        # key_map을 구성한다.
        for i, room in enumerate(rooms):
            for r in room:
                key_map[i].append(r)

        # 앞으로 방문해야할 방의 넘버가 담긴 stack
        stack = [0]
        # 방문한 적이 있는 방 넘버가 담긴 stack
        visited = []

        while stack:
            # 방문할 방 선택
            room = stack.pop(0)

            # 이미 방문한 적이 있으면 pass
            if room in visited:
                continue
            # 방문한적이 없으면 visited에 넣어줌
            else :
                visited.append(room)

            # 해당 방에서 얻을 수 있는 키를 꺼내와 앞으로 방문할 방에 넣어줌
            for r in key_map[room]:
                stack.append(r)   
        # 방문한 방과 현재 존재하는 방의 갯수가 같으면 모두 방문한 것임
        return set(key_map.keys()) == set(visited)
