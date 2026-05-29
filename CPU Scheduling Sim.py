import customtkinter as ctk

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

add_btn = ctk.CTkButton(input_frame, text="Add Process")
add_btn.grid(row=0, column=8, padx=15, pady=5)

app.mainloop()