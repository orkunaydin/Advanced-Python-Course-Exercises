orknaydn@ang-kemi1325:~/Documents/Lectures_UU/adv_python_course/exercises/day3$ kernprof -l -v matmult.py 
Wrote profile results to matmult.py.lprof
Timer unit: 1e-06 s

Total time: 10.5097 s
File: matmult.py
Function: matmult at line 21

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    21                                           @profile
    22                                           def matmult(X,Y):
    23       251         56.0      0.2      0.0      for i in range(len(X)):
    24                                                   # iterate through columns of Y
    25     63000      14689.0      0.2      0.1          for j in range(len(Y[0])):
    26                                                       # iterate through rows of Y
    27  15750250    3589451.0      0.2     34.2              for k in range(len(Y)):
    28  15687500    6905518.0      0.4     65.7                  result[i][j] += X[i][k] * Y[k][j]
    29         1          1.0      1.0      0.0      return result

