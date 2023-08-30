from string import ascii_lowercase

def solution(s, skip, index):
    result = ''
    # 소문자 a부터 z까지 
    a_to_z = set(ascii_lowercase)
    # skip 해야하는 문자 제거 
    a_to_z -= set(skip)
    # 정렬
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    # 알파벳 : 인덱스 
    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}
    
    # 하나씩 뽑아서 
    for i in s:
        #현재 알파벳 인덱스에 인덱스 더 해준 후 % 길이의 나머지 = z 초과되도 계산 가능!!!!
        result += a_to_z[(dic_alpha[i] + index) % l]

    return result