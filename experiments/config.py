LOW_PRIORITY = ['uncompilable', 'timeout']
MEDIUM_PROORITY = ['wrong']
HIGH_PRIORITY = ['plausible']

CLUSTER_NUM = 3
DISTANCE_THRES = 3

BUG_INFO = {
    'MATH_80': {
        'file_name': 'EigenDecompositionImpl.java',
        'bug_id': 'Math_80',
        'buggy_line': 'int j = 4 * n - 1;'
    }
}