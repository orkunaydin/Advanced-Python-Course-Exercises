orknaydn@ang-kemi1325:~/Documents/Lectures_UU/adv_python_course/exercises/day4-bestpractices-2$ kernprof -l -v rbf.py 
Wrote profile results to rbf.py.lprof
Timer unit: 1e-06 s

Total time: 0 s
File: rbf.py
Function: rbf_network at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           @profile
     7                                           def rbf_network(X, beta, theta):
     8                                           
     9                                               N = X.shape[0]
    10                                               D = X.shape[1]
    11                                               Y = np.zeros(N)
    12                                           
    13                                               for i in range(N):
    14                                                   for j in range(N):
    15                                                       r = 0
    16                                                       for d in range(D):
    17                                                           r += (X[j, d] - X[i, d]) ** 2
    18                                                       r = r**0.5
    19                                                       Y[i] += beta[j] * exp(-(r * theta)**2)
    20                                           
    21                                               return Y

Total time: 0 s
File: rbf.py
Function: rbf_scipy at line 24

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    24                                           @profile
    25                                           def rbf_scipy(X, beta):
    26                                           
    27                                               N = X.shape[0]
    28                                               D = X.shape[1]
    29                                               rbf = Rbf(X[:,0], X[:,1], X[:,2], X[:,3], X[:, 4], beta)
    30                                               #Xtuple = tuple([X[:, i] for i in range(D)])
    31                                               Xtuple = tuple([X[:, i] for i in range(D)])
    32                                           
