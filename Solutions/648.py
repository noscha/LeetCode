class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
         """ For each derivate in sentence, replace with the shortest root """
        sentence = sentence.split()
        dictionary.sort()

        for i in range(len(sentence)):
            for j in dictionary:
                if sentence[i].startswith(j):
                    sentence[i] = j
                    break
        return (" ").join(sentence)
