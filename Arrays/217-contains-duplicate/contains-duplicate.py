class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        seen = set()
        #we use the property of set .i.e. whether it is present or not ..?
        #but 1st , we need loop for this comparison and we need the number itself.
        for number in nums:
            if number in seen:
                return True
            else:
                seen.add(number)
        return False