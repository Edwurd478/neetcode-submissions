from collections import defaultdict
class Solution:
    def applySubstitutionsHelper(self, text: str) -> str:
        print(text)
        #find all placeholders
        placeholders = set()
        curr = prev = counter = 0
        for i in range(len(text)):
            if text[i] == "%":
                counter += 1
                prev = curr
                curr = i
                #print(prev, curr, counter)
                if counter % 2 == 0:
                    #print(text[prev+1:curr])
                    placeholders.add(text[prev+1:curr])

        #print(placeholders)

        #replace
        for p in placeholders:
            replacementValue = self.reps[p]
            #print(replacementValue, "%"+p+"%", text)
            text = text.replace("%"+p+"%", self.applySubstitutionsHelper(replacementValue))

        return text
    
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        self.reps = defaultdict(str)
        
        #precompute dictionary
        for i in range(len(replacements)):
            self.reps[replacements[i][0]] = replacements[i][1]
        
        #print(self.reps)
        
        return self.applySubstitutionsHelper(text)
        

"""
1. Find all placeholders
    - split by underscore -> gives a list of all placeholders
    - trim the %'s on either side to get keys
2. Make a dictionary of replacements
    - List[List[str]] -> dict
3. Use recursion to replace all placeholders with dict value
    - run function on replacement recursively until no placeholders remain
        - base case: no replacements
    - search by detecting % (cannot split by underscore)
"""