from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = Counter(words)
        total_words = len(words)
        
        res = []
        
        for i in range(word_len):  # offsets
            left = i
            right = i
            seen = {}
            count = 0
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1
                    
                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    if count == total_words:
                        res.append(left)
                
                else:
                    seen.clear()
                    count = 0
                    left = right
        
        return res