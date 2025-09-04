def wordBreak(self, s: str, d: List[str]) -> bool:
        dp=[True]+ [False]*len(s)

        for i in range(1,len(s)+1):
            for w in d:
                start= i-len(w)
                if start>=0 and dp[start] and s[start:i]==w:
                    dp[i]=True
                    break

        return dp[-1]