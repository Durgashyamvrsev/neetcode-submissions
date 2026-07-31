class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=0
        res = ""

        for ch in s:
            if ch.isalnum():
                res += ch.lower()

        
        s2=len(res)-1
        while s1<s2:
            if res[s1]!=res[s2]:
                return False
                break
            s1+=1
            s2-=1
        return True

        