from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        word_len = len(words[0])
        total_words = len(words)
        req_count = Counter(words)
        res=[]

        for i in range(word_len):
            l = i
            r = i
            seen = {}
            count =0
            while r+ word_len <= len(s):
                word = s[r: r+ word_len]
                r+= word_len

                if word in req_count:
                    seen[word] = seen.get(word,0)+1
                    count+=1

                    while seen[word] > req_count[word]:
                        lword = s[l: l+word_len]
                        seen[lword]-=1
                        l+=word_len
                        count-=1
                    if count == total_words:
                        res.append(l)
                else:
                    seen.clear()
                    count=0
                    l=r
        return res
                
                
                
        