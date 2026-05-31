import customtkinter as ctk
import tkinter as tk 
from tkinter import ttk, messagebox
import CTkTable
from CTkTable import *
from CTkMessagebox import CTkMessagebox
from scheduling_algorithms import SchedulingAlgorithms

processes = []

def add_process():
        name = name_input.get()
        at = arrival_input.get()
        bt = burst_input.get()
        pr = priority_input.get() or "0"

        if not (name and at and bt):
            CTkMessagebox(title="Input Error", message="Please fill in all required fields (Name, Arrival Time, Burst Time).", icon="cancel")
            return

        try:
            at = int(at)
            bt = int(bt)
            pr = int(pr)
        except ValueError:
            CTkMessagebox(title="Input Error", message="Arrival Time, Burst Time, and Priority must be integers.", icon="cancel")
            return

        processes.append({"name": name, "at": at, "bt": bt, "pr": pr, "rem_bt": bt})
        
        table.add_row([name, at, bt, pr])

        name_input.delete(0, ctk.END)
        arrival_input.delete(0, ctk.END)
        burst_input.delete(0, ctk.END)
        priority_input.delete(0, ctk.END)

def clear_all():
        processes.clear()
        table.update_values([table_headers])
        canvas.delete("all")
        computations.set("Avg Turnaround Time: 0.00 ms   |   Avg Waiting Time: 0.00 ms")

def run_simulation():
    if not processes:
        messagebox.showwarning("Warning", "No processes to simulate.")
        return

    algo = algo_var.get()
    
    for p in processes:
        p['rem_bt'] = p['bt']

    if algo == "FCFS":
        schedule, avg_tat, avg_wt = SchedulingAlgorithms.simulate_fcfs(processes)
    elif algo == "Round Robin":
        try:
            tq = int(quantum_entry.get())
            if tq <= 0: raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Time Quantum must be a positive integer.")
            return
        schedule, avg_tat, avg_wt = SchedulingAlgorithms.simulate_rr(processes, tq)

    computations.set(f"Avg Turnaround Time: {avg_tat:.2f} ms   |   Avg Waiting Time: {avg_wt:.2f} ms")
    #draw_gantt_chart(schedule)

app = ctk.CTk()
app.title("CPU Scheduling Simulator")
app.geometry("805x700")

label =ctk.CTkLabel(app, text="Process Input", font=ctk.CTkFont(size=16, weight="bold"))
label.pack(pady=10)

input_frame = ctk.CTkFrame(app)
input_frame.pack(fill="x", padx=10, pady=5)

ctk.CTkLabel(input_frame, text="Process Name:").grid(row=0, column=0, padx=5, pady=5)
name_input = ctk.CTkEntry(input_frame, width=70)
name_input.grid(row=0, column=1, padx=5, pady=5)

ctk.CTkLabel(input_frame, text="Arrival Time:").grid(row=0, column=2, padx=5, pady=5)
arrival_input = ctk.CTkEntry(input_frame, width=70)
arrival_input.grid(row=0, column=3, padx=5, pady=5)

ctk.CTkLabel(input_frame, text="Burst Time:").grid(row=0, column=4, padx=5, pady=5)
burst_input = ctk.CTkEntry(input_frame, width=70)
burst_input.grid(row=0, column=5, padx=5, pady=5)

ctk.CTkLabel(input_frame, text="Priority:").grid(row=0, column=6, padx=5, pady=5)
priority_input = ctk.CTkEntry(input_frame, width=70)
priority_input.grid(row=0, column=7, padx=5, pady=5)

add_btn = ctk.CTkButton(input_frame, text="Add Process", command=add_process)
add_btn.grid(row=0, column=8, padx=15, pady=5)

control_frame = ctk.CTkFrame(app)
control_frame.pack(fill="x", padx=10, pady=10)

ctk.CTkLabel(control_frame, text="Algorithm:").grid(row=0, column=0, padx=5, pady=5)
algo_var = ctk.StringVar(value="FCFS")
algorithms = ["FCFS", "Round Robin"]
algo_dropdown = ctk.CTkComboBox(control_frame, variable=algo_var, values=algorithms, state="readonly", width=190)
algo_dropdown.grid(row=0, column=1, padx=5, pady=5)

ctk.CTkLabel(control_frame, text="Time Quantum (for RR):").grid(row=0, column=2, padx=(20, 5))
quantum_entry = ctk.CTkEntry(control_frame, width=40)
quantum_entry.grid(row=0, column=3, padx=5, pady=5)
quantum_entry.insert(0, "2")

run_btn = ctk.CTkButton(control_frame, text="Run Simulation", command=run_simulation, fg_color="#2FA572")
run_btn.grid(row=0, column=4, padx=10, pady=5)

clear_btn = ctk.CTkButton(control_frame, text="Clear All", command=clear_all, fg_color="#E85D04")
clear_btn.grid(row=0, column=5, pady=5)

table_headers = ["Name", "Arrival Time", "Burst Time", "Priority"]

table = CTkTable(app, values=[table_headers], colors=["gray14", "gray16"], header_color="gray20", text_color="white")
table.pack(fill="both", expand=True, padx=20, pady=10)

computations = ctk.StringVar(value="Avg Turnaround Time: 0.00 ms   |   Avg Waiting Time: 0.00 ms")
ctk.CTkLabel(app, textvariable=computations, font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

gantt_frame = ctk.CTkFrame(app)
gantt_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
ctk.CTkLabel(gantt_frame, text="Gantt Chart", font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="w", padx=10, pady=10)
            
canvas = tk.Canvas(gantt_frame, bg="#2b2b2b", highlightthickness=0, height=100)
canvas.pack(fill="both", expand=True, padx=10, pady=(0, 10))

app.mainloop()