def findMatrixElement(matrix,target):
    if not matrix or not matrix[0]:
        return False
    row = len(matrix)
    col = len(matrix[0])

    left = 0
    right = (row*col)-1

print(findMatrixElement([[1,3,5,7],[10,11,16,20],[23,30,34,60]],1))
