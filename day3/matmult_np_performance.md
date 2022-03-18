orknaydn@ang-kemi1325:~/Documents/Lectures_UU/adv_python_course/exercises/day3$ kernprof -l -v matmult_np.py 
Wrote profile results to matmult_np.py.lprof
Timer unit: 1e-06 s

Total time: 0.012146 s
File: matmult_np.py
Function: matmult at line 12

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    12                                           @profile
    13                                           def matmult(X,Y):
    14         1      12145.0  12145.0    100.0      result = np.matmul(X,Y)
    15         1          1.0      1.0      0.0      return result

