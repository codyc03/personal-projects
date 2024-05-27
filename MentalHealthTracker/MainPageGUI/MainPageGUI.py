import tkinter as tk
import tkinter.ttk as ttk

def on_resize(event):
    # Update the size of the frame when the window is resized
    frame.config(width=window.winfo_width(), height=window.winfo_height())

window = tk.Tk()
window.title("My First Tkinter App")

# Get the screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

frame = ttk.Frame(window, width=screen_width, height=screen_height)
frame.pack(fill=tk.BOTH, expand=True)  # Fill the entire window

# Prevent the frame from shrinking to fit its contents
frame.pack_propagate(False)

# Bind the resize event to the on_resize function
window.bind("<Configure>", on_resize)

greeting = ttk.Label(master=frame, text="Hello, Tkinter!")
greeting.pack()

window.mainloop()
