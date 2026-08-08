class Solution:

    def encode(self, strs: List[str]) -> str:
        message = []
        mainStr = []
        idx = 0
        for i in range(len(strs)):
            message.append(str(idx))
            message.append(".")
            for j in range(len(strs[i])):
                idx += 1
                mainStr.append(strs[i][j])

        message.append(str(idx))
        #print("".join(message) + "".join(mainStr))
        return "".join(message) + "|" + "".join(mainStr)

    def decode(self, s: str) -> List[str]:
        messageEnd = s.find("|")
        message = s[:messageEnd]
        mainStr = s[messageEnd+1:]
        #print(message, mainStr)

        ans = []

        indices = message.split(".")
        #print(indices)
        for i in range(1, len(indices)):
            idx = int(indices[i])
            prev = int(indices[i-1])
            ans.append(mainStr[prev:idx])
        
        return ans



"""
need way to handle delimiters
    - "message" at the start of the string indicating where the splits are
    - ["Hello", "World"] -> "0.5_HelloWorld"

Encode (O(n * m)):
    - Loop through every string, and every character of the string
    - Keep track of what index starts each string
    - Construct message
Decode (O(n * m)):
    - separate message from combined string
    - Loop through all characters of message and separate encoded string into original array
"""
