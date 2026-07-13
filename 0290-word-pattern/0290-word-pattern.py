class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        pattern_to_word={}
        used_words=set()
        for i in range(len(pattern)):
            ch=pattern[i]
            word=words[i]
            if ch in pattern_to_word:
                if pattern_to_word[ch]!=word:
                    return False
            else:
                if word in used_words:
                    return False

                pattern_to_word[ch]=word
                used_words.add(word)
        return True
        