class Solution:
    def trap(self, height: List[int]) -> int:
        left_max=0
        right_max=0
        left=[0]*len(height)
        right=[0]*len(height)
        for i in range(len(height)):
            j=-i-1
            left[i]=left_max
            right[j]=right_max
            left_max=max(height[i],left_max)
            right_max=max(height[j], right_max)
        res=0
        print(left)
        print(right)
        for i in range(len(height)):
            p=min(left[i], right[i])
            res+=max(0,p-height[i])
        return res
        