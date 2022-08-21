class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        look_up = {}
               
        i = 0
        while i < len(nums):
            
            if nums[i] in look_up:
                nums.pop(i)
            else:
                look_up[nums[i]] = 0
                i +=1
            
        return len(look_up.keys())
