# 나의 풀이
from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        match_map = defaultdict(int)
        number_list = []
        
        for m in matches : 
            match_map[m[1]] += 1

            number_list.append(m[0])
            number_list.append(m[1])
        
        no_lost = sorted([n for n in set(number_list) if n not in match_map.keys()])
        one_lost = sorted([m for m in match_map.keys() if match_map[m] == 1])

        return no_lost, one_lost
        

# 베스트 풀이
class Solution: 
    def findWinners(self, matches : List[List[int]]) ->List[List[int]]: 
        seen = set() losses_count = {}
        
        for winner, loser in matches:
            seen.add(winner)
            seen.add(loser)
            # get -> 있으면 가져오고 아니면 0으로 넣어라.
            losses_count[loser] = losses_count.get(loser, 0) + 1
        
        #Add players with 0 or 1 loss to the corresponding list.
        zero_lose, one_lose = [], []
        for player in seen:
            count = losses_count.get(player, 0)
            if count == 0:
                zero_lose.append(player)
            elif count == 1:
                one_lose.append(player)
        
        return [sorted(zero_lose), sorted(one_lose)]