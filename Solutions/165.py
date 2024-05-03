class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """ Compare each revision """
        version1, version2 = version1.split('.'), version2.split('.')
        max_length = max(len(version1), len(version2))
        for i in range(max_length):
            v1 = int(version1[i]) if i < len(version1) else 0
            v2 = int(version2[i]) if i < len(version2) else 0
            if v1 - v2 != 0:
                return (v1 - v2) // abs(v1 - v2)
        return 0
