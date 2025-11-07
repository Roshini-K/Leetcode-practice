class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hmap={}
        for i,j in zip(s,t):
            if i in hmap:
                if hmap[i]!=j:
                    return False
            elif j in hmap.values():
                return False
            else:
                hmap[i]=j
        return True
        