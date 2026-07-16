class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        t=0
        for num in nums:
            t+=num
            ans.append(t)
        return ans
        