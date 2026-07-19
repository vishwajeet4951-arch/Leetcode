class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=0
        ls=0
        for num in nums:
            total=total+num
        for i in range(len(nums)):
            rs=total-ls-nums[i]
            if ls==rs:
                return i
            ls=ls+nums[i]
        return -1
        