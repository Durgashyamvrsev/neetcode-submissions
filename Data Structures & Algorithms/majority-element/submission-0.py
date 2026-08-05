class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        x=len(nums)/2
        for key,value in freq.items():
            if value>x:
                return key
            
        

        