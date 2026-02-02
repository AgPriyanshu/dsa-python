# Given an undirected graph with V vertices labeled from 0 to V-1. The graph is represented using an adjacency list where adj[i] lists all nodes connected to node. Determine if the graph contains any cycles.

# Note: The graph does not contain any self-edges (edges where a vertex is connected to itself).
from collections import deque

class Solution:

    # Function to perform DFS traversal
    def dfs(self, i, adj, visited, prev):
        # Mark the node as visited
        visited[i] = True
        
        # Traverse all the neighbors
        for node in adj[i]:
            
            # If not visited
            if not visited[node]:
                
                # Recursively perform DFS, and 
                # return true if cycle is found
                if self.dfs(node, adj, visited, i):
                    return True
                    
            # Else if it is visited with some 
            # different parent a cycle is detected
            elif node != prev:
                return True
        
        # Return false if no cycle is detected
        return False
    
    # Function to perform BFS traversal
    def bfs(self, i, adj, visited):
        # Queue to store (node, parent)
        q = deque()
        
        # Push initial node in queue 
        # with no one as parent
        q.append((i, -1))
        
        # Mark the node as visited
        visited[i] = True
        
        # Until the queue is empty
        while q:
            # Get the node and its parent
            node, parent = q.popleft()
            
            # Traverse all the neighbors
            for it in adj[node]:
                # If not visited
                if not visited[it]:
                    # Mark the node as visited
                    visited[it] = True
                    
                    # Push the new node in queue 
                    # with curr node as parent
                    q.append((it, node))
                    
                # Else if it is visited with some 
                # different parent a cycle is detected
                elif it != parent:
                    return True
        return False

    # Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):
        visited = [False] * V
        ans = False
        
        # Start Traversal from every unvisited node
        for i in range(V):
            if not visited[i]:
                # Start BFS traversal and update result
                ans = self.bfs(i, adj, visited)
                
                # Break if a cycle is detected
                if ans:
                    break
        return ans




    

if __name__ == "__main__":
  # V = 6 
  # adj= [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
  V = 4
  adj= [[1, 2], [0], [0, 3], [2]]
  print(Solution().isCycle(V,adj))