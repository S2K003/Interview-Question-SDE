#Interview Method
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)  # Start with 1s

            for j in range(1, i):  # Fill the middle values
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle

#Mathematical Method
class Solution(object):
    #Generating Each Row By Formula
    def generateRow(self, row):
        ans = 1
        ansRow = [1]

        for col in range(1, row + 1):  
            ans *= (row - col + 1)
            ans //= col
            ansRow.append(ans)

        return ansRow

    def generate(self, numRows):
        res = []
        #Adding each row by iteration of row numbers
        for row in range(numRows):
            res.append(self.generateRow(row))
        return res
