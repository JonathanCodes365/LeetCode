class Solution(object):
    def groupAnagrams(self, strs):
        
        #Using tuples 

        groups = {}
        #we are still using dictionary..
        #we are just using tuples as our keys..

        for word in strs:
            #so there are 26 alphabets so we need an array capable of holding 26 alphabets.
            count=[0]*26
            #it creates [0 ,0 ,0 ,0, 0,0,0,0,0,,0,0,0,0,0,.....]
            #26 of them...

            #now we need to make sure that ; when a letter is given --> we convert that letter into a alphabet..
            #so heres how we do it

            #we use ord()..-> when we use ord('a') --> it gives the unicode of a.

            for char in word:
                index = ord(char) - ord('a')
                count[index] +=1
                #now we have got the indexing and proper markings of words here.
                #we want to make sure; we properly make it a key..
                #we use tuples here as the key that stores it 

            key = tuple(count)

            if key in groups:
                groups[key].append(word)
            else:
                groups[key]=[word]
#note : our keys are tuple: but the values of the key in dictionary views are lists.
        return list(groups.values())





