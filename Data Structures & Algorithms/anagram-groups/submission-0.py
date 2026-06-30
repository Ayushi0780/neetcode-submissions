class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        ana=defaultdict(list)
        for i in strs:
            sortedkey="".join(sorted(i))
            ana[sortedkey].append(i)  
        
        
    
        return list(ana.values())    

        