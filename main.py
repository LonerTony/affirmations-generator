import requests
import json
import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk

# Window size and position
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
WINDOW_X_POS = 100
WINDOW_Y_POS = 100

# App color scheme
PRIMARY_COLOR = "#7EB2B1"
SECONDARY_COLOR = "#F2EEE8"
ACCENT_COLOR = "#4b6a6a"

# Create the main window
root = tk.Tk()
root.title("Affirmations Journal")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X_POS}+{WINDOW_Y_POS}")
root.config(bg=PRIMARY_COLOR)

# Canvas for lotus logo
canvas = tk.Canvas(root, width=110, height=110, bg=PRIMARY_COLOR)
canvas.pack(side=tk.TOP, pady=20)

# Load the lotus.png image
image = Image.open("lotus.png")
photo = ImageTk.PhotoImage(image)  # Convert the image to be tkinter-compatible
canvas.create_image(50, 50, image=photo)  # Place image on canvas

def get_affirmation():
    """ Retrieves a random affirmation from the https://www.affirmations.dev/ API. """
    try:
        response = requests.get("https://www.affirmations.dev/")
        affirmation = json.loads(response.text)["affirmation"]
        return affirmation
    except:
        raise Exception("Unable to retrieve affirmation right now. Try again later.")

def show_affirmation():
    """ Displays an affirmation in the UI. """
    affirmation = get_affirmation()
    if affirmation:
        affirmation_text.set(affirmation)

affirmation_text = tk.StringVar()
affirmation_label = tk.Label(root, textvariable=affirmation_text, font=("Helvetica", 20),
                             bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, wraplength=300)
affirmation_label.pack(pady=5)

new_affirmation_button = tk.Button(root, text="New Affirmation", font=("Helvetica", 14),
                                   bg=ACCENT_COLOR, fg=SECONDARY_COLOR, command=show_affirmation)
new_affirmation_button.pack(pady=0)

thoughts_label = tk.Label(root, text="Enter your thoughts about these affirmations:",
                          font=("Times New Roman", 12), bg=PRIMARY_COLOR, fg=SECONDARY_COLOR)
thoughts_label.pack(pady=10)

thoughts_textbox = tk.Text(root, height=4, width=40, wrap=tk.WORD, font=("Helvetica", 9))
thoughts_textbox.pack()

def save_thoughts():
    """ Save the thoughts entered in the textbox to a text file. """
    thoughts = thoughts_textbox.get("1.0", tk.END).strip()
    if thoughts:
        date = datetime.now().strftime("%m/%d/%Y")
        affirmation = affirmation_text.get()
        log_string = f"{date}\nAffirmation: {affirmation}\nMy thoughts: {thoughts}\n\n"
        with open("thoughts.txt", "a") as f:
            f.write(log_string)
        thoughts_textbox.delete("1.0", tk.END)
        saved_label = tk.Label(root, text="Thoughts saved!", font=("Helvetica", 9))
        saved_label.pack()
        root.after(2000, saved_label.destroy)

save_button = tk.Button(root, text="Save Thoughts", font=("Helvetica", 14),
                        bg=ACCENT_COLOR, fg=SECONDARY_COLOR, command=save_thoughts)
save_button.pack(pady=10)
# attempting to add another button to auto generate affrimations on a timely basis // btn = Button(root, text = 'Click me !', bd = '5',command = root.destroy) 
# Adding an Exit button
exit_button = tk.Button(root, text="Exit", font=("Helvetica", 14),
                        bg=ACCENT_COLOR, fg=SECONDARY_COLOR, command=root.destroy)
exit_button.pack(pady=10)

# Adding a clock display
clock_label = tk.Label(root, font=('Helvetica', 14), fg=SECONDARY_COLOR, bg=PRIMARY_COLOR)
clock_label.pack(pady=10)

def update_clock():
    now = datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=now)
    root.after(1000, update_clock)  # update the time every second (1000 milliseconds)

update_clock()  # initial call to display the clock

root.mainloop()