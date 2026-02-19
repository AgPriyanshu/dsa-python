# You are given an integer array asteroids representing asteroids in a row. Each asteroid moves at the same speed.
# The absolute value of an asteroid represents its size. The sign of an asteroid represents its direction: positive (+) means moving right, negative (-) means moving left.


# Collision rules:

#     Asteroids moving in the same direction never collide.
#     When two asteroids moving in opposite directions collide, the smaller asteroid explodes and the larger asteroid continues moving in the same direction.
#     If both asteroids are equal in size, both explode.
#     Collisions are resolved one at a time, from left to right. If an asteroid survives a collision, it continues moving and may collide immediately with the next asteroid in its path.

# Return the state of the asteroids after all collisions as an array in the same order.

class Solution:
    def asteroidCollision(self, asteroids):
        
        # Size of the array
        n = len(asteroids)
        
        # List implementation of stack
        st = []
        
        # Traverse all the asteroids
        for i in range(n):
            
            # Push the asteroid in stack if a 
            # right moving asteroid is seen
            if asteroids[i] > 0:
                st.append(asteroids[i])
            
            # Else if the asteroid is moving 
            # left, perform the collisions
            else:
                
                # Until the right moving asteroids are 
                # smaller in size, keep on destroying them 
                while (st and st[-1] > 0 and 
                       st[-1] < abs(asteroids[i])):
                    
                    # Destroy the asteroid
                    st.pop()
                
                # If there is right moving asteroid 
                # which is of same size
                if st and st[-1] == abs(asteroids[i]):
                    
                    # Destroy both the asteroids
                    st.pop()
                
                # Otherwise, if there is no left
                # moving asteroid, the right moving 
                # asteroid will not be destroyed
                elif not st or st[-1] < 0:
                    
                    # Storing the array in final state
                    st.append(asteroids[i])
        
        # Return the final state of asteroids
        return st

# Main function to test the solution
if __name__ == "__main__":
    arr = [10, 20, -10]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to determine the state of 
    # asteroids after all collisions
    ans = sol.asteroidCollision(arr)
    
    print("The state of asteroids after collisions is:", ans)
