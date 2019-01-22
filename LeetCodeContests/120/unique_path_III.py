class Solution:
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 3 reps passed 0
        m,n=len(grid[0]),len(grid)
        tot=m*n
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==-1:
                    tot-=1
                if grid[i][j]==1:
                    st=[i,j]
        ans=[0]
        def dfs(pos,step):
            if grid[pos[0]][pos[1]]==0:
                grid[pos[0]][pos[1]]=3
            for i,j in [[0,1],[0,-1],[1,0],[-1,0]]:
                if 0<=pos[0]+i<n and 0<=pos[1]+j<m:
                    if step+1==tot-1 and grid[pos[0]+i][pos[1]+j]==2:
                        ans[0]+=1
                        break
                    if grid[pos[0]+i][pos[1]+j]==0:
                        dfs([pos[0]+i,pos[1]+j],step+1)
            if grid[pos[0]][pos[1]]==3:
                grid[pos[0]][pos[1]]=0
        dfs(st,0)
        return ans[0]
            
                
            
            
