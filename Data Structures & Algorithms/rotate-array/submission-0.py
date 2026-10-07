class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        # Handle cases where k is larger than the list length
        k = k % length 
        
        if k > 0:
            # The nums[:] syntax overwrites the original list in-place
            nums[:] = nums[-k:] + nums[:-k]