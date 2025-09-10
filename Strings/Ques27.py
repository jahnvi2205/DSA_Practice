def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix= strs[0]
        for k in strs[1:]:
            if len(prefix)>len(k):
                prefix= prefix[:len(k)]

            j=0
            while j<len(prefix):
                if prefix[j]==k[j]:
                    j+=1
                else:
                    break

            prefix= prefix[:j]

        return prefix
