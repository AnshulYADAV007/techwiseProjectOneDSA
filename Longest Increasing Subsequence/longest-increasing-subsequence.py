class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = [1] * len(nums)
        # Length[i] is the length of the longest increasing subsequence
        # ending at index i.
        print(nums)
        for i in range(len(nums)):
            for j in range(i):
                if(nums[i] > nums[j]):
                    length[i] = max(length[i], length[j] + 1)
            print(nums[i], length)
        return max(length)


"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.longestCommonSubsequence(nums, sorted(list(set(nums))))
    
    def longestCommonSubsequence(self, text1, text2) -> int:
        dp = [[-1] * len(text2) for _ in range(len(text1))]
        def helper(i1, i2):
            if i1 == len(text1) or i2 == len(text2):
                return 0
            
            if dp[i1][i2] != -1:
                return dp[i1][i2]

            choice1 = 0
            if text1[i1] == text2[i2]:
                choice1 = 1 + helper(i1 + 1, i2 + 1)
            
            choice2 = helper(i1 + 1, i2)
            choice3 = helper(i1, i2 + 1)
            dp[i1][i2] = max([choice1, choice2, choice3])
            return dp[i1][i2]

        return helper(0, 0)
"""
