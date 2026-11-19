class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = defaultdict(list)
        current_course_path = set()
        no_cycle_courses = set()
        
        for n in range(numCourses):
            course_map[n] = []
        for course, prer in prerequisites:
            course_map[course].append(prer)
        
        def detect_cycle(c):
            if c in current_course_path:
                return True
            if c in no_cycle_courses:
                return False 
            prerequisites = course_map[c]

            if len(prerequisites) == 0:
                return False # no cycle
            current_course_path.add(c)

            for prerequisite in prerequisites:
                if detect_cycle(prerequisite) == True: # cycle
                    return True
            current_course_path.remove(c)
            no_cycle_courses.add(c)
            return False
        for course in range(numCourses):
            if detect_cycle(course) == True:
                return False 
        return True

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = defaultdict(list)
        # current course path is used as a visited to see how to take before complete a course.
        current_course_path = set()
        no_cycle_courses = set()
        
        # we need to create a map of course to prereqs
        # cuz we want to see for each course, if any course has a cycle
        for n in range(numCourses):
            course_map[n] = []
        for course, prer in prerequisites:
            course_map[course].append(prer)
        
        # this is dfs
        def detect_cycle(c):
            # if a course is alreayd in the path, it means there is a cycle
            # to take c course for c course
            if c in current_course_path:
                return True # yes cycle
            if c in no_cycle_courses:
                return False # we have visited fully and confirmed no cycle 
            prerequisites = course_map[c]
            # no prer for c course
            if len(prerequisites) == 0:
                return False # no cycle
            current_course_path.add(c)

            # For each prer, check if any of them has a cycle
            for prerequisite in prerequisites:
                if detect_cycle(prerequisite) == True: # cycle
                    return True
            # when reaching a dead end, where the chain is finished, we confirmed no cycle deteced. Remove c course and try a diffferent path
            current_course_path.remove(c)
            # completed going over on all prers, no cycle for c course
            no_cycle_courses.add(c)
            
            return False

        # check if a cycle exists for a course and if so, return false
        # otherwise return True
        for course in range(numCourses):
            if detect_cycle(course) == True: # there is a cycle
                return False # cant complete
        return True
            
        