class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count=1
        max_count=1
        x=sorted(set(nums))
        y=list(x)
        for i in range(len(y)-1):
            if y[i]+1==y[i+1]:
                count+=1
            else:
                max_count=max(max_count,count)
                count=1
        max_count=max(max_count,count)
        return max_count

        