"""Task6"""

import numpy as np


def getdimension(a):
    """Function. Returns dimensions of array a."""
    return len(a.shape)


def getdiagonal(a):
    """Function. Returns diagonal of square matrix."""
    print(type(np.diagonal(a)))
    return np.diagonal(a)


if __name__ == "__main__":
    print(sum((np.array([1, 2, 3]) == np.array([1,2,3])))
    assert np.getdimension(np.array([1, 2, 3])) == 1
    assert getdimension(np.array([[1], [2], [3]])) == 2
    assert getdimension(np.array([[[[1]]]])) == 4
    print("getdimension - OK")

    assert getdiagonal(np.array([[1]])) == np.array([1])
    assert getdiagonal(np.array([[1, 2], [3, 4]])) == np.array([1, 4])
    print("getdiagonal - OK")
