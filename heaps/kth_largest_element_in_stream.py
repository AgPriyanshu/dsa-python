

# Implement a class KthLargest to find the kth largest number in a stream. It should have the following methods:

#     KthLargest(int k, int [] nums) Initializes the object with the integer k and the initial stream of numbers in nums
#     int add(int val) Appends the integer val to the stream and returns the kth largest element in the stream.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.
import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.K = k  # Integer K
        self.pq = []  # Min-heap

        # Traverse all the elements in the array
        for num in nums:
            # If the size of min-heap is less than k
            if len(self.pq) < self.K:
                heapq.heappush(self.pq, num)  # Add the current element

            # Else if the top element is smaller than the current element
            elif num > self.pq[0]:
                heapq.heappop(self.pq)  # Pop the top element
                heapq.heappush(self.pq, num)  # Add the current element

    def add(self, val):
        # If the size of the queue is less than K
        if len(self.pq) < self.K:
            heapq.heappush(self.pq, val)

            return self.pq[0]

        # If the smallest element is less than the element to be added
        if val > self.pq[0]:
            heapq.heappop(self.pq)  # Remove the top element
            heapq.heappush(self.pq, val)  # Add the current element

        return self.pq[0]  # Return the Kth largest element
            

