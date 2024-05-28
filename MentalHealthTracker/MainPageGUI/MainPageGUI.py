import tkinter as tk
from tkinter import ttk

def on_resize(event):
    # Update the size of the frame when the window is resized
    frame.config(width=root.winfo_width(), height=root.winfo_height())

def exit_program(event=None):
    root.destroy()

root = tk.Tk()
root.title("Main Window")

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window attributes to fullscreen
root.attributes("-fullscreen", True)

frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)  # Fill the entire window

# Prevent the frame from shrinking to fit its contents
frame.pack_propagate(False)

# Bind the resize event to the on_resize function
root.bind("<Configure>", on_resize)

# Bind the Escape key to exit the program
root.bind("<Escape>", exit_program)

greeting = ttk.Label(master=frame, text="Hello, welcome to MyHealth!", font=("Arial", 20, "bold"))
greeting.pack()

button = ttk.Button(master=frame, text="Add Entry")
button.pack()

goals_label = ttk.Labelframe(master=frame, text="Goals")
goals_label.pack()

goals_output_1 = ttk.Label(master=goals_label, text="First goal")
goals_output_1.pack()

goals_output_2 = ttk.Label(master=goals_label, text="Second goal")
goals_output_2.pack()

goals_output_3 = ttk.Label(master=goals_label, text="Third goal")
goals_output_3.pack()

accomplishments_label = ttk.Labelframe(master=frame, text="accomplishments")
accomplishments_label.pack()

accomplishments_output_1 = ttk.Label(master=accomplishments_label, text="First accomplishment")
accomplishments_output_1.pack()

accomplishments_output_2 = ttk.Label(master=accomplishments_label, text="Second accomplishment")
accomplishments_output_2.pack()

accomplishments_output_3 = ttk.Label(master=accomplishments_label, text="Third accomplishment")
accomplishments_output_3.pack()

coping_strategies_label = ttk.Labelframe(master=frame, text="coping_strategies")
coping_strategies_label.pack()

coping_strategies_output_1 = ttk.Label(master=coping_strategies_label, text="First coping strategy")
coping_strategies_output_1.pack()

coping_strategies_output_2 = ttk.Label(master=coping_strategies_label, text="Second coping strategy")
coping_strategies_output_2.pack()

coping_strategies_output_3 = ttk.Label(master=coping_strategies_label, text="Third coping strategy")
coping_strategies_output_3.pack()


gratitudes_label = ttk.Labelframe(master=frame, text="gratitudes")
gratitudes_label.pack()

gratitudes_output_1 = ttk.Label(master=gratitudes_label, text="First gratitude")
gratitudes_output_1.pack()

gratitudes_output_2 = ttk.Label(master=gratitudes_label, text="Second gratitude")
gratitudes_output_2.pack()

gratitudes_output_3 = ttk.Label(master=gratitudes_label, text="Third gratitude")
gratitudes_output_3.pack()

reflections_label = ttk.Labelframe(master=frame, text="reflections")
reflections_label.pack()

reflections_output_1 = ttk.Label(master=reflections_label, text="First reflection")
reflections_output_1.pack()

reflections_output_2 = ttk.Label(master=reflections_label, text="Second reflection")
reflections_output_2.pack()

reflections_output_3 = ttk.Label(master=reflections_label, text="Third reflection")
reflections_output_3.pack()

self_care_activities_label = ttk.Labelframe(master=frame, text="self_care_activities")
self_care_activities_label.pack()

self_care_activities_output_1 = ttk.Label(master=self_care_activities_label, text="First self_care_activity")
self_care_activities_output_1.pack()

self_care_activities_output_2 = ttk.Label(master=self_care_activities_label, text="Second self_care_activity")
self_care_activities_output_2.pack()

self_care_activities_output_3 = ttk.Label(master=self_care_activities_label, text="Third self_care_activity")
self_care_activities_output_3.pack()

stressors_label = ttk.Labelframe(master=frame, text="stressors")
stressors_label.pack()

stressors_output_1 = ttk.Label(master=stressors_label, text="First stressor")
stressors_output_1.pack()

stressors_output_2 = ttk.Label(master=stressors_label, text="Second stressor")
stressors_output_2.pack()

stressors_output_3 = ttk.Label(master=stressors_label, text="Third stressor")
stressors_output_3.pack()

root.mainloop()
