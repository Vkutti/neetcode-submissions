class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
            
        nums.sort()
        max_len = 1
        current_streak = 1

        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1]:
                if nums[i] + 1 == nums[i+1]:
                    current_streak += 1
                else:
                    max_len = max(max_len, current_streak)
                    current_streak = 1
        
        return max(max_len, current_streak)