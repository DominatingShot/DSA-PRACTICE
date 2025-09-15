class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l = text.split()
        count = 0
        for i in l:
            count += 1
            for j in i:
                if j in brokenLetters:
                    count -= 1
                    break
        return count
            