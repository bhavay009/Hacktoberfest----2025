class Solution(object):
    def twoSum(self, nums, target):
        seen={}

        for i,num in enumerate(nums):
            a=target-num
            if a in seen:
                return [i,seen[a]]

            seen[num]=i    
