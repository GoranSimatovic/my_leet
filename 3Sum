class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       
        res = []
        nums.sort()
        
        for i, first in enumerate(nums):
            
            if i > 0 and first == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            
            while l<r:
                
                
                if first + nums[l] + nums[r] >0:
                    r -= 1
                
                elif first + nums[l] + nums[r] <0:
                    l += 1
                    
                else:
                    if [first,  nums[l], nums[r]] not in res:
                        res.append([first,  nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
                        
        return res
