class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for i,j in enumerate(digits):
            num+=j*(10**(len(digits)-i-1))

        num_1 = num+1
        res=[]
        for i in str(num_1):
            res.append(int(i))
        return res

        