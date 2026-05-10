class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mapper = defaultdict(list)

        for s in strs:
            sval = "".join(sorted(s))
            print(sval)
            mapper[sval].append(s)
        return list(mapper.values())

        