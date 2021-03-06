import numpy as np


def get_request():

    num_bin = np.random.randint(2, 5)
    num_dim = 4

    num_points = num_bin ** num_dim

    v = np.random.normal(size=num_points, scale=10)
    x = np.random.normal(size=1, scale=10)

    # We want to integrate the case where the probabilities are generated by the discretized
    # normal distribution.
    # if np.random.choice([True, False]):
    #
    # else:
    #     mean = np.random.normal(size=num_dim)
    #     cov = wishart.rvs(num_dim, np.identity(num_dim))
    #     q = get_normal_probabilities(num_bin, mean, cov)[0].flatten()
    #
    #     # We need to remove all zero-probability events.
    #     is_nonzero = (q > EPS_FLOAT)
    #     q, v = q[is_nonzero], v[is_nonzero]

    q = np.random.uniform(low=0.01, size=num_points)

    q = q / np.sum(q)

    beta = np.random.uniform()
    gamma = np.random.uniform()
    is_cost = np.random.choice([True, False])

    return x, v, q, beta, gamma, is_cost
