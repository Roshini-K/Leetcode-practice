class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i in range(0, len(nums)):
            diff=target-nums[i]
            if diff in hm:
                return [i,hm[diff]]
            hm[nums[i]]=i
        