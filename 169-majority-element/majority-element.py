class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        import numpy as np
        c = Counter(nums)
        for i in c.keys():
            if c[i]>=int(np.ceil(len(nums)/2)):
                return i
        