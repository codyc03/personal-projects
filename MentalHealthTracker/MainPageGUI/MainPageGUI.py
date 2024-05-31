import tkinter as tk
from tkinter import ANCHOR, NSEW, ttk
from turtle import bgcolor
import Main as db

def on_resize(event):
    # Update the size of the root window when resized
    root.grid_rowconfigure(0, weight=6)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=12)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=12)
    root.grid_rowconfigure(5, weight=1)
    root.grid_rowconfigure(6, weight=12)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)
    root.grid_columnconfigure(2, weight=1)
    

def exit_program(event=None):
    root.destroy()

def clicked() :
    all_goals = db.get_reminders("goal","goals_new")
    goals_output_1.config(text= f"{all_goals[0]}")
    goals_output_2.config(text= f"{all_goals[1]}")
    goals_output_3.config(text= f"{all_goals[2]}")

    all_accomplishments = db.get_reminders("accomplishment", "accomplishments_new")
    accomplishments_output_1.config(text = f"{all_accomplishments[0]}")
    accomplishments_output_2.config(text = f"{all_accomplishments[1]}")
    accomplishments_output_3.config(text = f"{all_accomplishments[2]}")

    all_coping_strategies = db.get_reminders("coping_strategy", "coping_strategies_new")
    coping_strategies_output_1.config(text = f"{all_coping_strategies[0]}")
    coping_strategies_output_2.config(text = f"{all_coping_strategies[1]}")
    coping_strategies_output_3.config(text = f"{all_coping_strategies[2]}")
    
    all_gratitudes = db.get_reminders("gratitude", "gratitudes_new")
    gratitudes_output_1.config(text = f"{all_gratitudes[0]}")
    gratitudes_output_2.config(text = f"{all_gratitudes[1]}")
    gratitudes_output_3.config(text = f"{all_gratitudes[2]}")

    all_reflections = db.get_reminders("reflection", "reflections_new")
    reflections_output_1.config(text = f"{all_reflections[0]}")
    reflections_output_2.config(text = f"{all_reflections[1]}")
    reflections_output_3.config(text = f"{all_reflections[2]}")

    all_self_care_activities = db.get_reminders("self_care_activity", "self_care_activities_new")
    self_care_activities_output_1.config(text = f"{all_self_care_activities[0]}")
    self_care_activities_output_2.config(text = f"{all_self_care_activities[1]}")
    self_care_activities_output_3.config(text = f"{all_self_care_activities[2]}")
 
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

button = ttk.Button(root, text="Add Entry", command = clicked)
button.grid(row=5, column=1, sticky = 'ns')

goals_header = ttk.Label(root, text = "Goals", anchor= "center")
goals_header.grid(row=1, column=0, sticky= NSEW)

goals_label = ttk.Labelframe(root)
goals_label.grid(row=2, column=0, sticky='nsew')

goals_output_1 = ttk.Label(goals_label, text="First goal")
goals_output_1.grid(row=0, column=0)

goals_output_2 = ttk.Label(goals_label, text="Second goal")
goals_output_2.grid(row=1, column=0)

goals_output_3 = ttk.Label(goals_label, text="Third goal")
goals_output_3.grid(row=2, column=0)

accomplishments_header = ttk.Label(root, text = "Accomplishments", anchor= "center")
accomplishments_header.grid(row=3, column=0, sticky= NSEW)

accomplishments_label = ttk.Labelframe(root)
accomplishments_label.grid(row=4, column=0, sticky='nsew')

accomplishments_output_1 = ttk.Label(accomplishments_label, text="First accomplishment")
accomplishments_output_1.grid(row=0, column=0)

accomplishments_output_2 = ttk.Label(accomplishments_label, text="Second accomplishment")
accomplishments_output_2.grid(row=1, column=0)

accomplishments_output_3 = ttk.Label(accomplishments_label, text="Third accomplishment")
accomplishments_output_3.grid(row=2, column=0)

coping_strategies_header = ttk.Label(root, text = "Coping Strategies", anchor= "center")
coping_strategies_header.grid(row=5, column=0, sticky= NSEW)

coping_strategies_label = ttk.Labelframe(root)
coping_strategies_label.grid(row=6, column=0, sticky='nsew')

coping_strategies_output_1 = ttk.Label(coping_strategies_label, text="First coping strategy")
coping_strategies_output_1.grid(row=0, column=0)

coping_strategies_output_2 = ttk.Label(coping_strategies_label, text="Second coping strategy")
coping_strategies_output_2.grid(row=1, column=0)

coping_strategies_output_3 = ttk.Label(coping_strategies_label, text="Third coping strategy")
coping_strategies_output_3.grid(row=2, column=0)

gratitudes_header = ttk.Label(root, text = "Gratitudes", anchor= "center")
gratitudes_header.grid(row=1, column=2, sticky= NSEW)

gratitudes_label = ttk.Labelframe(root)
gratitudes_label.grid(row=2, column=2, sticky='nsew')

gratitudes_output_1 = ttk.Label(gratitudes_label, text="First gratitude")
gratitudes_output_1.grid(row=0, column=0)

gratitudes_output_2 = ttk.Label(gratitudes_label, text="Second gratitude")
gratitudes_output_2.grid(row=1, column=0)

gratitudes_output_3 = ttk.Label(gratitudes_label, text="Third gratitude")
gratitudes_output_3.grid(row=2, column=0)

reflections_header = ttk.Label(root, text = "Reflections", anchor= "center")
reflections_header.grid(row=3, column=2)

reflections_label = ttk.Labelframe(root)
reflections_label.grid(row=4, column=2, sticky='nsew')

reflections_output_1 = ttk.Label(reflections_label, text="First reflection")
reflections_output_1.grid(row=0, column=0)

reflections_output_2 = ttk.Label(reflections_label, text="Second reflection")
reflections_output_2.grid(row=1, column=0)

reflections_output_3 = ttk.Label(reflections_label, text="Third reflection")
reflections_output_3.grid(row=2, column=0)


self_care_activities_header = ttk.Label(root, text = "Self Care Activities", anchor= "center")
self_care_activities_header.grid(row=5, column=2, sticky= NSEW)

self_care_activities_label = ttk.Labelframe(root)
self_care_activities_label.grid(row=6, column=2, sticky='nsew')

self_care_activities_output_1 = ttk.Label(self_care_activities_label, text="First self-care activity")
self_care_activities_output_1.grid(row=0, column=0)

self_care_activities_output_2 = ttk.Label(self_care_activities_label, text="Second self-care activity")
self_care_activities_output_2.grid(row=1, column=0)

self_care_activities_output_3 = ttk.Label(self_care_activities_label, text="Third self-care activity")
self_care_activities_output_3.grid(row=2, column=0)

# Create a frame
user_entry_frame = ttk.Frame(root)
user_entry_frame.grid(row=2, column=1, rowspan=3, sticky="nsew")

# Configure grid weights for the frame
user_entry_frame.grid_columnconfigure(0, weight=1)
user_entry_frame.grid_rowconfigure(0, weight=1)

# Create a label inside the frame
test_label = ttk.Label(user_entry_frame, text="hello", background="blue", foreground="white")

# Configure grid weights for the label
test_label.grid(row=0, column=0, sticky="nsew")

# Create a frame
results_frame = ttk.Frame(root)
results_frame.grid(row=6, column=1, rowspan=2, sticky="nsew")

# Configure grid weights for the frame
results_frame.grid_columnconfigure(0, weight=1)
results_frame.grid_rowconfigure(0, weight=1)

# Create a label inside the frame
test_label = ttk.Label(results_frame, text="hello", background="green", foreground="white")

# Configure grid weights for the label
test_label.grid(row=0, column=0, sticky="nsew")

root.mainloop()
