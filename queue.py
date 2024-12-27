import numpy as np
from matplotlib import pyplot as plt

import exponential


def exponential_generate(lambda_param: float) -> float:
    u = np.random.uniform(0, 1)
    return -np.log(1 - u) / lambda_param


def simulate(lambda_a: float, lambda_s: float,
             max_time: float) -> ([float], [int], [int], float, float, float):
    arrival_times = []
    current_time = 0
    total_system_time = 0
    num_tasks = 0

    while current_time < max_time:
        inter_arrival_time = exponential.generate(lambda_a)
        current_time += inter_arrival_time
        if current_time > max_time:
            break
        arrival_times.append(current_time)
        num_tasks += 1

    service_times = [exponential.generate(lambda_s) for _ in range(len(arrival_times))]

    current_service_end = 0
    queue = 0
    tasks_done = 0

    time_points = []
    queue_sizes_over_time = []
    tasks_done_over_time = []

    for arrival, service in zip(arrival_times, service_times):
        while time_points and time_points[0] <= arrival:
            current_service_end = time_points.pop(0)
            if queue > 0:
                queue -= 1
                tasks_done += 1

        if current_service_end < arrival:
            current_service_end = arrival + service
        else:
            queue += 1
            current_service_end += service

        time_points.append(current_service_end)

        queue_sizes_over_time.append(queue)
        tasks_done_over_time.append(tasks_done)

        total_system_time += current_service_end - arrival

    average_time_in_system = total_system_time / num_tasks
    average_number_in_system = total_system_time / max_time

    return (arrival_times, queue_sizes_over_time, tasks_done_over_time,
            average_time_in_system, average_number_in_system, num_tasks)


def plot(queue_sizes: [int], tasks_done: [int],
         lambda_a: float, lambda_s: float, max_time: float) -> None:
    time_points = np.arange(0, max_time, max_time / len(queue_sizes))

    plt.figure(figsize = (14, 6))

    plt.subplot(1, 2, 1)
    plt.plot(time_points, queue_sizes, label = f"λA={lambda_a}, λS={lambda_s}")
    plt.title("Number of tasks in the queue over time")
    plt.xlabel("Time")
    plt.ylabel("Number of tasks in the queue")
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(time_points, tasks_done, label = f"λA={lambda_a}, λS={lambda_s}")
    plt.title("Number of tasks completed over time")
    plt.xlabel("Time")
    plt.ylabel("Number of tasks completed")
    plt.yticks(np.arange(0, max(tasks_done) + 1, 1))
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
