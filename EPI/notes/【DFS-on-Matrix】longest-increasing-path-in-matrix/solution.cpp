// [1] know what a normal DFS is when traversing in matrix;
// [2] know how to extend from a normal visited table(a dp table) to hold value for more complex usage. such as holding the maximum value seen so far.

// c++ version:
struct entry {
  int x;
  int y;
}

vector<vector<int>> dp_table = {{-1, -1, ...}, ...}; // record the max value reached till curr position.

int dfs(entry* curr, vector<vector<int>> dp_table) {
  if (dp_table[curr->x][curr->y]) return dp_table[curr->x][curr->y];
  for(int i = 0 ; i < directions.size(); i++) {
    int new_x = curr->x + directions[i].first;
    int new_y = curr->y + directions[i].second;
    max_len = -1;
    if (valid_position && A[new_x][new_y] > A[curr->x][curr->y]) {
      int length = 1 + dfs(new Entry(new_x, new_y), dp_table);
      max_len = max(max_len, length);
    }
  }
  dp_table[curr->x][curr->y] = max_len;
  return max_len;
}

// python version:
def dfs(self, i, j, matrix, visited, m, n):
  if visited[i][j]: 
    # return or return a value
  for dir in self.directions:
    x, y = i + direction[0], j + direction[1]
    if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j] (or a condition you want to skip this round):
      continue
    # do something like
    visited[i][j] = True
    # explore the next level like
    self.dfs(x, y, matrix, visited, m, n)