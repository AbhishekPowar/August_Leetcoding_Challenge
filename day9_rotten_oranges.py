class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rotten = set()
        Rotten = 2
        Fresh = 1

        rows = len(grid)
        cols = len(grid[0])

        for x in range(rows):
            for y in range(cols):
                orange = grid[x][y]
                if orange is Rotten:
                    rotten.add((x, y))
                elif orange is Fresh:
                    fresh.add((x, y))

        freshCount = len(fresh)
        newRotten = set()

        delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        days = 0

        while fresh:
            for x, y in rotten:
                for dx, dy in delta:
                    newX, newY = x+dx, y+dy
                    if 0 <= newX < rows and 0 <= newY < cols:
                        if (newX, newY) in fresh:
                            fresh.remove((newX, newY))
                            newRotten.add((newX, newY))
            rotten = newRotten.copy()
            newRotten.clear()
            if len(fresh) == freshCount:
                return -1
            else:
                freshCount = len(fresh)
            days += 1
        return days
