class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False]*n
        def DFS(node,visited):
            visited[node]=True
            for nei in range(n):
                if isConnected[node][nei]==1 and not visited[nei]:
                    DFS(nei,visited)
        count=0
        for i in range(n):
            if not visited[i]:
                DFS(i,visited)
                count+=1
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna