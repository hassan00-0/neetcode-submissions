class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}

        for n in s:
            if n in dic1:
                dic1[n] +=1
            else:
                dic1[n] = 0

        for m in t:
            if m in dic2:
                dic2[m] += 1
            else:
                dic2[m] = 0
        return dic1 == dic2