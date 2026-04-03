class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        
        while i < len(words):
            # Step 1: take words for one line
            line_len = len(words[i])
            j = i + 1
            
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            
            line_words = words[i:j]
            num_words = len(line_words)
            
            # Step 2: check if last line OR single word
            if j == len(words) or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            
            else:
                total_chars = sum(len(word) for word in line_words)
                total_spaces = maxWidth - total_chars
                gaps = num_words - 1
                
                space_each = total_spaces // gaps
                extra = total_spaces % gaps
                
                line = ""
                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (space_each + (1 if k < extra else 0))
                
                line += line_words[-1]
            
            res.append(line)
            i = j
        
        return res