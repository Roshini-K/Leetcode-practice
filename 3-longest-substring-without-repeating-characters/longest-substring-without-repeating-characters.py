class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm={}
        l=0
        res=0
        for r in range(len(s)):
            if s[r] not in hm:
                hm[s[r]]=r
            else:
                l=max(l,hm[s[r]]+1)
                hm[s[r]]=r
            res=max(res,r-l+1)
        return res

        