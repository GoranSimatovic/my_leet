class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sum_arr = nums1 + nums2
        sum_arr.sort()
        middle = (len(sum_arr))//2

        if (len(sum_arr) % 2) ==0:
            return ((sum_arr[(middle)] + sum_arr[middle-1])/2.0)
        else:
            return sum_arr[middle]
