import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = np.array(matrix)
        flat = arr.flatten()
        l, r = 0,len(flat) -1 
        mid = (r+l)//2
        for i in flat: 
            if target == i: 
                return True
            if target < mid: 
                r = mid -1 
            else:
                l = mid + 1 
        return False
            
        