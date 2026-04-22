class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        volwels = ('a','e','i','o','u')
        l = 0
        r = len(s)-1
        while l<r:
            if s[l].lower() in volwels and s[r].lower() not in volwels:
                r-=1
            elif s[l].lower() not in volwels and s[r].lower() in volwels:
                l+=1
            elif s[l].lower() in volwels and s[r].lower() in volwels:
                s[l],s[r] = s[r],s[l]
                l+=1
                r-=1
            else:
                l+=1
                r-=1
        return ''.join(s)
        