class Solution:
    def maxSlidingWindow(self, nums: List[int], K: int) -> List[int]:
        res=[]

        for i in range(len(nums)- K+1):
            window = nums[i : i + K]
            res.append(max(window))
        return res

            
        