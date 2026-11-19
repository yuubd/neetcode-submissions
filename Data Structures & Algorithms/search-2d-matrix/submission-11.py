class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        vertical bs and hotizontal bs

        First implement the first bs for an array

        get the mid of the len(matrix)
        check if target is the first of the list, return true if it is
        if target < mid, recurse on the upper part of the matrix
        else recurse on the upper part of the matrix

            run the 1D BS if the uppper_part mid array index + 1 == mid_array idx and upper_part_mid_array[0] < target < mid_array[0]
            or the uppper_part mid_array idx+1 == lower part matrix idx and upper_part_mid_array[0] < target < mid_array[0]

        return both with or
        '''
        def one_D_bs(idx):
            print("%% one_D_bs", "l", matrix[idx])
            l = matrix[idx]
            mid = int(len(l)/2)

            visited = set()
            start = 0
            end = len(l)-1
            while not mid in visited:
                print("start", start, "end", end, "mid", mid)
                visited.add(mid)
                if l[mid] == target:
                    return True
                if target < l[mid]:
                    end = mid
                else:
                    start = mid+1

                mid = int((start+end)/2)

            return False


        visited_rows = set()
        def searchMatrix_helper(start_idx, end_idx):
            print("@@ searchMatrix_helper")
            mid_idx = int((start_idx + end_idx) / 2)
            mid_row = matrix[mid_idx]
            print("mid_idx", mid_idx, "mid_row", mid_row)

            # the target is in the mid array
            if mid_row[0] <= target <= mid_row[-1]:
                return one_D_bs(mid_idx)
            
            visited_rows.add(mid_idx)
            print("visited_rows", visited_rows)

            if not mid_idx-1 in visited_rows and target < mid_row[0]:
                print("!! upper matrix", "start_idx", start_idx, "end_idx", mid_idx)
                return searchMatrix_helper(start_idx, mid_idx)
            elif not mid_idx+1 in visited_rows and mid_row[0] < target:
                print("!! lower matrix", "start_idx", mid_idx, "end_idx", end_idx)
                return searchMatrix_helper(mid_idx+1, end_idx)

            return False

        # target is out of the boundary
        if target < matrix[0][0] or matrix[len(matrix)-1][len(matrix[0])-1] < target :
            return False
        return searchMatrix_helper(0, len(matrix)-1)








