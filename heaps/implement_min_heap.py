# You need to implement the Min Heap with the following given methods.

#     insert (x) -> insert value x to the min heap
#     getMin -> Output the minimum value from min heap
#     exctractMin -> Remove the minimum element from the heap
#     heapSize -> return the current size of the heap
#     isEmpty -> returns if heap is empty or not
#     changeKey (ind, val) -> update the value at given index to val (index will be given 0-based indexing)
#     initializeHeap -> Initialize the heap
class Solution:

    def heapifyUp(self,ind): 
      parent = (ind-1)//2 
      if ind > 0 and self.heap[parent] > self.heap[ind]:
        self.heap[parent],self.heap[ind] = self.heap[ind],self.heap[parent]
        self.heapifyUp(parent)


    def heapifyDown(self,ind): 
      smallest_ind = ind
      left_child_ind = 2*ind + 1
      right_child_ind = 2*ind + 2

      if left_child_ind < self.heapSize() and self.heap[left_child_ind] < self.heap[smallest_ind]:
        smallest_ind = left_child_ind

      if right_child_ind < self.heapSize() and self.heap[right_child_ind] < self.heap[smallest_ind]:
        smallest_ind = right_child_ind

      if smallest_ind != ind:        
        self.heap[smallest_ind],self.heap[ind] = self.heap[ind],self.heap[smallest_ind]
        self.heapifyDown(smallest_ind)      
    
    def initializeHeap(self):
      self.heap = []
      self.heap_size = 0
    
    def insert(self, key):
      self.heap.append(key)
      self.heapifyUp(self.heapSize())
      self.heap_size += 1

        

    def changeKey(self, index, new_val):
      if self.heap[index] > new_val:
          self.heap[index] = new_val
          self.heapifyUp( index)
      else:
          self.heap[index] = new_val
          self.heapifyDown( index)

      return


    def extractMin(self):
      self.heap[0],self.heap[self.heap_size -1] = self.heap[self.heap_size -1],self.heap[0]
      self.heap.pop()
      self.heap_size -= 1

      if self.heap_size > 0:
          self.heapifyDown(0)
     



    def isEmpty(self):
      return self.heapSize() == 0

    def getMin(self):
      # print(self.heap)
      return self.heap[0] 

    def heapSize(self):
      return self.heap_size

# Driver code
def main():
    # Creating an object of the Solution class
    heap = Solution()

    # Initializing a min heap data structure
    heap.initializeHeap()

    # Performing different operations
    heap.insert(4); print("Inserting 4 in the min-heap")
    heap.insert(1); print("Inserting 5 in the min-heap")
    heap.insert(10); print("Inserting 10 in the min-heap")
    print("Minimum value in the min-heap is:", heap.getMin())
    print("Size of min-heap is:", heap.heapSize())
    print("Is heap empty:", heap.isEmpty())
    print("Extracting minimum value from the heap")
    heap.extractMin()
    print("Changing value at index 0 to 10")
    heap.changeKey(0, 16)
    print("Minimum value in the min-heap is:", heap.getMin())
    



if __name__ == "__main__":
    main()