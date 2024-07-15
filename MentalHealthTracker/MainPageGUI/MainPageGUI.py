from email.policy import default
from pstats import Stats
from pydoc import cli
from queue import Empty
import tkinter as tk
from tkinter import ANCHOR, BOTH, CENTER, NSEW, RAISED, ttk
from turtle import bgcolor
from unicodedata import category
import Main as db
from datetime import date
from tkinter import messagebox

# db.feed_values()
popup_input = Empty

def on_resize(event):
    # Update the size of the root window when resized
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=4)
    root.grid_rowconfigure(2, weight=12)
    root.grid_rowconfigure(3, weight=2)
    root.grid_rowconfigure(4, weight=4)
    root.grid_rowconfigure(5, weight=12)
    root.grid_rowconfigure(6, weight=2)
    root.grid_rowconfigure(7, weight=4)
    root.grid_rowconfigure(8, weight=12)
    root.grid_rowconfigure(9, weight=2)
    root.grid_rowconfigure(10, weight=1)

    

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)
    root.grid_columnconfigure(2, weight=1)
    
def add_reminder(input_value, text) : 
    try :
        if "Goal" in text :
            db.add_goal(input_value)
        elif "Accomplishment" in text :
            db.add_accomplishment(input_value)
        elif "Coping Strategy" in text :
            db.add_coping_strategy(input_value)
        elif "Gratitude" in text :
            db.add_gratitude(input_value)
        elif "Reflection" in text:
            db.add_reflection(input_value)
        elif "Self Care Activity" in text : 
            db.add_self_care_activity(input_value)
            
    except Exception:
        open_popup_error_alert()
 
def remove_reminder(input_value, text) : 
    try :
        if "Goal" in text :
            db.remove_goal(input_value)
        elif "Accomplishment" in text :
            db.remove_accomplishment(input_value)
        elif "Coping Strategy" in text :
            db.remove_coping_strategy(input_value)
        elif "Gratitude" in text :
            db.remove_gratitude(input_value)
        elif "Reflection" in text:
            db.remove_reflection(input_value)
        elif "Self Care Activity" in text : 
            db.remove_self_care_activity(input_value)
    
    except Exception:
        open_popup_error_alert()
        

# def fill_stats(headers, outputs, stats_popup, num) :
#     for i in range(0, len(headers), 2):
#         headers[i] = ttk.Label(stats_popup, text = f"Average {category} Over Past {num} Days", anchor= CENTER)
#         headers[i].grid(row=i, column=0, sticky = 'nsew')
        
#         outputs[i] = ttk.Label(stats_popup, text = db.get_avg(category_id, num), anchor= CENTER)
#         outputs[i].grid(rows=i + 1 , column=0, sticky = 'nsew')
        
#         for j in outputs :
#             outputs[j] = ttk.Label(stats_popup, text = db.get_avg(category_id, num), anchor= CENTER)
#             outputs[j].grid(rows=i + j , column=0, sticky = 'nsew')
   
            

def open_stats():
    try :
        # db.feed_values()
    
        stats_popup = tk.Toplevel(root)
        stats_popup.attributes('-fullscreen', True)
        # stats_popup.configure(bg='red')
    
        stats_popup.grid_columnconfigure(0, weight = 1)
        stats_popup.grid_columnconfigure(1, weight = 1)
        stats_popup.grid_columnconfigure(2, weight = 1)
        stats_popup.grid_columnconfigure(3, weight = 1)
        stats_popup.grid_columnconfigure(4, weight = 1)
        stats_popup.grid_columnconfigure(5, weight = 1)
        stats_popup.grid_columnconfigure(6, weight = 1)
        stats_popup.grid_columnconfigure(7, weight = 1)

    
        stats_popup.grid_rowconfigure(0, weight = 1)
        stats_popup.grid_rowconfigure(1, weight = 1)
        stats_popup.grid_rowconfigure(2, weight = 1)
        stats_popup.grid_rowconfigure(3, weight = 1)
        # stats_popup.grid_rowconfigure(4, weight = 1)
        # stats_popup.grid_rowconfigure(5, weight = 1)

        avg_header = ttk.Label(stats_popup, text = "Average over past...", anchor = CENTER)
        avg_header.grid(row=0,column=0, sticky = 'nsew')

        days_label = ttk.Label(stats_popup, text = "10 days\n20 days\n30 days", anchor = CENTER)
        days_label.grid(row=1,column=0,sticky='nsew')

        
        avg_header = ttk.Label(stats_popup, text = "Percent change of today\n    compared to past...", anchor = CENTER)
        avg_header.grid(row=2,column=0, sticky = 'nsew')

        days_label = ttk.Label(stats_popup, text = "10 days\n20 days\n30 days", anchor = CENTER)
        days_label.grid(row=3,column=0,sticky='nsew')

        avg_mood_header = ttk.Label(stats_popup, text = "Average Mood", anchor= CENTER)
        avg_mood_header.grid(row=0, column=1, sticky = 'nsew')
    
        avg_mood_output = ttk.Label(stats_popup, text="\n".join(str(round(entry,1)) for entry in db.get_avg(0)), anchor=CENTER)
        avg_mood_output.grid(row = 1, column = 1, sticky = 'nsew')

        avg_energy_level_header = ttk.Label(stats_popup, text = "Average Energy Level", anchor= CENTER)
        avg_energy_level_header.grid(row=0, column=2, sticky = 'nsew')
    
        avg_energy_level_output = ttk.Label(stats_popup, text ="\n".join(str(round(entry,1)) for entry in db.get_avg(1)), anchor = CENTER)
        avg_energy_level_output.grid(row = 1, column = 2, sticky = 'nsew')
    
        avg_sleep_duration_header = ttk.Label(stats_popup, text = "Average Sleep Duration", anchor= CENTER)
        avg_sleep_duration_header.grid(row=0, column=3, sticky = 'nsew')
    
        avg_sleep_duration_output = ttk.Label(stats_popup, text = "\n".join(str(round(entry,1)) for entry in db.get_avg(2)), anchor = CENTER)
        avg_sleep_duration_output.grid(row = 1, column = 3, sticky = 'nsew')
    
        avg_sleep_quality_header = ttk.Label(stats_popup, text = "Average Sleep Quality", anchor= CENTER)
        avg_sleep_quality_header.grid(row=0, column=4, sticky = 'nsew')
    
        avg_sleep_quality_output = ttk.Label(stats_popup, text = "\n".join(str(round(entry,1)) for entry in db.get_avg(3)), anchor = CENTER)
        avg_sleep_quality_output.grid(row = 1, column = 4, sticky = 'nsew')
    
        avg_physical_symptoms_header = ttk.Label(stats_popup, text = "Average Physical Symptoms", anchor= CENTER)
        avg_physical_symptoms_header.grid(row=0, column=5, sticky = 'nsew')
    
        avg_physical_symptoms_output = ttk.Label(stats_popup, text = "\n".join(str(round(entry,1)) for entry in db.get_avg(4)), anchor = CENTER)
        avg_physical_symptoms_output.grid(row = 1, column = 5, sticky = 'nsew')
    
        avg_social_interaction_header = ttk.Label(stats_popup, text = "Average Social Interaction", anchor= CENTER)
        avg_social_interaction_header.grid(row=0, column=6, sticky = 'nsew')
    
        avg_social_interaction_output = ttk.Label(stats_popup, text ="\n".join(str(round(entry,1)) for entry in db.get_avg(5)), anchor = CENTER)
        avg_social_interaction_output.grid(row = 1, column = 6, sticky = 'nsew')
    
        avg_physical_activity_header = ttk.Label(stats_popup, text = "Average Physical Activity", anchor= CENTER)
        avg_physical_activity_header.grid(row=0, column=7, sticky = 'nsew')
    
        avg_physical_activity_output = ttk.Label(stats_popup, text ="\n".join(str(round(entry,1)) for entry in db.get_avg(6)), anchor = CENTER)
        avg_physical_activity_output.grid(row = 1, column = 7, sticky = 'nsew')
    
        cmp_mood_header = ttk.Label(stats_popup, text = "Percent Change Mood", anchor= CENTER)
        cmp_mood_header.grid(row=2, column=1, sticky = 'nsew')
    
        cmp_mood_output = ttk.Label(stats_popup, text="\n".join(f"{str(round(entry,1))}%" for entry in db.get_cmp(0,db.get_avg(0)[0],db.get_avg(0)[1], db.get_avg(0)[2])), anchor=CENTER)
        cmp_mood_output.grid(row = 3, column = 1, sticky = 'nsew')

        cmp_energy_level_header = ttk.Label(stats_popup, text = "Percent Change Energy Level", anchor= CENTER)
        cmp_energy_level_header.grid(row=2, column=2, sticky = 'nsew')
    
        cmp_energy_level_output = ttk.Label(stats_popup, text ="\n".join(f"{str(round(entry,1))}%" for entry in db.get_cmp(1,db.get_avg(0)[0],db.get_avg(0)[1], db.get_avg(0)[2])), anchor = CENTER)
        cmp_energy_level_output.grid(row = 3, column = 2, sticky = 'nsew')
    
        cmp_sleep_duration_header = ttk.Label(stats_popup, text = "Percent Change Sleep Duration", anchor= CENTER)
        cmp_sleep_duration_header.grid(row=2, column=3, sticky = 'nsew')
    
        cmp_sleep_duration_output = ttk.Label(stats_popup, text ="\n".join(f"{str(round(entry,1))}%" for entry in db.get_cmp(2,db.get_avg(0)[0],db.get_avg(0)[1], db.get_avg(0)[2])), anchor = CENTER)
        cmp_sleep_duration_output.grid(row = 3, column = 3, sticky = 'nsew')
    
        cmp_sleep_quality_header = ttk.Label(stats_popup, text = "Percent Change Sleep Quality", anchor= CENTER)
        cmp_sleep_quality_header.grid(row=2, column=4, sticky = 'nsew')
    
        cmp_sleep_quality_output = ttk.Label(stats_popup, text ="\n".join(f"{str(round(entry,1))}%" for entry in db.get_cmp(3,db.get_avg(0)[0],db.get_avg(0)[1], db.get_avg(0)[2])), anchor = CENTER)
        cmp_sleep_quality_output.grid(row = 3, column = 4, sticky = 'nsew')
    
        cmp_physical_symptoms_header = ttk.Label(stats_popup, text = "Percent Change Physical Symptoms", anchor= CENTER)
        cmp_physical_symptoms_header.grid(row=2, column=5, sticky = 'nsew')
    
        cmp_physical_symptoms_output = ttk.Label(stats_popup, text ="\n".join(f"{str(round(entry,1))}%" for entry in db.get_cmp(4,db.get_avg(0)[0],db.get_avg(0)[1], db.get_avg(0)[2])), anchor = CENTER)
        cmp_physical_symptoms_output.grid(row =3, column = 5, sticky = 'nsew')
    
        cmp_social_interaction_header = ttk.Label(stats_popup, text = "Percent Change Social Interaction", anchor= CENTER)
        cmp_social_interaction_header.grid(row=2, column=6, sticky = 'nsew')
    
        cmp_social_interaction_output = ttk.Label(stats_popup, text ="\n".join(f"{str(round(entry,1))}%" for entry in db.get_cmp(5,db.get_avg(0)[0],db.get_avg(0)[1], db.get_avg(0)[2])), anchor = CENTER)
        cmp_social_interaction_output.grid(row =3, column = 6, sticky = 'nsew')
    
        cmp_physical_activity_header = ttk.Label(stats_popup, text = "Percent Change Physical Activity", anchor= CENTER)
        cmp_physical_activity_header.grid(row=2, column=7, sticky = 'nsew')
    
        cmp_physical_activity_output = ttk.Label(stats_popup, text ="\n".join(f"{str(round(entry,1))}%" for entry in db.get_cmp(6,db.get_avg(0)[0],db.get_avg(0)[1], db.get_avg(0)[2])), anchor = CENTER)
        cmp_physical_activity_output.grid(row =3, column = 7, sticky = 'nsew')

        # avg_mood_10_days_output = ttk.Label(stats_popup, text = db.get_avg(0, 10), anchor = CENTER)
        # avg_mood_10_days_output.grid(row = 1, column = 0, sticky = 'nsew')
    
        # avg_mood_30_days_header = ttk.Label(stats_popup, text = "Average Mood Over Past 30 Days", anchor= CENTER)
        # avg_mood_30_days_header.grid(row=2, column=0, sticky = 'nsew')

        # avg_mood_30_days_output = ttk.Label(stats_popup, text = db.get_avg(0, 30), anchor = CENTER)
        # avg_mood_30_days_output.grid(row = 3, column = 0, sticky = 'nsew')
    
        # avg_mood_90_days_header = ttk.Label(stats_popup, text = "Average Mood Over Past 90 Days", anchor= CENTER)
        # avg_mood_10_days_header.grid(row= 4, column=0, sticky = 'nsew')

        # avg_mood_90_days_output = ttk.Label(stats_popup, text = db.get_avg(0, 90), anchor = CENTER)
        # avg_mood_90_days_output.grid(row = 5, column = 0, sticky = 'nsew')
    
        # headers = []

        # fill_stats(headers,outputs, stats_popup, num = 0)

        
        # Function to close the popup
        def close_popup():
            stats_popup.destroy()
    
        style = ttk.Style()
        # style.theme_use('default')  # Change to the 'default' theme 
        style.configure('Close.TButton', background='red', foreground = 'black')
    
        # Create a red X button in the top right corner
        close_button = ttk.Button(stats_popup, text="X", command=close_popup, style='Close.TButton')
        close_button.place(relx=1.0, rely=0.0, anchor='ne', width=40, height=40)
    
    except Exception:
        open_popup_error_alert()
    
def open_popup(addsub, text):
    try :
        def handle_ok():
            input_value = entry.get()
        
            if addsub == 1 :
                add_reminder(input_value, text)
            elif addsub == 0 : 
                remove_reminder(input_value, text)
            
            refresh()
            popup.destroy()

        popup = tk.Toplevel(root)
        popup.title("User Input")

        # Set the size of the popup window
        popup_width = 300
        popup_height = 150

        # Calculate position to center the window on the screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - popup_width) // 2
        y = (screen_height - popup_height) // 2

        # Set the position of the popup window
        popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        label = ttk.Label(popup, text=f"{text}")
        label.pack(padx=10, pady=10)

        entry = ttk.Entry(popup, width=30)
        entry.pack(padx=10, pady=10)
        entry.focus()

        ok_button = ttk.Button(popup, text="OK", command=handle_ok)
        ok_button.pack(padx=10, pady=10)
        
    except Exception:
        open_popup_error_alert()
   
def exit_program(event=None):
    root.destroy()

def get_all_in_category(category) :
    try :
        all_in_category = db.get_reminders(category, "user_entries")
        all_category_string = "\n".join(str(entry) for entry in reversed(all_in_category[-10:]))
        return all_category_string
    except Exception:
        open_popup_error_alert()
   

def get_all_in_category_entries(category) :
    try :
        all_in_category = db.get_entries(category, "user_entries")
        all_category_string = "\n".join(str(entry) for entry in all_in_category[:10])
        return all_category_string
    except Exception:
        open_popup_error_alert()

def update_previous_entries() :
    try :
        date_label = ttk.Label(results_frame,text="DATE", anchor="center")
        date_label.grid(row=0,column=0, sticky='new')
    
        mood_label = ttk.Label(results_frame,text="MOOD", anchor="center")
        mood_label.grid(row=0,column=1, sticky='new')
    
        energy_level_label = ttk.Label(results_frame,text="ENERGY LEVEL", anchor="center")
        energy_level_label.grid(row=0,column=2, sticky='new')
    
        sleep_duration_label = ttk.Label(results_frame,text="SLEEP DURATION", anchor="center")
        sleep_duration_label.grid(row=0,column=3, sticky='new')
    
        sleep_quality_label = ttk.Label(results_frame,text="SLEEP QUALITY", anchor="center")
        sleep_quality_label.grid(row=0,column=4, sticky='new')

        physical_symptoms_label = ttk.Label(results_frame,text="PHYSICAL SYMPTOMS", anchor="center")
        physical_symptoms_label.grid(row=0,column=5, sticky='new')
    
        social_interaction_label = ttk.Label(results_frame,text="SOCIAL INTERACTION", anchor="center")
        social_interaction_label.grid(row=0,column=6, sticky='new')

        physical_activity_label = ttk.Label(results_frame,text="PHYSICAL ACTIVITY", anchor="center")
        physical_activity_label.grid(row=0,column=7, sticky='new')
    
        test = get_all_in_category("entry_date")

        last_10_entries_dates = ttk.Label(results_frame, text = get_all_in_category_entries("entry_date"), anchor='center')
        last_10_entries_dates.grid(row=1,column=0, sticky = 'n')
    
        last_10_entries_moods = ttk.Label(results_frame, text = get_all_in_category_entries("mood"), anchor='center')
        last_10_entries_moods.grid(row=1,column=1, sticky = 'n')
    
        last_10_entries_energy_levels = ttk.Label(results_frame, text = get_all_in_category_entries("energy_level"), anchor='center')
        last_10_entries_energy_levels.grid(row=1,column=2, sticky = 'n')

        last_10_entries_sleep_durations = ttk.Label(results_frame, text = get_all_in_category_entries("sleep_duration"), anchor='center')
        last_10_entries_sleep_durations.grid(row=1,column=3, sticky = 'n')
    
        last_10_entries_sleep_qualities = ttk.Label(results_frame, text = get_all_in_category_entries("sleep_quality"), anchor='center')
        last_10_entries_sleep_qualities.grid(row=1,column=4, sticky = 'n')
    
        last_10_entries_physical_symptoms = ttk.Label(results_frame, text = get_all_in_category_entries("physical_symptoms"), anchor='center')
        last_10_entries_physical_symptoms.grid(row=1,column=5, sticky = 'n')
    
        last_10_entries_social_interactions = ttk.Label(results_frame, text = get_all_in_category_entries("social_interaction"), anchor='center')
        last_10_entries_social_interactions.grid(row=1,column=6, sticky = 'n')
    
        last_10_entries_physical_activities = ttk.Label(results_frame, text = get_all_in_category_entries("physical_activity"), anchor='center')
        last_10_entries_physical_activities.grid(row=1,column=7, sticky = 'n')
    
    except Exception:
        open_popup_error_alert()
    
def update_output(output_widgets, all_outputs, default_output):
    num_outputs = len(all_outputs)
    progress = 0
    
    for i in range(min(num_outputs, 3)) :
         progress = i + 1
         output_text = f"{i+1}. {all_outputs[i]}"
        
         if i == 0:
             output_widgets[i].config(text=output_text, font=("Arial", 12), background = "")
         elif i == 1:
             output_widgets[i].config(text=output_text, font=("Arial", 12), background = "")
         elif i == 2:
             output_widgets[i].config(text=output_text, font=("Arial", 12), background = "")
       

    for i in range(progress,3) :
         if i == 0:
             output_widgets[i].config(text=default_output, font=("Arial", 12), background = "")
         elif i == 1:
             output_widgets[i].config(text=default_output, font=("Arial", 12), background = "")
         elif i == 2:
             output_widgets[i].config(text=default_output, font=("Arial", 12), background = "")
    
# def open_popup(addsub, text) :
#     if(addsub == 1) :
#         open_popup(addsub, text)
#     elif(addsub == 0) :
#         open_popup(addsub, text)
        
def refresh() :
    try :
        all_goals = db.get_reminders("goal","goals_new")
        default_goal = "Please Add Goal"
        goals_output_widgets = [goals_output_1, goals_output_2, goals_output_3]
        update_output(goals_output_widgets, all_goals, default_goal)

        all_accomplishments = db.get_reminders("accomplishment", "accomplishments_new")
        default_accomplishment = "Please Add Accomplishment"
        accomplishments_output_widgets = [accomplishments_output_1, accomplishments_output_2, accomplishments_output_3]
        update_output(accomplishments_output_widgets, all_accomplishments, default_accomplishment)

        all_coping_strategies = db.get_reminders("coping_strategy", "coping_strategies_new")
        default_coping_strategy = "Please Add Coping Strategy"
        coping_strategys_output_widgets = [coping_strategies_output_1, coping_strategies_output_2, coping_strategies_output_3]
        update_output(coping_strategys_output_widgets, all_coping_strategies, default_coping_strategy)
    
        all_gratitudes = db.get_reminders("gratitude", "gratitudes_new")
        default_gratitude = "Please Add Gratitude"
        gratitudes_output_widgets = [gratitudes_output_1, gratitudes_output_2, gratitudes_output_3]
        update_output(gratitudes_output_widgets, all_gratitudes, default_gratitude)

        all_reflections = db.get_reminders("reflection", "reflections_new")
        default_reflection = "Please Add reflection"
        reflections_output_widgets = [reflections_output_1, reflections_output_2, reflections_output_3]
        update_output(reflections_output_widgets, all_reflections, default_reflection)

        all_self_care_activities = db.get_reminders("self_care_activity", "self_care_activities_new")
        default_self_care_activity = "Please Add Self Care Activity"
        self_care_activitys_output_widgets = [self_care_activities_output_1, self_care_activities_output_2, self_care_activities_output_3]
        update_output(self_care_activitys_output_widgets, all_self_care_activities, default_self_care_activity)

        update_previous_entries()
    
    except Exception:
        open_popup_error_alert()
    
def open_error_alert(message) :
    messagebox.showinfo("Alert", message) 

def open_popup_error_alert() :
    root.geometry("+%d+%d" % ((root.winfo_screenwidth() - 300) // 2, (root.winfo_screenheight() - 200) // 2))
    
    # Show error message box
    messagebox.showerror("Error", "Operation failed. Please double check your work and try again.")

def clicked() :
    try :
        mood = user_entry_mood.get()
        energy_level = user_entry_energy.get()
        sleep_duration = user_entry_sleep.get()
        sleep_quality = user_entry_sleep_quality.get()
        physical_symptoms = user_entry_physical_symptoms.get()
        social_interaction = user_entry_social_interaction.get()
        physical_activity = user_entry_physical_activity.get()

        get_latest_entry_date = db.get_latest_entry_date()[0]

        if not get_latest_entry_date == date.today() :        
            db.add_entry(mood,energy_level,sleep_duration,sleep_quality,physical_symptoms,social_interaction,physical_activity)
            update_previous_entries()

        else : 
            open_error_alert("You have already entered your survery for today!")      
            
    except Exception:
        open_popup_error_alert()
            
 
root = tk.Tk()
root.title("Main Window")

# db.set_error_callback(open_popup_error_alert)

# Set the window attributes to fullscreen
root.attributes("-fullscreen", True)

# Bind the resize event to the on_resize function
root.bind("<Configure>", on_resize)

# Bind the Escape key to exit the program
root.bind("<Escape>", exit_program)

greeting = ttk.Label(root, text="Hello, welcome to MyHealth!", font=("Arial", 20, "bold"),anchor="center", background='dark green', relief=RAISED)
greeting.grid(row=1, column=1, sticky='nsew', padx=2)

two_button_frame = ttk.Frame(root)
two_button_frame.grid(row=7, column = 1, sticky='nsew')

two_button_frame.grid_columnconfigure(0, weight = 1)
two_button_frame.grid_columnconfigure(1, weight = 1)

button = ttk.Button(two_button_frame, text="Add Daily Entry", command = clicked)
button.grid(row= 0, column = 1, sticky = 'ew', padx=8, pady=2)

stats_button = ttk.Button(two_button_frame, text="View Stats", command=open_stats)
stats_button.grid(row = 0, column = 0, sticky='ew', padx=8, pady=2)

goals_header = ttk.Label(root, text = "Goals", anchor= "center", font=("Arial", 14, "bold"), relief='ridge', background='dark green')
goals_header.grid(row=1, column=0, sticky= NSEW)

goals_label = ttk.Frame(root)
goals_label.grid(row=2, column=0, sticky='nsew', padx=2, pady=2)

goals_buttons = ttk.Frame(root)
goals_buttons.grid(row=3, column = 0, sticky='nsew')

goals_buttons.grid_columnconfigure(0, weight=1)
goals_buttons.grid_columnconfigure(1, weight=1)

goals_buttons.grid_rowconfigure(0,weight=1)

add_goal_button = ttk.Button(goals_buttons, text="Add Goal", command=lambda: (open_popup(1, "Add Goal"), refresh()))
add_goal_button.grid(row=0, column = 0, sticky='nsew', padx=5, pady=5)

remove_goal_button = ttk.Button(goals_buttons, text = "Remove Goal", command=lambda: (open_popup(0, "Remove Goal"), refresh()))
remove_goal_button.grid(row=0, column = 1, sticky='nsew', padx=5, pady=5)

goals_label.grid_columnconfigure(0,weight=1)
goals_label.grid_rowconfigure(0,weight=1)
goals_label.grid_rowconfigure(1,weight=1)
goals_label.grid_rowconfigure(2,weight=1)

goals_output_1 = ttk.Label(goals_label, text="First goal", anchor=CENTER)
goals_output_1.grid(row=0, column=0, sticky = 'nsew')

goals_output_2 = ttk.Label(goals_label, text="Second goal", anchor=CENTER)
goals_output_2.grid(row=1, column=0,sticky='nsew')

goals_output_3 = ttk.Label(goals_label, text="Third goal", anchor=CENTER)
goals_output_3.grid(row=2, column=0, sticky='nsew')

accomplishments_header = ttk.Label(root, text = "Accomplishments", anchor= "center", font=("Arial", 14, "bold"), relief='ridge', background='dark green')
accomplishments_header.grid(row=4, column=0, sticky= NSEW)

accomplishments_label = ttk.Frame(root)
accomplishments_label.grid(row=5, column=0, sticky='nsew', padx=2, pady=2)

accomplishments_label.grid_columnconfigure(0,weight=1)
accomplishments_label.grid_rowconfigure(0,weight=1)
accomplishments_label.grid_rowconfigure(1,weight=1)
accomplishments_label.grid_rowconfigure(2,weight=1)

accomplishments_buttons = ttk.Frame(root)
accomplishments_buttons.grid(row=6, column = 0, sticky='nsew')

accomplishments_buttons.grid_columnconfigure(0, weight=1)
accomplishments_buttons.grid_columnconfigure(1, weight=1)

accomplishments_buttons.grid_rowconfigure(0,weight=1)

add_accomplishment_button = ttk.Button(accomplishments_buttons, text = "Add Accomplishment", command=lambda: (open_popup(1, "Add Accomplishment"), refresh()))
add_accomplishment_button.grid(row=0, column = 0, sticky='nsew', padx=5, pady=5)

remove_accomplishment_button = ttk.Button(accomplishments_buttons, text = "Remove Accomplishment",  command=lambda: (open_popup(0, "Remove Accomplishment"), refresh()))
remove_accomplishment_button.grid(row=0, column = 1, sticky='nsew', padx=5, pady=5)

accomplishments_output_1 = ttk.Label(accomplishments_label, text="First accomplishment", anchor=CENTER)
accomplishments_output_1.grid(row=0, column=0)

accomplishments_output_2 = ttk.Label(accomplishments_label, text="Second accomplishment", anchor=CENTER)
accomplishments_output_2.grid(row=1, column=0)

accomplishments_output_3 = ttk.Label(accomplishments_label, text="Third accomplishment", anchor=CENTER)
accomplishments_output_3.grid(row=2, column=0)

coping_strategies_header = ttk.Label(root, text = "Coping Strategies", anchor= "center", font=("Arial", 14, "bold"), relief='ridge', background='dark green')
coping_strategies_header.grid(row=7, column=0, sticky= NSEW)

coping_strategies_label = ttk.Frame(root)
coping_strategies_label.grid(row=8, column=0, sticky='nsew', padx=2, pady=2)


coping_strategys_buttons = ttk.Frame(root)
coping_strategys_buttons.grid(row=9, column = 0, sticky='nsew')

coping_strategys_buttons.grid_columnconfigure(0, weight=1)
coping_strategys_buttons.grid_columnconfigure(1, weight=1)

coping_strategys_buttons.grid_rowconfigure(0,weight=1)

add_coping_strategy_button = ttk.Button(coping_strategys_buttons, text = "Add Coping Strategy",  command=lambda: (open_popup(1, "Add Coping Strategy"), refresh()))
add_coping_strategy_button.grid(row=0, column = 0, sticky='nsew', padx=5, pady=5)

remove_coping_strategy_button = ttk.Button(coping_strategys_buttons, text = "Remove Coping Strategy",  command=lambda: (open_popup(0, "Remove Coping Strategy"), refresh()))
remove_coping_strategy_button.grid(row=0, column = 1, sticky='nsew', padx=5, pady=5)

coping_strategies_label.grid_columnconfigure(0,weight=1)
coping_strategies_label.grid_rowconfigure(0,weight=1)
coping_strategies_label.grid_rowconfigure(1,weight=1)
coping_strategies_label.grid_rowconfigure(2,weight=1)

coping_strategies_output_1 = ttk.Label(coping_strategies_label, text="First coping strategy", anchor=CENTER)
coping_strategies_output_1.grid(row=0, column=0)

coping_strategies_output_2 = ttk.Label(coping_strategies_label, text="Second coping strategy", anchor=CENTER)
coping_strategies_output_2.grid(row=1, column=0)

coping_strategies_output_3 = ttk.Label(coping_strategies_label, text="Third coping strategy", anchor=CENTER)
coping_strategies_output_3.grid(row=2, column=0)

gratitudes_header = ttk.Label(root, text = "Gratitudes", anchor= "center", font=("Arial", 14, "bold"), relief='ridge', background='dark green')
gratitudes_header.grid(row=1, column=2, sticky= NSEW)

gratitudes_label = ttk.Frame(root)
gratitudes_label.grid(row=2, column=2, sticky='nsew', padx=2, pady=2)


gratitudes_buttons = ttk.Frame(root)
gratitudes_buttons.grid(row=3, column = 2, sticky='nsew')

gratitudes_buttons.grid_columnconfigure(0, weight=1)
gratitudes_buttons.grid_columnconfigure(1, weight=1)

gratitudes_buttons.grid_rowconfigure(0,weight=1)

add_gratitude_button = ttk.Button(gratitudes_buttons, text = "Add Gratitude", command=lambda: (open_popup(1, "Add Gratitude"), refresh()))
add_gratitude_button.grid(row=0, column = 0, sticky='nsew', padx=5, pady=5)

remove_gratitude_button = ttk.Button(gratitudes_buttons, text = "Remove Gratitude",  command=lambda: (open_popup(0, "Remove Gratitude"), refresh()))
remove_gratitude_button.grid(row=0, column = 1, sticky='nsew', padx=5, pady=5)

gratitudes_label.grid_columnconfigure(0,weight=1)
gratitudes_label.grid_rowconfigure(0,weight=1)
gratitudes_label.grid_rowconfigure(1,weight=1)
gratitudes_label.grid_rowconfigure(2,weight=1)

gratitudes_output_1 = ttk.Label(gratitudes_label, text="First gratitude", anchor=CENTER)
gratitudes_output_1.grid(row=0, column=0)

gratitudes_output_2 = ttk.Label(gratitudes_label, text="Second gratitude", anchor=CENTER)
gratitudes_output_2.grid(row=1, column=0)

gratitudes_output_3 = ttk.Label(gratitudes_label, text="Third gratitude", anchor=CENTER)
gratitudes_output_3.grid(row=2, column=0)

reflections_header = ttk.Label(root, text = "Reflections", anchor= "center", font=("Arial", 14, "bold"), relief='ridge', background='dark green')
reflections_header.grid(row=4, column=2, sticky= NSEW)

reflections_label = ttk.Frame(root)
reflections_label.grid(row=5, column=2, sticky='nsew', padx=2, pady=2)


reflections_buttons = ttk.Frame(root)
reflections_buttons.grid(row=6, column = 2, sticky='nsew')

reflections_buttons.grid_columnconfigure(0, weight=1)
reflections_buttons.grid_columnconfigure(1, weight=1)

reflections_buttons.grid_rowconfigure(0,weight=1)

add_reflection_button = ttk.Button(reflections_buttons, text = "Add Reflection", command=lambda: (open_popup(1, "Add Reflection"), refresh()))
add_reflection_button.grid(row=0, column = 0, sticky='nsew', padx=5, pady=5)

remove_reflection_button = ttk.Button(reflections_buttons, text = "Remove Reflection", command=lambda: (open_popup(0, "Remove Reflection"), refresh()))
remove_reflection_button.grid(row=0, column = 1, sticky='nsew', padx=5, pady=5)

reflections_label.grid_columnconfigure(0,weight=1)
reflections_label.grid_rowconfigure(0,weight=1)
reflections_label.grid_rowconfigure(1,weight=1)
reflections_label.grid_rowconfigure(2,weight=1)

reflections_output_1 = ttk.Label(reflections_label, text="First reflection", anchor=CENTER)
reflections_output_1.grid(row=0, column=0)

reflections_output_2 = ttk.Label(reflections_label, text="Second reflection", anchor=CENTER)
reflections_output_2.grid(row=1, column=0)

reflections_output_3 = ttk.Label(reflections_label, text="Third reflection", anchor=CENTER)
reflections_output_3.grid(row=2, column=0)

self_care_activities_header = ttk.Label(root, text = "Self Care Activities", anchor= "center", font=("Arial", 14, "bold"), relief='ridge', background='dark green')
self_care_activities_header.grid(row=7, column=2, sticky= NSEW)

self_care_activities_label = ttk.Frame(root)
self_care_activities_label.grid(row=8, column=2, sticky='nsew', padx=2, pady=2)


self_care_activitys_buttons = ttk.Frame(root)
self_care_activitys_buttons.grid(row=9, column = 2, sticky='nsew')

self_care_activitys_buttons.grid_columnconfigure(0, weight=1)
self_care_activitys_buttons.grid_columnconfigure(1, weight=1)

self_care_activitys_buttons.grid_rowconfigure(0,weight=1)

add_self_care_activity_button = ttk.Button(self_care_activitys_buttons, text = "Add Self Care Activity", command=lambda: (open_popup(1, "Add Self Care Activity"), refresh()))
add_self_care_activity_button.grid(row=0, column = 0, sticky='nsew', padx=5, pady=5)

remove_self_care_activity_button = ttk.Button(self_care_activitys_buttons, text = "Remove Self Care Activity", command=lambda: (open_popup(0, "Remove Self Care Activity"), refresh()))
remove_self_care_activity_button.grid(row=0, column = 1, sticky='nsew', padx=5, pady=5)

self_care_activities_label.grid_columnconfigure(0,weight=1)
self_care_activities_label.grid_rowconfigure(0,weight=1)
self_care_activities_label.grid_rowconfigure(1,weight=1)
self_care_activities_label.grid_rowconfigure(2,weight=1)

self_care_activities_output_1 = ttk.Label(self_care_activities_label, text="First self-care activity", anchor=CENTER)
self_care_activities_output_1.grid(row=0, column=0)

self_care_activities_output_2 = ttk.Label(self_care_activities_label, text="Second self-care activity", anchor=CENTER)
self_care_activities_output_2.grid(row=1, column=0)

self_care_activities_output_3 = ttk.Label(self_care_activities_label, text="Third self-care activity", anchor=CENTER)
self_care_activities_output_3.grid(row=2, column=0)

# Create a frame
user_entry_frame = ttk.Frame(root)
user_entry_frame.grid(row=2, column=1, rowspan=5, sticky="nsew", pady=2, padx=8)

# Configure grid weights for the frame
user_entry_frame.grid_columnconfigure(0, weight=1)
user_entry_frame.grid_columnconfigure(1, weight=1)

user_entry_frame.grid_rowconfigure(0, weight=1)
user_entry_frame.grid_rowconfigure(1, weight=1)
user_entry_frame.grid_rowconfigure(2, weight=1)
user_entry_frame.grid_rowconfigure(3, weight=1)
user_entry_frame.grid_rowconfigure(4, weight=1)
user_entry_frame.grid_rowconfigure(5, weight=1)
user_entry_frame.grid_rowconfigure(6, weight=1)
user_entry_frame.grid_rowconfigure(7, weight=1)


# Create a label inside the frame
user_entry_label1 = ttk.Label(user_entry_frame, text="On a scale of 1-10, how was your mood today?", anchor="center", background="tan", foreground="white", relief=RAISED)
user_entry_label2 = ttk.Label(user_entry_frame, text="On a scale of 1-10, how was your energy level today?", anchor="center", background="tan", foreground="white", relief=RAISED)
user_entry_label3 = ttk.Label(user_entry_frame, text="How long did you sleep for?", anchor="center", background="tan", foreground="white", relief=RAISED)
user_entry_label4 = ttk.Label(user_entry_frame, text="On a scale of 1-10, how was your sleep quality?", anchor="center", background="tan", foreground="white", relief=RAISED)
user_entry_label5 = ttk.Label(user_entry_frame, text="On a scale of 1-10, how would you rate your physical symptoms today?", anchor="center", background="tan", foreground="white", relief=RAISED)
user_entry_label6 = ttk.Label(user_entry_frame, text="How many hours of social interaction did you have today?", anchor="center", background="tan", foreground="white", relief=RAISED)
user_entry_label7 = ttk.Label(user_entry_frame, text="How many hours of physical activity did you have today?", anchor="center", background="tan", foreground="white", relief=RAISED)

user_entry_mood = ttk.Entry(user_entry_frame, background="blue")
user_entry_energy = ttk.Entry(user_entry_frame, background="blue")
user_entry_sleep = ttk.Entry(user_entry_frame, background="blue")
user_entry_sleep_quality = ttk.Entry(user_entry_frame, background="blue")
user_entry_physical_symptoms = ttk.Entry(user_entry_frame, background="blue")
user_entry_social_interaction = ttk.Entry(user_entry_frame, background="blue")
user_entry_physical_activity = ttk.Entry(user_entry_frame, background="yellow")

# Configure grid weights for the label
user_entry_label1.grid(row=0, column=0, sticky='nsew')
user_entry_label2.grid(row=1,column=0, sticky='nsew')
user_entry_label3.grid(row=2, column=0, sticky='nsew')
user_entry_label4.grid(row=3,column=0, sticky='nsew')
user_entry_label5.grid(row=4, column=0, sticky='nsew')
user_entry_label6.grid(row=5,column=0, sticky='nsew')
user_entry_label7.grid(row=6, column=0, sticky='nsew')

user_entry_mood.grid(row=0, column=1, sticky='nsew')
user_entry_energy.grid(row=1,column=1, sticky='nsew')
user_entry_sleep.grid(row=2, column=1, sticky='nsew')
user_entry_sleep_quality.grid(row=3,column=1, sticky='nsew')
user_entry_physical_symptoms.grid(row=4, column=1, sticky='nsew')
user_entry_social_interaction.grid(row=5,column=1, sticky='nsew')
user_entry_physical_activity.grid(row=6, column=1, sticky='nsew')

# Create a frame
results_frame = ttk.Frame(root)
results_frame.grid(row=8, column=1, rowspan=3, sticky="nsew")

# Configure grid weights for the frame
results_frame.grid_columnconfigure(0, weight=1)
results_frame.grid_columnconfigure(1, weight=1)
results_frame.grid_columnconfigure(2, weight=1)
results_frame.grid_columnconfigure(3, weight=1)
results_frame.grid_columnconfigure(4, weight=1)
results_frame.grid_columnconfigure(5, weight=1)
results_frame.grid_columnconfigure(6, weight=1)
results_frame.grid_columnconfigure(7, weight=1)

results_frame.grid_rowconfigure(0, weight=1)
results_frame.grid_rowconfigure(1, weight=1)


# # Create a label inside the frame
# test_label = ttk.Label(results_frame, text="hello", background="green", foreground="white")

# # Configure grid weights for the label
# test_label.grid(row=0, column=0, sticky="nsew")

refresh()

root.mainloop()
