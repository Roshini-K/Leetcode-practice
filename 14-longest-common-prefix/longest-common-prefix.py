class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minn=float("inf")
        for i in strs:
            if len(i)<minn:
                minn=len(i)
        j=0
        while j<minn:
            for s in strs:
                if s[j]!=strs[0][j]:
                    return s[:j]
            j+=1
        return strs[0][:j]