class Solution:
    def candy(self, ratings: list) -> int:
        if not ratings or len(ratings) == 0:
            return 0
        
        candies = [1]

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies.append(candies[i-1] + 1)
            else:
                candies.append(1)
        
        result = candies[-1]

        for j in range(len(ratings) - 2, -1, -1):
            cur = 1

            if ratings[j] > ratings[j+1]:
                cur = candies[j+1] + 1
            
            result += max(cur, candies[j])
            candies[j] = cur
        
        return result
