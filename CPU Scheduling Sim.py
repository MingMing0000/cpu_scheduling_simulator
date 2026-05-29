import customtkinter as ctk
import tkinter as tk 
from tkinter import ttk, messagebox
import CTkTable
from CTkTable import *

app = ctk.CTk()
app.title("CPU Scheduling Simulator")
app.geometry("850x700")

label =ctk.CTkLabel(app, text="Process Input")
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

add_btn = ctk.CTkButton(input_frame, text="Add Process", command='')
add_btn.grid(row=0, column=8, padx=15, pady=5)

control_frame = ctk.CTkFrame(app,)
control_frame.pack(fill="x", padx=10, pady=10)

ctk.CTkLabel(control_frame, text="Algorithm:").grid(row=0, column=0, padx=5, pady=5)
algo_var = ctk.StringVar(value="FCFS")
algorithms = ["FCFS", "Round Robin"]
algo_dropdown = ctk.CTkComboBox(control_frame, variable=algo_var, values=algorithms, state="readonly", width=200)
algo_dropdown.grid(row=0, column=1, padx=5, pady=5)

ctk.CTkLabel(control_frame, text="Time Quantum (for RR):").grid(row=0, column=2, padx=(20, 5))
quantum_entry = ctk.CTkEntry(control_frame, width=30)
quantum_entry.grid(row=0, column=3, padx=5, pady=5)
quantum_entry.insert(0, "2")

run_btn = ctk.CTkButton(control_frame, text="Run Simulation", command='')
run_btn.grid(row=0, column=4, padx=10, pady=5)

clear_btn = ctk.CTkButton(control_frame, text="Clear All", command='')
clear_btn.grid(row=0, column=5, pady=5)

table_frame = ctk.CTkFrame(app)
table_frame.pack(fill="both", expand=True, padx=10, pady=10)

table_headers = ["Name", "Arrival Time", "Burst Time", "Priority"]

table = CTkTable(master=table_frame, row=6, values=[table_headers], colors=["#1C1A1A", "#0E0D0D"], header_color="#1E1A1A", text_color="white")
table.pack(fill="both", expand=True)

app.mainloop()