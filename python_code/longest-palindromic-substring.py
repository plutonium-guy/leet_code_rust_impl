# idea is simple :- expand from center
from operator import le


class Solution:
    def longestPalindrome(self, s: str) -> str:
        final_str = ""
        final_len = 0
        for i in range(0, len(s)):
            # for odd
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > final_len:
                    final_len = r - l + 1
                    final_str = s[l : r + 1]
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > final_len:
                    final_len = r - l + 1
                    final_str = s[l : r + 1]
                l -= 1
                r += 1
        return final_str
