# TC - O(m*n)
#SC - O(1)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        result = []

        while top<=bottom:

            for i in range(left,right+1):
                result.append(matrix[left][i])
            top+=1

            if left<=right:
                for i in range(top,bottom+1):
                    result.append(matrix[i][right])
                right-=1

            if  top<=bottom:
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])
                bottom-=1
                
            if left<=right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left+=1  

        return result              


        
