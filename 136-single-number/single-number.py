class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        else:
            nums.sort()
            i = 0
            j = 1
            while j<len(nums):
                if nums[i] != nums[j]:
                    return nums[i]
                    break
                else:
                    i+=2
                    j+=2
        return nums[i]
        