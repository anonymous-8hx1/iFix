from experiment.CURE import *
from experiment.S3 import *
# from experiment.LLM import *
from experiment.SIMPLE_RANK import *
from experiment.RewardRepair import *
from experiment.KNOD import *

def main(test):
    if test == 'CURE':
        CURE_test()
    elif test == 'S3':
        S3_test()
    elif test == 'LLM':
        # LLM_test()
        return
    elif test == 'SIMPLE_RANK':
        SIMPLERANK_test()
    elif test == 'RewardRepair':
        RewardRepair_test()
    elif test == 'KNOD':
        KNOD_test()

if __name__ == '__main__':
    TEST = 'RewardRepair'
    main(TEST)