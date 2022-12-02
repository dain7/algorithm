class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        word1_dict = {}
        word2_dict = {}
        
        for w1 in word1:
            word1_dict[w1] = word1_dict.get(w1, 0) + 1
        
        for w2 in word2:
            word2_dict[w2] = word2_dict.get(w2, 0) + 1
        

        # 어떤 글자인지와 상관없이 글자의 Count값만 각각이 같으면 됨! 
        # 글자의 구성 또한 같아야 됨!
        return sorted(word1_dict.values()) == sorted(word2_dict.values()) and set(word1) == set(word2)
