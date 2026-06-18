# CPU Scheduling Simulator

A simple, interactive command-line simulator that demonstrates and compares classic CPU scheduling algorithms. The program runs First-Come-First-Served (FCFS), Shortest Job First (SJF), Priority Scheduling, and Round Robin (RR), and calculates key scheduling metrics such as Average Turnaround Time and Average Waiting Time for the set of processes.

## Features

- Implements common CPU scheduling algorithms: FCFS, SJF, Priority, and Round Robin.
- Computes Average Turnaround Time and Average Waiting Time for each algorithm.
- Accepts process definitions (arrival time, burst time, priority) and scheduling parameters (e.g., time quantum for Round Robin).
- Displays scheduling order and basic timeline information to help visualize how each algorithm behaves.

## What this program is for

This simulator is intended for students, educators, and anyone learning operating systems concepts. It provides a hands-on way to see how different CPU scheduling policies affect process order and performance metrics, and to compare trade-offs between fairness, throughput, and responsiveness.

## Input

Provide a list of processes. Each process should include at least:
- Process ID (or name)
- Arrival time
- Burst (CPU) time
- Priority (for Priority Scheduling)

The program may accept interactive prompt input or a simple text/CSV input depending on the command-line interface implementation.

## Output

For each chosen algorithm, the simulator prints:
- The order in which processes are scheduled.
- Turnaround time and waiting time for each process.
- Average Turnaround Time and Average Waiting Time across all processes.
- (Optional) A textual timeline/Gantt-like view to visualize scheduling.

## Example usage

Run the program with Python 3 and follow the prompts to enter processes and select an algorithm. If the repository exposes a script name (for example `simulator.py` or `main.py`), run it with:

python <script>.py

Then follow the on-screen instructions to enter processes and algorithm options (e.g., set the time quantum for Round Robin).

## Learning outcomes

- Understand how FCFS, SJF, Priority, and RR choose which process to run next.
- See how arrival times and priorities affect scheduling.
- Compare algorithms using Turnaround Time and Waiting Time metrics.

## Contributing

Contributions are welcome — open an issue or submit a pull request with bug fixes, new features (preemptive SJF, Gantt chart visualization, file-based input), or documentation improvements.

## License

Include a LICENSE file or add a short license note here if desired.
