# Given a undirected Graph consisting of V vertices numbered from 0 to V-1 and E edges. The ith edge is represented by [ai,bi], denoting a edge between vertex ai and bi. We say two vertices u and v belong to a same component if there is a path from u to v or v to u. Find the number of connected components in the graph.
# A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

class Solution:
    def dfs(self,node,adjLs,visited):
      visited[node] = 1
      for n in adjLs[node]:
        if visited[n] == 0:
          self.dfs(n,adjLs,visited)

    def findNumberOfComponent(self, V, edges):
        visited = [0] * V
        count = 0
        E = len(edges)
        adjLs = [[] for _ in range(V)]
        
        # Add edges to adjacency list
        for i in range(E):
            adjLs[edges[i][0]].append(edges[i][1])
            adjLs[edges[i][1]].append(edges[i][0])
        for node in range(V):
          if not visited[node]:
            self.dfs(node,adjLs,visited)
            count += 1
        return count

       
if __name__ == "__main__":
  s = Solution()
  V = 4
  edges = [[0,1],[1,2]]
  print(s.findNumberOfComponent(V,edges))