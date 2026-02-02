# Given a directed graph with V vertices labeled from 0 to V-1. The graph is represented using an adjacency list where adj[i] lists all nodes adjacent to node i, meaning there is an edge from node i to each node in adj[i]. A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node. Return an array containing all the safe nodes of the graph in ascending order.
from typing import List
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

    # Function to get the
    # eventually safe nodes
    def eventualSafeNodes(self, V, adj):
        
        # To store the reverse graph
        adjRev = [[] for _ in range(V)]
        
        # Reversing the edges
        for i in range(V):
            
            # i -> it, it-> i
            for it in adj[i]:
                
                # Add the edge to reversed graph
                adjRev[it].append(i)
        
        # Return the topological 
        # sort of the given graph
        result = self.topoSort(V, adjRev)
        
        # Sort the result
        result.sort()
        
        # Return the result
        return result
class Solution:
    
    # Function to perform DFS traversal 
    # while checking for safe nodes
    def dfsCheck(self, node: int, adj: List[List[int]], 
                 vis: List[bool], 
                 pathVis: List[bool], 
                 check: List[bool]) -> bool:
                      
        # Mark the node as visited
        vis[node] = True
        
        # Add the node to current path
        pathVis[node] = True
        
        # Mark the node as potentially unsafe
        check[node] = False
        
        # Traverse for adjacent nodes
        for it in adj[node]:
            
            # When the node is not visited
            if not vis[it]:
                
                # Perform DFS recursively and if 
                # a cycle is found, return false
                if self.dfsCheck(it, adj, vis, pathVis, check):
                    
                    # Return true since a 
                    # cycle was detected
                    return True

            # Else if the node has been previously 
            # visited in the same path
            elif pathVis[it]:
                
                # Return true since a 
                # cycle was detected
                return True
        
        # If the current node neither exist 
        # in a cycle nor points to a cycle, 
        # it can be marked as a safe node
        check[node] = True
        
        # Remove the node from the current path
        pathVis[node] = False
        
        # Return false since no cycle was found
        return False

    # Function to get the eventually safe nodes
    def eventualSafeNodes(self, V, adj):
        
        # Visited array
        vis = [False] * V
        
        # Path Visited array
        pathVis = [False] * V
        
        # To keep a check of safe nodes
        check = [False] * V
        
        # Traverse the graph and 
        # check for safe nodes
        for i in range(V):
            if not vis[i]:
                
                # Start DFS traversal
                self.dfsCheck(i, adj, vis, pathVis, check)
        
        # To store the result
        ans = []
        
        # Add the safe nodes to the result
        for i in range(V):
            if check[i]:
                ans.append(i)
        
        # Return the result
        return ans
if __name__ == "__main__":
  V = 7
  adj= [[1,2], [2,3], [5], [0], [5], [], []]
  print(Solution().eventualSafeNodes(V,adj))