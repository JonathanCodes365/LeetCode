class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for word in strs:
            #what we are saying is we are going from 1 word to another..
            # 1 string to another?
#since these are anagrams we are talking about; we need to make sure that if they are anagrams of each other then ; we need to have something that can take them together?

#I mean something that can represent these anagram by a single Key.
            keys = "".join(sorted(word))

#Yes .. key so: we can use dictionary for this...
            #initiating dictionary outside of this.
            if keys in groups:
                #now it is simple we created a alpabhetic key for this anagram.
                #now if it is already inside the group; we need to add that new word   
                groups[keys].append(word)
            else:
                #what if it is not inside..
                #if it is not inside ; we need to make sure that it is added.

                #remember this CLI...
                groups[keys]=[word]
                # dictionary[key] = value..
                #if it doesnt have value already then it will add if it does; it will modify.

                #the output is asking for the list
                #we dont know all the keys that might be in the system 
                #so to get the values of the system we just return groups.values...
        return list(groups.values())