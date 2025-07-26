class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #Transpose the matrix by swapping elements of ij and ji 
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[i])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        #Reverse each row by Two Pointer Method 
        for i in range(len(matrix)):
            left = 0
            right = len(matrix[i]) - 1
            while left<right:
                matrix[i][left],matrix[i][right] = matrix[i][right],matrix[i][left]
                left+=1
                right-=1
        


        