# 나의 풀이
def frequencySort(self, s: str) -> str:
    dic = {}

    for alpha in s:
        dic[alpha] = dic.get(alpha, 0) + 1
    
    dic = sorted(dic.items(), key = lambda x : x[1], reverse=True)

    answer = ""
    for i in dic:
        answer += i[0] * i[1]
    
    return answer


# 다른 사람 풀이
def frequencySort(self, s: str) -> str:
	# Count the occurence on each character
	cnt = collections.Counter(s)
	
	# Build string
	res = []
    # counter의 most common 이용
	for k, v in cnt.most_common():
		res += [k] * v
	return "".join(res)

# 다른 사람 풀이 2
def frequencySort(self, s: str) -> str:
	# Count the occurence on each character
	cnt = collections.Counter(s)
	
	# Build heap
	heap = [(-v, k) for k, v in cnt.items()]
	heapq.heapify(heap)
	
	# Build string
	res = []
	while heap:
		v, k = heapq.heappop(heap)
		res += [k] * -v
	return ''.join(res)