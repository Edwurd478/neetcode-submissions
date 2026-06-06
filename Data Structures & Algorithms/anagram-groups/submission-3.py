class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        ans = []
        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str in mp.keys():
                ans[mp[sorted_str]].append(s)
            else:
                ans.append([s])
                mp[sorted_str] = len(ans)-1
        return ans
