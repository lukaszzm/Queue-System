import matplotlib.pyplot as plt

import exponential


def simulate_process(lambda_param: float, max_time: float) -> (float, int):
    times = []
    jumps = []

    current_time: float = 0
    current_jump: int = 0

    while current_time < max_time:
        inter_arrival_time = exponential.generate(lambda_param)
        current_time += inter_arrival_time

        if current_time > max_time:
            break

        times.append(current_time)

        current_jump += 1
        jumps.append(current_jump)

    return times, jumps


def plot(times: [float], jumps: [int], lambda_param: float, max_time: float):
    plt.step(times, jumps, where='post')
    plt.title(f'Poisson Process with rate {lambda_param} up to time {max_time}')
    plt.xlabel('Time')
    plt.ylabel('Number of Jumps')
    plt.show()
