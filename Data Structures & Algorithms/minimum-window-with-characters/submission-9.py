from collections import defaultdict, Counter
import heapq
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = defaultdict(int)
        freqT = Counter(t)
        have, need = 0, len(freqT.keys())
        L = 0

        ansStart, ansEnd = -1, -1
        minLen = float("inf")
        if s[L] in t:
            window[s[L]] += 1
            if window[s[L]] == freqT[s[L]]:
                have += 1
                if have == need:
                    minLen = 1
                    ansStart, ansEnd = 0, 0


        for R in range(1, len(s)):
            if s[R] in t:
                window[s[R]] += 1
                if window[s[R]] == freqT[s[R]]:
                    have += 1
                
                #print(s[R], have, need)

                while have == need:
                    if s[L] in t:
                        window[s[L]] -= 1
                        if window[s[L]] < freqT[s[L]]:
                            have -= 1
                    #print(R-L+1)
                    if R-L+1 < minLen:
                        minLen = R-L+1
                        ansStart = L
                        ansEnd = R
                    L += 1
                
                #print(L, R)
                
        #print(ansStart, ansEnd, minLen)
        return s[ansStart:ansEnd+1] if minLen != float("inf") else ""


        
        """
        maxIdx, minIdx = -1, float("inf")

        freqT = Counter(t)
        chars = defaultdict(list)
        for i in range(len(s)):
            heapq.heappush(chars[s[i]], i)
            if len(chars[s[i]]) > freqT[s[i]]:
                heapq.heappop(chars[s[i]])

        for c in freqT.keys():
            if len(chars[c]) < freqT[c]:
                return ""

        for key in chars.keys():
            if len(chars[key]) > 0:
                minIdx = min(minIdx, min(chars[key]))
                maxIdx = max(maxIdx, max(chars[key]))
        
        return s[minIdx:maxIdx+1]
        """


        

