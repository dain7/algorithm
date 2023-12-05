class Solution:
    def numberOfMatches(self, n: int) -> int:
        answer = 0
        while n != 1:
            if n%2 == 0:
                n = n/2
                answer += n
            else:
                n = (n-1)/2
                answer += n+1

        return int(answer)


class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n > 1:
            matches += n // 2
            n = (n + 1) // 2
        return matches