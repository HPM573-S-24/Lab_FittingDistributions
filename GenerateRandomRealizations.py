import numpy as np

import deampy.random_variates as rvgs

# a random number generator
rng = np.random.RandomState(seed=0)

# gamma
gamma = rvgs.Gamma(a=0.9835458832943496,
                   loc=0,
                   scale=1.9199027077975956)
# generate 10 realizations from gamma
print('Realizations from gamma:')
for i in range(10):
    print(gamma.sample(rng))

# gamma-Poisson
gammaPoisson = rvgs.GammaPoisson(a=0.3693765965041004,
                                 gamma_scale=9.154827879319111,
                                 loc=0)
# generate 10 realizations from gamma-Poisson
print('Realizations from gamma-Poisson:')
for i in range(10):
    print(gammaPoisson.sample(rng))
