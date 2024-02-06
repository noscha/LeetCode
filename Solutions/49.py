class Solution:
    """ Count occurrences of each char and look for strings with the same amount """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            counter = [0 for i in range(26)]
            for c in s:
                counter[ord(c) - 97] += 1
                
            if tuple(counter) not in hm:
                hm[tuple(counter)] = [s]
            else:
                hm[tuple(counter)].append(s)
        return hm.values()
