class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        pattern={}
        used_words=set()
        for i in range(len(s)):
            ch1=s[i]
            ch2=t[i]

            if ch1 in pattern:
                if pattern[ch1]!=ch2:
                    return False
            else:
                if ch2 in used_words:
                    return False
                pattern[ch1]=ch2
                used_words.add(ch2)
        return True
        