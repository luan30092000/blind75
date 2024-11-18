class Solution:
    def findMin(self, nums: list[int]) -> int:
        '''
        153. Find Minimum in Rotated Sorted Array
        bigO: log(N)
        '''
        res = nums[0]
        l, r = 0, len(nums) - 1
        
        while l <= r:   # generic condition
            if nums[r] > nums[l]:   # found unshifted minimum portion -> max is right most, min is left most -> take left most
                res = min(res, nums[l])
                break
            else:   # l to r portion is shifted -> max and min stand next to each other
                m = (l + r) // 2
                res = min(res,nums[m])
                if nums[m] >= nums[l]:  # max is next to min -> max and min is on the right
                    l = m + 1
                else:   # max is next to min -> max and min is on the left
                    r = m - 1
        return res
    def search(self, nums: list[int], target: int) -> int:
        '''
        33. Search in Rotated Sorted Array
        bigO: log(N)
        '''
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]: return m
            # left portion of mid is sorted (aka mid belong to left portion)
            if nums[m] >= nums[l]: # TODO: Why >= but not >
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else: 
                    l = m + 1
        
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1