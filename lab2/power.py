import numpy as np
import compare
def power(sample1, sample2, reps, size, alpha,K_iterations):
    count =0
    for i in range(reps):
        sampleA = np.random.choice(sample1, size)
        sampleB = np.random.choice(sample2, size)
        pVal = compare.abTest(sampleA,sampleB,K_iterations)
        if(pVal<1-alpha):
            count = count + 1
    return count/reps