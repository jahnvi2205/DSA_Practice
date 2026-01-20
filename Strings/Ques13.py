def solveWordWrap(self, arr, k):
		n = len(arr)

    # dp[i] = minimum punishment if we start wrapping from word i
        dp = [float('inf')] * (n + 1)

    # no words left → no cost
        dp[n] = 0

    # fill dp from back to front
        for i in range(n - 1, -1, -1):
            length = 0

            for j in range(i, n):
                length += arr[j]

                if j > i:
                    length += 1  # space between words

                if length > k:
                    break

                if j == n - 1:
                    cost = 0  # last line has no penalty
                else:
                    extra = k - length
                    cost = extra * extra

                dp[i] = min(dp[i], cost + dp[j + 1])

        return dp[0]