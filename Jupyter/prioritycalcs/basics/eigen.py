import numpy as np

def harker_fix(mat):
    """
    Performs Harkers fix on the numpy matrix mat.  It returns a copy with the fix.
    The function does not change the matrix mat.
    :param mat:
    :return:
    """
    nrows = mat.shape[0]
    ncols = mat.shape[1]
    rval = mat.copy()
    for row in range(nrows):
        val = 1
        for col in range(ncols):
            if col != row and mat[row,col]==0:
                val+=1
        rval[row,row]=val
    return(rval)

def largest_eigen(mat, error = 1e-10, use_harker = False):
    if use_harker:
        mat = harker_fix(mat)
    size = mat.shape[0]
    vec = np.ones([size])
    diff = 1
    while diff > error:
        nextv = np.matmul(mat, vec)
        nextv = nextv/sum(nextv)
        diff = max(abs(nextv - vec))
        vec = nextv
    return(vec)