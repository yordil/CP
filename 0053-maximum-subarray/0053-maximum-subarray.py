class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #using kaden's Algorithm can be implmented in O(n) time complexity
        
        cur = 0 
        
        maxval = nums[0]
        
        for n in nums:
            cur = max(cur , 0)
            
            cur += n
            
            maxval = max(maxval , cur)
            
        return maxval
    
    
#using kaden's Algorithm can be implmented in O(n) time complexity