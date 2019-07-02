import numpy as np
cimport numpy as np

ctypedef np.int_t VAR_INTDTYPE_t
ctypedef np.float32_t VAR_FLOAT32DTYPE_t
ctypedef np.float64_t VAR_FLOAT64DTYPE_t
ctypedef np.uint8_t VAR_UINT8DTYPE_t

ctypedef np.float_t FLOATDTYPE_t

ctypedef fused variable_in_histogram_type:
    np.ndarray[VAR_FLOAT32DTYPE_t, ndim=1]
    np.ndarray[VAR_FLOAT64DTYPE_t, ndim=1]
    np.ndarray[VAR_UINT8DTYPE_t, ndim=1]
    np.ndarray[VAR_INTDTYPE_t, ndim=1]

cpdef  np.ndarray[FLOATDTYPE_t, ndim =1] get_weights_from_bins(variable_in_histogram_type variable_in_histogram, np.ndarray[FLOATDTYPE_t, ndim = 1] low_edges, np.ndarray[FLOATDTYPE_t, ndim=1] high_edges, np.ndarray[FLOATDTYPE_t, ndim = 1] normalization):
    cdef int maxbin = low_edges.shape[0]
    cdef int tracks = variable_in_histogram.shape[0]
    cdef int i, j
    cdef np.ndarray[FLOATDTYPE_t, ndim =1] weights = np.ones(tracks, dtype = np.float)

    for i in range(maxbin):
        for j in range(tracks):
            if (variable_in_histogram[j] >= low_edges[i]) and (variable_in_histogram[j] < high_edges[i]):
                weights[j] = normalization[i]
    return weights
