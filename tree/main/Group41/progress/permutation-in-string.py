class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = Counter(s1)
        left = 0
        s2_freq = Counter( s2[:len(s1)] )
        if s1_freq == s2_freq:
            return True

        for right in range(len(s1),len(s2)):
            s2_freq[s2[left]] -= 1
            
            if s2_freq[s2[left]] == 0:
                s2_freq.pop(s2[left])
            left += 1
            
            s2_freq[s2[right]] = s2_freq.get(s2[right],0) + 1
            if s2_freq == s1_freq :
                return True

        return False


