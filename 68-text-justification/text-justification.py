class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res=[]
        line,length=[],0 #words, no of spaces
        i=0
        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                extra = maxWidth - length
                spaces = extra//max(1,len(line)-1)
                remainder = extra % max(1,len(line)-1)

                for j in range(max(1, len(line) -1)):
                    line[j] += " "*spaces
                    if remainder:
                        line[j]+= " "
                        remainder -=1
                res.append(("").join(line))
                line, length = [],0

            line.append(words[i])
            length += len(words[i])
            i+=1

        last_line = " ".join(line)
        trail = maxWidth - len(last_line)
        res.append(last_line+ " "*trail)
        return res