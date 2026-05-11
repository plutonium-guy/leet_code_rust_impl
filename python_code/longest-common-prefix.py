from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        smalles_word = min(strs, key=len)
        for index, char in enumerate(smalles_word):
            count = 0
            for i in strs:
                if char == i[index]:
                    count += 1
            if count != len(strs):
                break
            else:
                lcp = lcp + char
        return lcp


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
