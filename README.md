# CPU Scheduling Simulator

A simple, GUI-based simulator built with Tkinter that demonstrates and compares classic CPU scheduling algorithms. The program provides an interactive window where users can add processes and choose scheduling algorithms to visualize how each policy behaves.

## Features

- Implements common CPU scheduling algorithms: FCFS, SJF, Priority, and Round Robin.
- Computes Average Turnaround Time and Average Waiting Time for each algorithm.
- Accepts process definitions (arrival time, burst time, priority) and scheduling parameters (e.g., time quantum for Round Robin) via a Tkinter form.
- Displays scheduling order and a basic timeline/Gantt-like view to help visualize how each algorithm behaves.

## What this program is for

This simulator is intended for students, educators, and anyone learning operating systems concepts. It provides a hands-on GUI that makes it easy to add and modify processes, run different scheduling algorithms, and compare results visually.

## Input

Use the Tkinter GUI to add processes. Each process should include at least:
- Process ID (or name)
- Arrival time
- Burst (CPU) time
- Priority (for Priority Scheduling)

The GUI provides fields to enter these values and buttons to add, edit, or remove processes. For Round Robin, set the time quantum using the provided input. (If the project later adds a file/CSV import option, this section can be expanded.)

## Output

When you run a chosen algorithm from the GUI, the simulator shows:
- The order in which processes are scheduled.
- Turnaround time and waiting time for each process.
- Average Turnaround Time and Average Waiting Time across all processes.
- A textual or simple graphical timeline/Gantt-like view to visualize scheduling.

## Example usage

Run the program with Python 3. If the repository exposes a script (for example `simulator.py` or `main.py`), launch it with:

python <script>.py

The Tkinter window will open. Use the on-screen form to add processes, choose an algorithm, and run the simulation. Adjust parameters (like time quantum) through the GUI controls.

## Learning outcomes

- Understand how FCFS, SJF, Priority, and RR choose which process to run next.
- See how arrival times and priorities affect scheduling.
- Compare algorithms using Turnaround Time and Waiting Time metrics.

## Contributing

Contributions are welcome — open an issue or submit a pull request with bug fixes, new features (preemptive SJF, improved Gantt chart visualization, file-based input), or documentation improvements.

## License

Include a LICENSE file or add a short license note here if desired.
