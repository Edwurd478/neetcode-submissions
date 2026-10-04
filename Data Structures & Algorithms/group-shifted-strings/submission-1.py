"""
Hash map: tuple of differences btwn letters -> string
abc -> (1, 1)
acef -> (2, 2, 1)
bca -> (1, -2)
"""
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        result = []
        shifts = {}

        for string in strings:
            diffs = []
            for i in range(1, len(string)):
                diff = ord(string[i]) - ord(string[i-1])
                if diff < 0:
                    diff += 26
                diffs.append(diff)
            diffs = tuple(diffs)
            if diffs not in shifts:
                shifts[diffs] = []
            shifts[diffs].append(string)
        
        for grouping in shifts:
            result.append(shifts[grouping])
        return result