class Solution:
    def sortVowels(self, s: str) -> str:
        """
        Store vowels in extra list to sort them
        """

        s = list(s)
        new_s = []
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        for i in range(len(s)):

            if s[i] in vowels:

                new_s.append(s[i])
                s[i] = -1

        new_s.sort()

        for i in range(len(s)): 
            
            if s[i] == -1:

                s[i] = new_s.pop(0)

        return "".join(s)
