class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for n in nums:
            if n in freq:
                freq[n]+=1
            else:
                freq[n]=1
        limit=len(nums)//2
        for key in freq:
            if freq[key]>limit:
                return key