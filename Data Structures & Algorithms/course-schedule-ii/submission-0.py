class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        current_path = set()
        checked = set() # before adding to checked, do sth to preverse the order
        c_to_prereqs = defaultdict(list)
        for n in range(numCourses):
            c_to_prereqs[n] = []
        for c, prereq in prerequisites:
            c_to_prereqs[c].append(prereq)
 
        def can_complete(c):
            if c in current_path:
                return False
            if c in checked:
                # res.append(c)
                return True
            current_path.add(c)
            for prer in c_to_prereqs[c]:
                if not can_complete(prer):
                    return False
            current_path.remove(c)
            res.append(c)
            checked.add(c)
            return True
        

        for c in range(numCourses):
            if not can_complete(c):
                return []
        return res

