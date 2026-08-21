class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        #lets us start from our index 0.
        lowest = prices[0]

        #after LOC 18
        #now since ,we have found the lowest of them all and we can never sell back in time.. we have to look forward
        current_profit = 0
        profit = 0
        for price in prices:

            #so i want a variable that can actually record the lowest i have seen so far.
            #note this is for buy : this means lowest is from 1 day before
            if price <= lowest:
                lowest = price
            else:
                profit = price - lowest
                if profit > current_profit:
                    current_profit = profit
                    #know this that return completely terminates the loop and gives back what is left... it doesnt give other elements the chance.
        return current_profit
                
                
       
            
                