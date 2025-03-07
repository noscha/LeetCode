class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        """
        Get primes with Sieve of Eratosthenes, then find minimum of neighbouring tuples in sorted set
        """

        # Sieve of Eratosthenes
        nums = [0, 0] + [i for i in range(2, right + 1)]
        for i in range(2, int(sqrt(right)) + 1):
            if not nums[i]:
                continue
            multiple = i * i
            while multiple <= right:
                nums[multiple] = 0
                multiple += i

        # remove smaller then left
        primes = []
        for i in range(2, right + 1):
            if nums[i] and i >= left:
                primes.append(i)

        if len(primes) <= 1:
            return [-1, -1]

        # find pair smallest distance
        res = [primes[0], primes[1]]
        dist = primes[1] - primes[0]
        for i in range(2, len(primes)):
            new_dist = primes[i] - primes[i - 1]
            if new_dist < dist:
                dist = new_dist
                res = [primes[i - 1], primes[i]]

        return res
