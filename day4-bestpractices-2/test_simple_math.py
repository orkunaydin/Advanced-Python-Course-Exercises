from simple_math import *
import pytest

@pytest.mark.parametrize("i1,i2,a,s,m,d", [
    (3.0,2.0,5.0,1.0,6.0,1.5),
    (7.0,1.0,8.0,6.0,7.0,7.0)
])


def test_simple_math(i1,i2,a,s,m,d):
    assert simple_add(i1,i2) == a
    assert simple_sub(i1,i2) == s
    assert simple_mult(i1,i2) == m
    assert simple_div(i1,i2) == d
