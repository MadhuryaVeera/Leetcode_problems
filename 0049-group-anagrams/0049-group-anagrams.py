

     #use the same letters

    #the letters appear same number of times

      #but the letters are in a different/random arrangement

         #\U0001f449 then they are anagrams.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}             # Taking the empty dictionary  to push the group of anagrams on it.
        for word in strs:        # We are storing strs in word as a loop
            key = ''.join(sorted(word)) 
            if key  not in groups:
                groups[key]=[]
            groups[key].append(word) 

                    #word = "eat"
                    #sorted("eat") -> ['a','e','t']
                    #key = ''.join(...) -> "aet"
                    #"aet" not in groups, so groups["aet"] = []
                    #append "eat" -> groups = {"aet": ["eat"]}

                #2nd word = "tea"
                #sorted("tea") -> ['a','e','t']
                #key = "aet" (same as before)
                #"aet" is already in groups, so append "tea" -> groups = {"aet": ["eat", "tea"]}

                #3rd word = "tan"
                #sorted("tan") -> ['a','n','t']
                #key = "ant"
                #"ant" not in groups, create groups["ant"] = []
                #append "tan" -> groups = {"aet": ["eat","tea"], "ant": ["tan"]}

                #word = "ate"
                #sorted("ate") -> ['a','e','t'] -> key = "aet"
                #append "ate" to existing aet group -> groups = {"aet":["eat","tea","ate"], "ant":["tan"]}

                #word = "nat"
                #sorted("nat") -> ['a','n','t'] -> key = "ant"
                #append "nat" -> groups = {"aet":["eat","tea","ate"], "ant":["tan","nat"]}

                #last word = "bat"
                #sorted(word)=['a','b','t']
                #''.join(sorted(word)) = "abt"  -> key 
                #if abt in already group append the value in it , if not crete another group
                # Here there is not group so we should create it 
                #groups["abt"]=[]
                #append into the exsited group -> then gropu becomes
                # group={"aet":["ate","eat","tea"], "ant":["nat","tan"], "abt":["bat"]};

            #End of loop.
 
        return list(groups.values())     #-> [["eat","tea","ate"], ["tan","nat"], ["bat"]]
            


        