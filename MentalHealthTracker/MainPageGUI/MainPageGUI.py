import tkinter as tk
from tkinter import ttk

def on_resize(event):
    # Update the size of the root window when resized
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=2)
    root.grid_rowconfigure(2, weight=2)
    root.grid_rowconfigure(3, weight=2)


    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)
    root.grid_columnconfigure(2, weight=1)
    

def exit_program(event=None):
    root.destroy()

root = tk.Tk()
root.title("Main Window")

# Set the window attributes to fullscreen
root.attributes("-fullscreen", True)

# Bind the resize event to the on_resize function
root.bind("<Configure>", on_resize)

# Bind the Escape key to exit the program
root.bind("<Escape>", exit_program)

greeting = ttk.Label(root, text="Hello, welcome to MyHealth!", font=("Arial", 20, "bold"),anchor="center")
greeting.grid(row=0, column=1, sticky='nsew')

button = ttk.Button(root, text="Add Entry")
button.grid(row=1, column=1, sticky='nsew')

goals_label = ttk.Labelframe(root, text="Goals")
goals_label.grid(row=1, column=0, sticky='nsew')

goals_output_1 = ttk.Label(goals_label, text="First goal")
goals_output_1.grid(row=0, column=0)

goals_output_2 = ttk.Label(goals_label, text="Second goal")
goals_output_2.grid(row=1, column=0)

goals_output_3 = ttk.Label(goals_label, text="Third goal")
goals_output_3.grid(row=2, column=0)

accomplishments_label = ttk.Labelframe(root, text="accomplishments")
accomplishments_label.grid(row=2, column=0, sticky='nsew')

accomplishments_output_1 = ttk.Label(accomplishments_label, text="First accomplishment")
accomplishments_output_1.grid(row=0, column=0)

accomplishments_output_2 = ttk.Label(accomplishments_label, text="Second accomplishment")
accomplishments_output_2.grid(row=1, column=0)

accomplishments_output_3 = ttk.Label(accomplishments_label, text="Third accomplishment")
accomplishments_output_3.grid(row=2, column=0)

coping_strategies_label = ttk.Labelframe(root, text="Coping Strategies")
coping_strategies_label.grid(row=3, column=0, sticky='nsew')

coping_strategies_output_1 = ttk.Label(coping_strategies_label, text="First coping strategy")
coping_strategies_output_1.grid(row=0, column=0)

coping_strategies_output_2 = ttk.Label(coping_strategies_label, text="Second coping strategy")
coping_strategies_output_2.grid(row=1, column=0)

coping_strategies_output_3 = ttk.Label(coping_strategies_label, text="Third coping strategy")
coping_strategies_output_3.grid(row=2, column=0)

gratitudes_label = ttk.Labelframe(root, text="Gratitudes")
gratitudes_label.grid(row=1, column=2, sticky='nsew')

gratitudes_output_1 = ttk.Label(gratitudes_label, text="First gratitude")
gratitudes_output_1.grid(row=0, column=0)

gratitudes_output_2 = ttk.Label(gratitudes_label, text="Second gratitude")
gratitudes_output_2.grid(row=1, column=0)

gratitudes_output_3 = ttk.Label(gratitudes_label, text="Third gratitude")
gratitudes_output_3.grid(row=2, column=0)

reflections_label = ttk.Labelframe(root, text="Reflections")
reflections_label.grid(row=2, column=2, sticky='nsew')

reflections_output_1 = ttk.Label(reflections_label, text="First reflection")
reflections_output_1.grid(row=0, column=0)

reflections_output_2 = ttk.Label(reflections_label, text="Second reflection")
reflections_output_2.grid(row=1, column=0)

reflections_output_3 = ttk.Label(reflections_label, text="Third reflection")
reflections_output_3.grid(row=2, column=0)

self_care_activities_label = ttk.Labelframe(root, text="Self-care Activities")
self_care_activities_label.grid(row=3, column=2, sticky='nsew')

self_care_activities_output_1 = ttk.Label(self_care_activities_label, text="First self-care activity")
self_care_activities_output_1.grid(row=0, column=0)

self_care_activities_output_2 = ttk.Label(self_care_activities_label, text="Second self-care activity")
self_care_activities_output_2.grid(row=1, column=0)

self_care_activities_output_3 = ttk.Label(self_care_activities_label, text="Third self-care activity")
self_care_activities_output_3.grid(row=2, column=0)

root.mainloop()
