def count(self, coins, s):
        amount= [0]* (s+1)
        amount[0]=1
        for coin in coins:
            for i in range(coin,len(amount)):
                amount[i]+= amount[i-coin]
                
                
        return amount[s]