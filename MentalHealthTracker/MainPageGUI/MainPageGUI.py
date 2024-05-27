import tkinter as tk
from tkinter.font import BOLD
import tkinter.ttk as ttk
from turtle import color
import Main

def on_resize(event):
    # Update the size of the frame when the window is resized
    frame.config(width=root.winfo_width(), height=root.winfo_height())

# def show_window(window):
#     window.deiconify()

# def hide_window(window):
#     window.withdraw()

# def switch_windows(window_to_hide, window_to_show):
#     hide_window(window_to_hide)
#     show_window(window_to_show)

# Main window
root = tk.Tk()
root.title("Main Window")

# # Create a button to open Window 1
# button_window1 = ttk.Button(root, text="Open Window 1", command=lambda: show_window(window1))
# button_window1.pack(pady=10)

# # Create a button to open Window 2
# button_window2 = ttk.Button(root, text="Open Window 2", command=lambda: show_window(window2))
# button_window2.pack(pady=10)

# # Window 1
# window1 = tk.Toplevel(root)
# window1.title("Window 1")
# window1.geometry("300x200")
# label_window1 = ttk.Label(window1, text="This is Window 1")
# label_window1.pack(pady=10)
# window1.withdraw()  # Hide Window 1 initially

# # Window 2
# window2 = tk.Toplevel(root)
# window2.title("Window 2")
# window2.geometry("300x200")
# label_window2 = ttk.Label(window2, text="This is Window 2")
# label_window2.pack(pady=10)
# window2.withdraw()  # Hide Window 2 initially

# root = tk.Tk()
# root.title("My First Tkinter App")

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

frame = ttk.Frame(root, width=screen_width, height=screen_height)
frame.pack(fill=tk.BOTH, expand=True)  # Fill the entire root

# Prevent the frame from shrinking to fit its contents
frame.pack_propagate(False)

# Bind the resize event to the on_resize function
root.bind("<Configure>", on_resize)

greeting = ttk.Label(master=frame, text="Hello, welcome to MyHealth!", font = ("Arial", 20, BOLD))
greeting.pack()

button = ttk.Button(master=frame, text="Test", command=Main.test)
button.pack()



root.mainloop()
