# A line of N kids is standing there. The rating values listed in the integer array ratings are assigned to each kid.


# These kids are receiving candy, according to the following criteria:


#     There must be at least one candy for every child.


#     Kids whose scores are higher than their neighbours receive more candies than their neighbours.


# Return the minimum number of candies needed to distribute among children.

class Solution:
    # To calculate the number of candies
    def candy(self, ratings):
        # Size of the ratings array
        n = len(ratings)
        
        # Initialize index variable
        i = 1
        
        '''Initialize the total number of candies,
        starting with one candy for the first child'''
        sum = 1
        
        # Loop the ratings array
        while i < n:
            
            '''Check if the current child's rating
            is equal to the previous one'''
            if ratings[i] == ratings[i - 1]:
                
                '''If so, give the current child one
                more candy than the previous one'''
                sum += 1
                
                '''Move to the next child'''
                i += 1
                
                '''Skip the rest of the loop and
                move to the next iteration'''
                continue
            
            '''Initialize the candy count
            for increasing rating trend'''
            peak = 1
            
            # Loop through increasing ratings trend
            while i < n and ratings[i] > ratings[i - 1]:
                
                '''Increment candy count
                for increasing trend'''
                peak += 1
                
                '''Update the total
                number of candies'''
                sum += peak
                
                # Move to next
                i += 1
            
            '''Initialize the candy count
            for decreasing rating trend'''
            down = 1
            
            # Loop through decreasing ratings trend
            while i < n and ratings[i] < ratings[i - 1]:
                
                '''Update the total number of
                candies for decreasing trend'''
                sum += down
                
                # Move to next
                i += 1
                
                '''Increment the candy
                count for decreasing trend'''
                down += 1
            
            '''Check if the candy count for
            decreasing trend exceeds the peak'''
            if down > peak:
                '''Adjust the total number of
                candies to satisfy the condition'''
                sum += (down - peak)
        
        # Return total candies
        return sum
ratings = [1, 0, 5]
print(Solution().candy(ratings))