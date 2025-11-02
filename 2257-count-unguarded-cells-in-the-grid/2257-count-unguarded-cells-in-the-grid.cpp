class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        vector<vector<int>> grid(m, vector<int>(n, 0)); // 0: empty, 1: guard, 2: wall, 3: guarded

        // Mark guards and walls
        for (auto& g : guards) grid[g[0]][g[1]] = 1;
        for (auto& w : walls) grid[w[0]][w[1]] = 2;

        vector<pair<int,int>> dirs = {{0,1},{1,0},{0,-1},{-1,0}}; // right, down, left, up

        // For each guard, mark cells in all 4 directions as guarded
        for (auto& g : guards) {
            for (auto& d : dirs) {
                int x = g[0] + d.first, y = g[1] + d.second;
                while (x >= 0 && y >= 0 && x < m && y < n && grid[x][y] != 1 && grid[x][y] != 2) {
                    if (grid[x][y] == 0) grid[x][y] = 3; // mark as guarded
                    x += d.first;
                    y += d.second;
                }
            }
        }

        int ans = 0;
        // Count unguarded and unoccupied cells
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (grid[i][j] == 0)
                    ++ans;
        return ans;
    }
};