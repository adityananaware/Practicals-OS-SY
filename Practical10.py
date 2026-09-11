# Implement Round Robin Scheduling with configurable Time Quantum

import random
from collections import deque


# Class used to store information about each process
class Process:

    # Constructor of the Process class
    def __init__(self, pid, burst_time, arrival_time=0):

        self.pid = pid
        self.burst_time = burst_time
        self.arrival_time = arrival_time

        # Initially, remaining time is equal to burst time
        self.remaining_time = burst_time

        # These values will be calculated during execution
        self.completion_time = None
        self.waiting_time = 0
        self.turnaround_time = 0

        # Initially, process has not been executed
        self.last_execution_time = arrival_time


# Function to implement Round Robin Scheduling
def round_robin(processes, time_quantum):

    # Current CPU time
    time = 0

    # Queue containing processes that are ready to execute
    ready_queue = deque()

    # List used to store Gantt Chart information
    gantt_chart = []

    # Sort processes according to their arrival time
    processes.sort(key=lambda p: p.arrival_time)

    # Make a copy of the process list
    processes_left = processes.copy()


    # Continue until all processes are completed
    # and the ready queue becomes empty
    while processes_left or ready_queue:

        # Check which processes have arrived
        for p in processes_left[:]:

            if p.arrival_time <= time:

                # Add arrived process to the ready queue
                ready_queue.append(p)

                # Remove it from the waiting list
                processes_left.remove(p)


        # If no process is ready, move the CPU time forward
        if not ready_queue:

            time += 0.1
            continue


        # Take the first process from the ready queue
        current = ready_queue.popleft()

        # Store the starting time of this process
        start_time = time

        # Execute the process for one time quantum
        # or until the process finishes
        exec_time = min(current.remaining_time, time_quantum)

        # Increase the current time
        time += exec_time

        # Decrease the remaining execution time
        current.remaining_time -= exec_time


        # Add process execution information to Gantt Chart
        gantt_chart.append((current.pid, start_time, time))


        # Calculate waiting time
        current.waiting_time += start_time - current.last_execution_time

        # Update the last execution time
        current.last_execution_time = time


        # If process still has remaining time,
        # put it back into the ready queue
        if current.remaining_time > 0:

            ready_queue.append(current)

        else:

            # Process has completed
            current.completion_time = time

            # Calculate Turnaround Time
            current.turnaround_time = (
                current.completion_time - current.arrival_time
            )


    # Return the Gantt Chart and completed processes
    return gantt_chart, processes


# Main program
if __name__ == "__main__":

    # Number of processes
    num_processes = 5

    # Time Quantum for Round Robin
    time_quantum = 1.0


    # Create 5 processes with random burst time
    # and random arrival time
    processes = [
        Process(
            i,
            burst_time=random.uniform(1, 5),
            arrival_time=random.uniform(0, 3)
        )
        for i in range(num_processes)
    ]


    # Display process information
    print("Processes:")

    for p in processes:

        print(
            f"P{p.pid}: "
            f"arrival={p.arrival_time:.2f}, "
            f"burst={p.burst_time:.2f}"
        )


    # Run Round Robin Scheduling
    gantt_chart, finished_processes = round_robin(
        processes,
        time_quantum
    )


    # Display Gantt Chart
    print("\nGantt Chart:")

    for pid, start, end in gantt_chart:

        print(
            f"| P{pid} ({start:.1f}-{end:.1f}) ",
            end=""
        )

    print("|")


    # Variables used to calculate average times
    total_wt = 0
    total_tat = 0


    # Display details of each process
    print("\nProcess Details:")

    for p in finished_processes:

        # Add waiting time to total waiting time
        total_wt += p.waiting_time

        # Add turnaround time to total turnaround time
        total_tat += p.turnaround_time

        print(
            f"P{p.pid}: "
            f"WT={p.waiting_time:.2f}, "
            f"TAT={p.turnaround_time:.2f}"
        )


    # Calculate and display average waiting time
    print(
        f"\nAverage Waiting Time: "
        f"{total_wt / num_processes:.2f}"
    )

    # Calculate and display average turnaround time
    print(
        f"Average Turnaround Time: "
        f"{total_tat / num_processes:.2f}"
    )
