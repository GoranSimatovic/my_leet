class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        counter = 0
        i = 0
        while counter < len(nums):

            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0,0)
                i += 1
            elif nums[i] == 2:
                nums.pop(i)
                nums.append(2)
            else:
                i += 1

            counter +=1
            
        return nums
