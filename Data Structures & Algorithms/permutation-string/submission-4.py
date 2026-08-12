class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        aFreq = [0] * 26
        bFreq = [0] * 26
        for i in range(len(s1)):
            aFreq[ord(s1[i]) - ord("a")] += 1
            bFreq[ord(s2[i]) - ord("a")] += 1
        
        def equals(arr1, arr2):
            for i in range(len(arr1)):
                if arr1[i] != arr2[i]:
                    return False
            return True
        print(bFreq)
        for R in range(len(s1), len(s2)):
            print(bFreq)
            if equals(aFreq, bFreq):
                return True
            Lidx = R - len(s1)
            print(Lidx, R)
            bFreq[ord(s2[R]) - ord("a")] += 1
            bFreq[ord(s2[Lidx]) - ord("a")] -= 1
        
        return equals(aFreq, bFreq)
        