class Solution:
    def decodeString(self, s: str) -> str:
        currStr = []
        ans = []
        needExpand = []
        for i in range(len(s)):
            c = s[i]
            if c.isalpha():
                currStr.append(c)
            elif c.isdigit() and not s[i-1].isdigit():
                if needExpand:
                    needExpand[-1][1] += "".join(currStr)
                else:
                    ans.append("".join(currStr))
                
                currStr = []
                dig = ""
                idx = i
                while s[idx].isdigit():
                    #print(idx, s[idx])
                    dig += s[idx]
                    idx += 1
                #print(dig)
                needExpand.append([int(dig), ""])
            elif c == "]":
                needExpand[-1][1] += "".join(currStr)
                #print("".join(currStr), needExpand)
                expandedStr = needExpand[-1][1] * needExpand[-1][0]
                #print(expandedStr)
                needExpand.pop()
                if needExpand:
                    needExpand[-1][1] += expandedStr
                else:
                    ans.append(expandedStr)
                currStr = []
            
            #print(needExpand)
        
        ans.append("".join(currStr))
        return "".join(ans)



        """
        Stack of tuples (number, string to be replicated)

        [(2, a), (3, b)]
        When you see "]", pop the stack, replicate as needed, then add the result to the new top of stack

        [(2, abbb)]
        if top of stack doesn't exist when you try to add, append to ans
        """