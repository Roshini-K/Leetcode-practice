class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        summ=0
        res=len(nums)+1
        for r in range(0, len(nums)):
            summ+=nums[r]
            while summ>=target:
                res=min(res, r-l+1)
                summ-=nums[l]
                l+=1
        return 0 if res==len(nums)+1 else res

