#Time_Complexity: O(mlogN)
#Space_Complexity: O(1)
#Approach: Binary Search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)     #m is the length of the matrix
        
        for i in range(m):  #Conitnue for the while matrix
            low = 0  #Initialze low to 0
            high = len(matrix[0])-1     #Initialize hight to last column -1
            
            while low<=high:    #Continue till low crosses high
                mid = low+(high-low)//2     #Integer over flow
                
                if target == matrix[i][mid]: #If matrix[i][mid] is equal to target then return True
                    return True    
                
                if target < matrix[i][mid]:  #If the target is less than matrix[i][mid] high = mid-1
                    high = mid-1
                else:   #Else low = mid+1
                    low = mid +1 
                               
        return False    #Return false if the targte is not found