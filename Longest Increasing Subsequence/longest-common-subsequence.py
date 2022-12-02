class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(len(text1) * len(text2))
        def helper(i1, i2):
            if i1 == len(text1) or i2 == len(text2):
                return 0

            choice1 = 0
            if text1[i1] == text2[i2]:
                choice1 = 1 + helper(i1 + 1, i2 + 1)

            choice2 = helper(i1 + 1, i2)
            choice3 = helper(i1, i2 + 1)
            return max([choice1, choice2, choice3])

        return helper(0, 0)
