import numpy as np
import matplotlib.pyplot as plt

import queue


def plot(x_axis: [float], y_axis: [float], title: str, x_label: str,
         y_label: str) -> None:
    plt.plot(x_axis, y_axis)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


if __name__ == "__main__":
    max_time = 1000

    # A) Plot - number of tasks in the system over λA
    lambda_a_values = np.linspace(0.01, 0.5, 1000)
    lambda_s = 0.15
    results = []

    for lambda_a in lambda_a_values:
        _, _, _, _, _, tasks_done = queue.simulate(lambda_a, lambda_s, max_time)
        results.append(tasks_done)

    plot(lambda_a_values, results,
         f"Number of tasks in the system over λA, λS = {lambda_s}",
         "λA", "Number of tasks in the system")

    # B) Plot - number of tasks in the system over λS

    lambda_s_values = np.linspace(0.01, 0.5, 1000)

    results = []
    lambda_a = 0.15

    for lambda_s in lambda_s_values:
        _, _, _, _, _, tasks_done = queue.simulate(lambda_a, lambda_s, max_time)
        results.append(tasks_done)

    plot(lambda_s_values, results,
         f"Number of tasks in the system over λS, λA = {lambda_a}",
         "λS", "Number of tasks in the system")

    # C) Plot - number of tasks in the system over ratio (r = λA / λS)

    r_values = np.linspace(0.1, 2, 100)

    results = []

    for r in r_values:
        lambda_s = 0.15
        lambda_a = r / lambda_s

        _, _, _, _, _, tasks_done = queue.simulate(lambda_a, lambda_s, max_time)
        results.append(tasks_done)

    plot(r_values, results,
         f"Number of tasks in the system over ratio (r = λA / λS), λS = {lambda_s}",
         "r", "Number of tasks in the system")
