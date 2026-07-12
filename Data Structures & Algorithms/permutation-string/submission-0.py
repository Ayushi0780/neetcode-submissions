class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            # s1 cannot fit inside s2 if it is longer
            return False  

        # Create a frequency map of the characters we are looking for
        s1_count = Counter(s1)
        
        # Look at every possible window of length n1 inside s2
        for i in range(n2 - n1 + 1):
            # Take a slice of s2 matching s1's exact length
            window = s2[i : i + n1]
            
            # If the character frequencies match exactly, it is a permutation
            if Counter(window) == s1_count:
                return True
                
        return False

        