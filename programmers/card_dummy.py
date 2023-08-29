def solution(cards1, cards2, goal):
    one_list = [0]
    two_list = [0]
    
    for g in goal:
        if g in cards1:
            i = cards1.index(g)
            if abs(one_list[-1]-i) > 1:
                return "No"
            else :
                one_list.append(i)
        if g in cards2:
            i = cards2.index(g)
            if abs(two_list[-1]-i) > 1:
                return "No"
            else :
                two_list.append(i)
    return "Yes"


# 다른 사람 풀이 
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]: # 0인것부터 뽑으면 순서 보장 가능..!!!
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"