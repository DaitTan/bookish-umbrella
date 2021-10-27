import numpy as np
from partx.run_part_x_macro_replication import run_part_x

def test_function(X):  ##CHANGE
    # return (X[0]**2 + X[1] - 11)**2 + (X[1]**2 + X[0] - 7)**2 - 40 # Himmelblau's
    return (100 * (X[1] - X[0] **2)**2 + ((1 - X[0])**2)) - 20 # Rosenbrock
    # return (1 + (X[0] + X[1] + 1) ** 2 * (
    #             19 - 14 * X[0] + 3 * X[0] ** 2 - 14 * X[1] + 6 * X[0] * X[1] + 3 * X[1] ** 2)) * (
    #                    30 + (2 * X[0] - 3 * X[1]) ** 2 * (
    #                        18 - 32 * X[0] + 12 * X[0] ** 2 + 48 * X[1] - 36 * X[0] * X[1] + 27 * X[1] ** 2)) - 50


# Options initialization

# Test function properties
test_function_dimension = 2
region_support = np.array([[[-1., 1.], [-1., 1.]]])

# Budgets
initialization_budget = 10
max_budget = 5000
continued_sampling_budget = 100

# BO grid size : number_of_BO_samples * number_of_samples_gen_GP
number_of_BO_samples = [10]
# R = number_of_BO_samples[0]
# M = number_of_samples_gen_GP
R = 10
M = 100
NGP = R*M

# Mostly not changes. change with caution
branching_factor = 2
nugget_mean = 0
nugget_std_dev = 0.001
alpha = [0.05]
delta = 0.001

# Other Parameters
number_of_macro_replications = 50
start_seed = 1000
fv_quantiles_for_gp = [0.5,0.95,0.99]


points_for_unif_sampling = 10000

BENCHMARK_NAME = "Rosenbrock_1"

run_part_x(BENCHMARK_NAME, test_function, test_function_dimension, region_support,
                initialization_budget, max_budget, number_of_BO_samples, continued_sampling_budget, R, M,
                branching_factor, nugget_mean, nugget_std_dev, alpha, delta, 
                number_of_macro_replications, start_seed, fv_quantiles_for_gp, NGP, points_for_unif_sampling)
                