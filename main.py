
import numpy as np
import pdb

def running_stats(samples):
    '''
    Compute the running mean and variance
    '''
    sum_x = 0
    count = 0
    M = 0
    S = 0
    for n in range(0,len(samples)):
        x = samples[n]
        # running mean
        sum_x += x
        count += 1
        print('Running mean = ' + str(sum_x/count))
        # Welford's algorithm
        M_prev = M;
        M = M + (x - M)/(n+1);
        S = S + (x - M)*(x - M_prev);
        print('Running variance = ' + str(S/(len(samples)-1)))

    print('True mean = ' + str(np.mean(samples)))
    print('True variance = ' + str(np.var(samples)))


def calc_corr(t1,x1,t2,y2):
    '''
    Compute correlation between two time series (t1,x1) and (t2,y2) whose sampling
    rates may be different
    '''
    return 0


if __name__ == "__main__":

    data = np.random.rand(100) # randomly generated data

    running_stats(data)
