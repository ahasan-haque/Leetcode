class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        freq_s1 = dict()
        freq_s2 = dict()

        for i in range(ord('a'), ord('z')+ 1):
            freq_s1[chr(i)] = 0
            freq_s2[chr(i)] = 0

        for i in range(len(s1)):
            freq_s1[s1[i]] +=  1
            freq_s2[s2[i]] +=  1
        
        matched = 0
        for i in range(ord('a'), ord('z')+ 1):
            matched += bool(freq_s1[chr(i)] == freq_s2[chr(i)])
        
        left = 0
        for right in range(len(s1), len(s2)):
            if matched == 26:
                return True
            if freq_s1[s2[right]] == freq_s2[s2[right]]:
                matched -= 1
            elif freq_s1[s2[right]] == freq_s2[s2[right]] + 1:
                matched += 1
            
            freq_s2[s2[right]] += 1

            if freq_s1[s2[left]] == freq_s2[s2[left]]:
                matched -= 1
            elif freq_s1[s2[left]] + 1 == freq_s2[s2[left]]:
                matched += 1
                
            freq_s2[s2[left]] -= 1
            left += 1
        return matched == 26
