import queue

if __name__ == '__main__':
    max_time = 1000

    scenarios = [
        (1/20, 1/15),
        (1/20, 1/100),
        (1/20, 1/5)
    ]

    for lambda_a, lambda_s in scenarios:
        arrival_times, queue_sizes, tasks_done = queue.simulate(lambda_a,
                                                                lambda_s,
                                                                max_time)

        queue.plot(queue_sizes, tasks_done, lambda_a, lambda_s, max_time)
