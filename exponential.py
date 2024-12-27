import numpy as np


def generate(lambda_param: float) -> [float]:
    u = np.random.uniform(0, 1)
    return -np.log(1 - u) / lambda_param
