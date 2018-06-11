#Function matVec multiplys a Matrix by a Vector given by the user.
def matVec(matrix,vector):
  '''
  the matrix i x j is mulitply by the vector j. 
  use a for loop for I then len( matrix) returns the length of the matrix. 
  set the value to zero in order to compute, next use the for loop for variable j in the range len(vector) in order to compute. the argument may be a sequence. 

  solve the mathematic equation given
        A x = b
  return each result to the given data list result.

  input the test results and print the given output.

  '''

  result = [] # blank data list 
  for i in range(len(matrix)):
    total = 0 # set a value in order to compute 
    for j in range(len(vector)):
      total = total + (matrix[i][j] * vector[j]) # here is the actual function purpose
    result.append(total) # return 
  return result
  
  
 # for x in vector:
#    b.append(matrix*x)
# Test input
vector = [1,2,3]
matrix = [[1,2,3],[4,5,6],[7,8,9]]

#this is to ask the user to input the desire Vector and Matrix
#vector = input ('Enter a Vector ex:[1,2,3] : ')
#matrix = input ('Enter a Matrix ex:[[1,2,3],[4,5,6],[7,8,9]] : ')

#test input 2
vector2 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [1,2,3]

#test input 3
vector3 = 3
matrix3 = 'test'

# print anwser 
print(matVec(matrix,vector))

#print test anwser
print(matVec(matrix2,vector2))
print(matVec(matrix3,vector3))