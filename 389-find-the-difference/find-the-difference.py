class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        p1=0
        p2=0
        while p1<len(s):
            if s[p1] !=t[p2]:
                return t[p2]
                break
            else:
                p1+=1
                p2+=1
        return t[-1]
        