class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum={0:1}
        res=0
        summ=0
        for n in nums:
            summ+=n
            if summ-k in prefixSum:
                res+=prefixSum.get(summ-k,0)
            prefixSum[summ]=1+prefixSum.get(summ,0)
        return res
        