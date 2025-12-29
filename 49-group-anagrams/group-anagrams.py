from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm=defaultdict(list)
        for s in strs:
            ch=[0]*26
            for i in s:
                ch[ord(i)-ord('a')]+=1
            hm[tuple(ch)].append(s)
        return list(hm.values())
            
        