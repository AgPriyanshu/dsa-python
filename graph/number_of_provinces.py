# Given an undirected graph with V vertices. Two vertices u and v belong to a single province if there is a path from u to v or v to u. Find the number of provinces. The graph is given as an n x n matrix adj where adj[i][j] = 1 if the ith city and the jth city are directly connected, and adj[i][j] = 0 otherwise.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

class Solution:
    def dfs(self,node,adjLs,visited):
      visited[node] = 1
      for n in adjLs[node]:
        if visited[n] == 0:
          self.dfs(n,adjLs,visited)

    def numProvinces(self, adj):
      V = len(adj)
      adj_list = [ [] for _ in range(V)]
      visited = [0] * V
      for i in range(V):
        for j in range(V):
          if i != j and adj[i][j] == 1:
            # print(adj_list[i][0])
            adj_list[i].append(j)
      count = 0
      for i in range(V):
        if not visited[i]:
          self.dfs(i,adj_list,visited)
          count += 1
      return count


if __name__ == "__main__":
  s = Solution()
  adj=[ [1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1] ]
  print(s.numProvinces(adj))