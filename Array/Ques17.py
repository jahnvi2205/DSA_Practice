def maxProfit(self, prices: List[int]) -> int:
        profit= 0
        minp= prices[0]
        for i in range(1,len(prices)):
            if prices[i]<minp:
                minp=prices[i]
            calc= prices[i]-minp
            profit=max(profit,calc)

        return profit