# There are a total of N tasks, labeled from 0 to N-1. Given an array arr where arr[i] = [a, b] indicates that you must take course b first if you want to take course a. Find if it is possible to finish all tasks.
from collections import deque
class Solution:
    # Function to return the topological
    # sorting of given graph
    def topoSort(self, V, adj):
        
        # To store the In-degrees of nodes
        inDegree = [0] * V
        
        # Update the in-degrees of nodes
        for i in range(V):
            
            for it in adj[i]:
                # Update the in-degree
                inDegree[it] += 1

        # To store the result
        ans = []
        
        # Queue to facilitate BFS
        q = deque()
        
        # Add the nodes with no in-degree to queue
        for i in range(V):
            if inDegree[i] == 0:
                q.append(i)
        
        # Until the queue is empty
        while q:
            
            # Get the node
            node = q.popleft()
            
            # Add it to the answer
            ans.append(node)
            
            # Traverse the neighbours
            for it in adj[node]:
                
                # Decrement the in-degree
                inDegree[it] -= 1
                
                # Add the node to queue if 
                # its in-degree becomes zero
                if inDegree[it] == 0:
                    q.append(it)
        
        # Return the result
        return ans

    # Function to determine if all 
    # the tasks can be finished
    def canFinish(self, N, arr):
        
        # To store the graph
        adj = [[] for _ in range(N)]
        
        # Form the graph
        for it in arr:
            u = it[0]
            v = it[1]
            
            # Add the edge v-> u
            adj[v].append(u)
        
        # Get the topological ordering of graph
        topo = self.topoSort(N, adj)
        
        # If it doesn't contain
        # all nodes, return false
        if len(topo) < N:
            return False
        
        # Return true otherwise
        return True