class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index_j: int = 0
        if len(s) == 0 or len(t) == 0:
            return False
        for i in t:
            if s[index_j] == i:
                index_j += 1
        if len(s) == index_j:
            return True
        return False


print(Solution().isSubsequence("aec", "abcde"))
