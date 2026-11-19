class CountSquares:

    def __init__(self):
        self.points = {} # {r: {c: count}}

    def add(self, point: List[int]) -> None:
        if point[0] not in self.points:
            self.points[point[0]] = {}
        if point[1] not in self.points[point[0]]:
            self.points[point[0]][point[1]] = 0
        self.points[point[0]][point[1]] += 1
        # print('self.points', self.points)

    def count(self, point: List[int]) -> int:
        r, c = point
        candidates = self.points[r] if r in self.points else {}
        # print('point', r, c, candidates)
        res = 0
        for c2, count in candidates.items(): # point2 (r c2)
            d = abs(c2-c)
            if d == 0:
                continue
            rUp = r+d # (rUP c) (rUP c2)
            rDown = r-d # (rDown c) (rDown c2)
            if rUp in self.points and c in self.points[rUp] and \
                rUp in self.points and c2 in self.points[rUp]: # point 3 and 4
                res += (self.points[r][c2] * self.points[rUp][c] * self.points[rUp][c2])
                # print("UPUP", (self.points[r][c2] * self.points[rUp][c] * self.points[rUp][c2]))
            if rDown in self.points and c in self.points[rDown] and \
                rDown in self.points and c2 in self.points[rDown]: # point 3 and 4
                res += (self.points[r][c2] * self.points[rDown][c] * self.points[rDown][c2])
                #print("DOWNDOWN", (self.points[r][c2] * self.points[rDown][c] * self.points[rDown][c2]))
        return res
        '''
        point = (2 1)
        cand = (2 2)
        d = 1
        rup rdown = 3, 1
        self.points[1][1] self.points[1][2]


        '''

        
