import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import poisson as analytic_poisson

import poisson


def collect_trajectories(lambda_param: float,
                         time: float, num_trajectories: [float]) -> [[(float, int)]]:
    trajectories = []

    for _ in range(num_trajectories):
        t, j = poisson.simulate_process(lambda_param, time)
        trajectories.append(list(zip(t, j)))

    return trajectories


def count_events_at_times(trajectories: [[(float, int)]],
                          times_to_check) -> {float: [int]}:
    counts_at_times = {t: [] for t in times_to_check}

    for trajectory in trajectories:
        for check_time in times_to_check:
            count = sum(1 for time, _ in trajectory if time <= check_time)
            counts_at_times[check_time].append(count)

    return counts_at_times


def plot_histogram_and_poisson(counts: {float: [int]},
                               lambda_param: float, t: float) -> None:
    plt.figure(figsize=(10, 6))

    plt.hist(counts, bins=range(min(counts), max(counts) + 2),
             density=True, alpha=0.6, color='blue', label='Empirical')

    poisson_mean = lambda_param * t
    x = np.arange(0, max(counts) + 1)
    poisson_probs = analytic_poisson.pmf(x, poisson_mean)

    plt.plot(x, poisson_probs, 'o-', color='red',
             label=f'Poisson (mean={poisson_mean:.1f})')

    plt.title(f'Distribution of events at t={t}')
    plt.xlabel('Number of events')
    plt.ylabel('Probability')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    test_lambda = 1
    check_times = [1, 20, 90]

    max_time = 10
    max_trajectory = 10_000

    times_result, jumps_result = poisson.simulate_process(test_lambda, max_time)
    poisson.plot(times_result, jumps_result, test_lambda, max_time)

    max_time = 100

    trajectories_arr = collect_trajectories(test_lambda, max_time, max_trajectory)
    events = count_events_at_times(trajectories_arr, check_times)

    for t_check in check_times:
        if t_check <= max_time:
            plot_histogram_and_poisson(events[t_check], test_lambda, t_check)
