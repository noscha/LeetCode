class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        """
        Use Prefix sum and update if better than to start from current position
        """

        for i in range(k, len(energy)):

            _temp = energy[i - k] + energy[i]
            energy[i] = _temp if _temp > energy[i] else energy[i]

        return max(energy[-k:])
