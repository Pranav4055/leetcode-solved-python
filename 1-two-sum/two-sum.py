class Solution(object):
    def twoSum(self, nums, target):
        num_hash = {}
        
        for i in range(len(nums)):
            if target - nums[i] in num_hash:
                return [num_hash[target - nums[i]], i]
            
            num_hash[nums[i]] = i