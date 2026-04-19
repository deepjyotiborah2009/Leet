class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=3 and n!=1:
            return False
        elif n==1:
            return True
        else:
            while n>=4:
                r = n%4
                n = n//4
                if r!=0:
                    return False
                    break

            if n==1:
                return True
            else:
                return False
        