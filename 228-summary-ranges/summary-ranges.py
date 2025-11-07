class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [str(nums[0])]
        start=nums[0]
        for i in range(0,len(nums)-1):
            if nums[i]+1==nums[i+1]:
                end=nums[i+1]
            else:
                end=nums[i]
                if start==end:
                    res.append(str(start))
                    start=nums[i+1]
                else:
                    t=f"{start}->{end}"
                    res.append(t)
                    start=nums[i+1]
                    end=nums[i+1]
        # if start==end:
        #     res.append(str(start))
        # elif start<end:
        #     res.append(f"{start}->{end}")
        # else:
        #     res.append(str(end))

        if start<end:
            res.append(f"{start}->{end}")
        else:
            res.append(str(start))
        print(start)
        print(end)
        return res
            

        