class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left=0
        min_len=min(len(word1),len(word2))
        res=[]
        while left<min_len:
            res.append(word1[left])
            res.append(word2[left])
            left+=1
        res.append(word1[left:])
        res.append(word2[left:])
        return "".join(res)


        