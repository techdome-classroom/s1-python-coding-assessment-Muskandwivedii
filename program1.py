class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        # Check if the grid is empty
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        # Helper function to perform DFS
        def dfs(r, c):
            # Base case: if out of bounds or water, return
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 'W':
                return
            # Mark the current land cell as visited by converting it to water
            grid[r][c] = 'W'
            # Visit all neighboring cells (up, down, left, right)
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right

        # Initialize the island count
        island_count = 0

        # Traverse each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If we find a landmass ('L'), start a DFS to mark the entire island
                if grid[r][c] == 'L':
                    dfs(r, c)  # Perform DFS to mark all connected land
                    island_count += 1  # Increment the island count

        return island_count

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    dispatch_1 = [
        ["L", "L", "L", "L", "W"],
        ["L", "L", "W", "L", "W"],
        ["L", "L", "W", "W", "W"],
        ["W", "W", "W", "W", "W"],
    ]
    
    dispatch_2 = [
        ["L", "L", "W", "W", "W"],
        ["L", "L", "W", "W", "W"],
        ["W", "W", "L", "W", "W"],
        ["W", "W", "W", "L", "L"],
    ]

    print(solution.getTotalIsles(dispatch_1))  # Output: 1
    print(solution.getTotalIsles(dispatch_2))  # Output: 3
