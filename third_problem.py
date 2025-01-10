import numpy as np

import queue


def run_multiple_simulations(lambda_a: float, lambda_s: float,
                             simulations: int, sim_time: int) -> (float, float):
    e_r_values = []
    e_x_values = []

    for _ in range(simulations):
        _, _, _, r, x, _ = queue.simulate(lambda_a, lambda_s, sim_time)
        e_r_values.append(r)
        e_x_values.append(x)

    return np.mean(e_r_values), np.mean(e_x_values)


if __name__ == "__main__":
    lambda_a_value = 1/20
    lambda_s_values = [1/15, 1/100, 1/5]

    simulations_count = 1_000
    simulation_time = 10_000

    for lambda_s_value in lambda_s_values:
        e_r, e_x = run_multiple_simulations(lambda_a_value, lambda_s_value,
                                            simulations_count, simulation_time)
        print(f"lambda_s = {lambda_s_value}, "
              f"E[R] = {e_r:.5f}, "
              f"E[x] = {e_x:.5f}, "
              f"Little's Law: {e_r:.2f} * {lambda_a_value:.2f} =  * {e_x:.2f} "
              f"(Expected: {lambda_a_value * e_r:.5f}, Got: {e_x:.5f})")
