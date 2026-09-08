# Analyze waiting time, turnaround time, and Gantt chart generation

import random


# Class used to store information about each process
class Process:

    # Constructor: runs automatically when a Process object is created
    def __init__(self, pid, burst_time, arrival_time=0, priority=0):

        # Store Process ID
        self.pid = pid

        # Store the time required by the process to complete
        self.burst_time = burst_time

        # Store the time at which the process arrives
        self.arrival_time = arrival_time

        # Store the priority of the process
        self.priority = priority

        # These values will be calculated later
        self.start_time = None
        self.completion_time = None
        self.waiting_time = None
        self.turnaround_time = None


# First Come First Serve (FCFS) scheduler
def fcfs_scheduler(processes):

    # Arrange processes according to their arrival time
    return sorted(processes, key=lambda p: p.arrival_time)


# Shortest Job First (SJF) scheduler
def sjf_scheduler(processes):

    # Arrange processes according to their burst time
    return sorted(processes, key=lambda p: p.burst_time)


# Priority scheduler
def priority_scheduler(processes):

    # Arrange processes according to their priority
    return sorted(processes, key=lambda p: p.priority)


# Simulate a non-preemptive scheduling algorithm
def simulate_non_preemptive(processes):

    # Current CPU time starts from 0
    current_time = 0

    # List used to store Gantt chart information
    gantt_chart = []

    # Process each process one by one
    for process in processes:

        # If the process has not arrived yet,
        # CPU waits until the process arrives
        if current_time < process.arrival_time:
            current_time = process.arrival_time

        # Store the time when the process starts execution
        process.start_time = current_time

        # Calculate the completion time
        process.completion_time = current_time + process.burst_time

        # Waiting time = Start Time - Arrival Time
        process.waiting_time = process.start_time - process.arrival_time

        # Turnaround time = Completion Time - Arrival Time
        process.turnaround_time = (
            process.completion_time - process.arrival_time
        )

        # Add process information to the Gantt chart
        gantt_chart.append(
            (process.pid, process.start_time, process.completion_time)
        )

        # Move current CPU time to the completion time
        current_time = process.completion_time

    # Return the completed Gantt chart
    return gantt_chart


# Main program
if __name__ == "__main__":

    # Create 5 processes with random values
    processes = [
        Process(
            i,
            burst_time=random.uniform(1, 4),
            arrival_time=random.uniform(0, 5),
            priority=random.randint(1, 5)
        )
        for i in range(5)
    ]

    # Display process information
    print("Processes:")

    # Print information about every process
    for p in processes:
        print(
            f"P{p.pid}: "
            f"arrival={p.arrival_time:.2f}, "
            f"burst={p.burst_time:.2f}, "
            f"priority={p.priority}"
        )

    # Schedule processes using FCFS
    scheduled = fcfs_scheduler(processes)

    # Simulate the scheduled processes
    gantt_chart = simulate_non_preemptive(scheduled)

    # Display Gantt chart
    print("\nGantt Chart:")

    # Print each process with its start and end time
    for pid, start, end in gantt_chart:
        print(f"| P{pid} ({start:.1f}-{end:.1f}) ", end="")

    # Print final separator
    print("|")

    # Display process details
    print("\nProcess Details:")

    # Variables used to calculate total waiting and turnaround time
    total_wt = 0
    total_tat = 0

    # Display calculated values for each process
    for p in scheduled:

        # Add waiting time to total waiting time
        total_wt += p.waiting_time

        # Add turnaround time to total turnaround time
        total_tat += p.turnaround_time

        # Print waiting time and turnaround time
        print(
            f"P{p.pid}: "
            f"WT={p.waiting_time:.2f}, "
            f"TAT={p.turnaround_time:.2f}"
        )

    # Calculate and display average waiting time
    print(
        f"\nAverage Waiting Time: "
        f"{total_wt / len(processes):.2f}"
    )

    # Calculate and display average turnaround time
    print(
        f"Average Turnaround Time: "
        f"{total_tat / len(processes):.2f}"
    )
