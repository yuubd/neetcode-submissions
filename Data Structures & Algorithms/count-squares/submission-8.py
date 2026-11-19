class CountSquares:

    def __init__(self):
        self.points = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.points[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        r, c = point
        candidates = self.points.get(r, {})
        res = 0
        for c2, count in candidates.items(): # point2 (r c2)
            d = abs(c2-c)
            if d == 0:
                continue
            rUp = r+d # (rUP c) (rUP c2)
            rDown = r-d # (rDown c) (rDown c2)

            if self.points[rUp][c] and self.points[rUp][c2]: # point 3 and 4
                res += (self.points[r][c2] * self.points[rUp][c] * self.points[rUp][c2])
            if self.points[rDown][c] and self.points[rDown][c2]: # point 3 and 4
                res += (self.points[r][c2] * self.points[rDown][c] * self.points[rDown][c2])
        return res
        '''
        point = (2 1)
        cand = (2 2)
        d = 1
        rup rdown = 3, 1
        self.points[1][1] self.points[1][2]


        '''

        
