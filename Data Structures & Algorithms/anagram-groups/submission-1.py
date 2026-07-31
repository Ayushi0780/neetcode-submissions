class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_value={}
        for s in strs:
            key=''.join(sorted(s))

            if key not in dict_value:
                dict_value[key]=[]
            dict_value[key].append(s)    
                
        return list(dict_value.values())    
