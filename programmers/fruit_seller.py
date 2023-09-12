def solution(k, m, score):
    score = sorted(score, reverse=True)
    answer = 0

    for i in range(0, len(score), m):
        if i+m <= len(score):
            a = min(score[i:i+m])
            answer += a * m
    
    return answer




def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m