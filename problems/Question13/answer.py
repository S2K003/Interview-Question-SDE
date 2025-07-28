class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Assume the 2d Matrix as 1d Matrix for binary Search

        #If the matrix is empty then return false
        if not matrix:
            return False
        
        # Variables to store number of rows and columns
        rows = len(matrix)
        cols = len(matrix[0])

        #Initializing left and right variable for Binary Search
        left = 0
        right = rows * cols - 1 # Last Element in the Matrix

        #Binary Search
        while left<=right:
            mid = (left+right) // 2
            mid_value = matrix[mid//cols][mid%cols]

            if mid_value == target:
                return True
            elif mid_value > target:
                right = mid-1
            else:
                left=mid+1
        
        return False