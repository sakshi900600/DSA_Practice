
# shortest job first - CPU scheduling algo
# 


def sjf_no_arrival(pids, bursts):
    """
    Non-preemptive SJF where all processes arrive at time 0.
    pids: list of process ids
    bursts: list of burst times (same order as pids)
    Returns: schedule (order), waiting_times dict, turnaround_times dict, avg_wait, avg_tat
    """
    procs = sorted(zip(pids, bursts), key=lambda x: x[1])  # sort by burst
    time = 0
    waiting = {}
    tat = {}
    schedule = []
    for pid, b in procs:
        waiting[pid] = time  # all arrived at 0, waiting = current time
        time += b
        tat[pid] = waiting[pid] + b
        schedule.append(pid)
    n = len(pids)
    avg_wait = sum(waiting.values()) / n
    avg_tat = sum(tat.values()) / n
    return schedule, waiting, tat, avg_wait, avg_tat


def sjf_with_arrival(processes):
    """
    Non-preemptive SJF with arrival times.
    processes: list of tuples (pid, arrival_time, burst_time)
    Returns: schedule (order), waiting_times dict, turnaround_times dict, avg_wait, avg_tat
    """
    procs = sorted(processes, key=lambda x: x[1])  # sort by arrival time
    time = 0
    waiting = {}
    tat = {}
    completed = set()
    schedule = []

    n = len(procs)
    # loop until all complete
    while len(completed) < n:
        # list of available (arrived and not completed)
        available = [p for p in procs if p[0] not in completed and p[1] <= time]
        if not available:
            # no process has arrived yet; advance time to next arrival
            next_arrival = min(p[1] for p in procs if p[0] not in completed)
            time = next_arrival
            available = [p for p in procs if p[0] not in completed and p[1] <= time]

        # pick shortest burst among available
        pid, arr, burst = min(available, key=lambda x: x[2])
        waiting[pid] = time - arr
        time += burst
        tat[pid] = time - arr
        completed.add(pid)
        schedule.append(pid)

    avg_wait = sum(waiting.values()) / n
    avg_tat = sum(tat.values()) / n
    return schedule, waiting, tat, avg_wait, avg_tat


# Example usage:
if __name__ == "__main__":
    # Without arrival times
    pids = ["P1", "P2", "P3", "P4"]
    bursts = [6, 2, 8, 3]
    sched, wait, tat, aw, at = sjf_no_arrival(pids, bursts)
    print("SJF (no arrival):")
    print("Order:", sched)
    print("Waiting times:", wait)
    print("Turnaround times:", tat)
    print(f"Avg waiting = {aw:.2f}, Avg TAT = {at:.2f}\n")

    # With arrival times
    procs = [("P1", 0, 6), ("P2", 2, 2), ("P3", 4, 1), ("P4", 5, 3)]
    sched2, wait2, tat2, aw2, at2 = sjf_with_arrival(procs)
    print("SJF (with arrival):")
    print("Order:", sched2)
    print("Waiting times:", wait2)
    print("Turnaround times:", tat2)
    print(f"Avg waiting = {aw2:.2f}, Avg TAT = {at2:.2f}")


# Output:
# SJF (no arrival):
# Order: ['P2', 'P4', 'P1', 'P3']
# Waiting times: {'P2': 0, 'P4': 2, 'P1': 5, 'P3': 11}
# Turnaround times: {'P2': 2, 'P4': 5, 'P1': 11, 'P3': 19}
# Avg waiting = 4.50, Avg TAT = 9.25

# SJF (with arrival):
# Order: ['P1', 'P3', 'P2', 'P4']
# Waiting times: {'P1': 0, 'P3': 2, 'P2': 5, 'P4': 4}
# Turnaround times: {'P1': 6, 'P3': 3, 'P2': 7, 'P4': 7}
# Avg waiting = 2.75, Avg TAT = 5.75