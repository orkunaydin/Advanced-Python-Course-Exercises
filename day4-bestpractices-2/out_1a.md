In [23]: import primes                                                                                 

In [24]: import cy_primes                                                                              

In [25]: %timeit primes.primes(2000)                                                                   
216 ms ± 1.09 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [26]: %timeit cy_primes.primes(2000)                                                                
1.37 ms ± 5.35 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
