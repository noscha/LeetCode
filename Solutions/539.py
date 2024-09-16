class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """ Sort and calculate dist of neighboring times """
        res = 24 * 60
        timePoints.sort()
        h, m = timePoints[-1].split(':')
        prev = int(m) + 60 * int(h)

        for i in range(len(timePoints)):
            h, m = timePoints[i].split(':')
            time = int(m) + 60 * int(h)
            diff = min(abs(time - prev), 24 * 60 - abs(time - prev))
            prev = time
            res = min(res, diff)

        return res
