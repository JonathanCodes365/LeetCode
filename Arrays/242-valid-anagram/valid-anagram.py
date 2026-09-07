class Solution(object):
    def isAnagram(self, s, t):
        x = len(s)
        y = len(t)

        if x != y:
            return False
        #okay we counted the total number of characters in both of them
        #if they are not equal they will be naturally returned false and program will terminate.

        #Assuming they have the same length.
        #Now, 1 way is we can check each and every one of those words 1 by 1.
        count_s={}
        for char in s:
            if char in count_s:
                count_s[char]+=1
            else:
                count_s[char]=1

        count_t ={}
        for char in t:
            if char in count_t:
                count_t[char] +=1
            else:
                count_t[char] =1
        return count_s == count_t



        
