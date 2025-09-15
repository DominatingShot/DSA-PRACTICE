from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")

        def mask(word):
            return "".join("0" if ch.lower() in vowels else ch for ch in word.lower())
        words = set(wordlist)

        lowerdict = {}
        novowdict = {} 

        for i in queries:
            lowerdict[i.lower()] = ""
            novowdict[mask(i)] = ""

        for i in wordlist[::-1]:
            lowerdict[i.lower()] = i
            novowdict[mask(i)] = i


        for i in range(len(queries)):
            if(queries[i] in words):
                continue
            elif(lowerdict[queries[i].lower()] != ""):
                queries[i] = lowerdict[queries[i].lower()]
            else:
                queries[i] = novowdict[mask(queries[i]).lower()]         
            
        return queries
