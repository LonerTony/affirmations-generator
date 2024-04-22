import requests
import json
import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk

# Window size and position
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
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
canvas = tk.Canvas(root, width=100, height=100, bg=PRIMARY_COLOR)
canvas.pack(side=tk.TOP, pady=20)

# Load the lotus.png image
image = Image.open("lotus.png")

# Convert the image to be tkinter-compatible
photo = ImageTk.PhotoImage(image)

# Place image on canvas
canvas.create_image(50, 50, image=photo)


def get_affirmation():
  """
    Retrieves a random affirmation from the https://www.affirmations.dev/ API.

    Parameters: None

    Returns:
        str: A string containing the random affirmation.

    Raises:
        Exception: If the API request fails.
    """
  try:
    response = requests.get("https://www.affirmations.dev/")
    affirmation = json.loads(response.text)["affirmation"]
    return affirmation
  except:
    raise Exception(
      "Unable to retrieve affirmation right now. Try again later.")


def show_affirmation():
  """
    Displays an affirmation in the UI based on the result from the get_affirmations function.
    
    Parameters: 
        None
    
    Returns: 
        None
    """
  affirmation = get_affirmation()
  if affirmation:
    affirmation_text.set(affirmation)


# Create the affirmation label
affirmation_text = tk.StringVar()
affirmation_label = tk.Label(root,
                             textvariable=affirmation_text,
                             font=("Helvetica", 20),
                             bg=PRIMARY_COLOR,
                             fg=SECONDARY_COLOR,
                             wraplength=300)
affirmation_label.pack(pady=5)

# Create the "New Affirmation" button
new_affirmation_button = tk.Button(root,
                                   text="New Affirmation",
                                   font=("Helvetica", 14),
                                   bg=ACCENT_COLOR,
                                   fg=SECONDARY_COLOR,
                                   activebackground=ACCENT_COLOR,
                                   activeforeground=SECONDARY_COLOR,
                                   command=show_affirmation)
new_affirmation_button.pack(pady=0)

# Create the thoughts label
thoughts_label = tk.Label(root,
                          text="Enter your thoughts about these affirmations:",
                          font=("Helvetica", 12),
                          bg=PRIMARY_COLOR,
                          fg=SECONDARY_COLOR)
thoughts_label.pack(pady=10)

# Create the thoughts text box
thoughts_textbox = tk.Text(root,
                           height=4,
                           width=40,
                           wrap=tk.WORD,
                           font=("Helvetica", 9))
thoughts_textbox.pack()


# Define the function to save thoughts with the date
def save_thoughts():
  """
  Save the thoughts entered in the thoughts_textbox to a text file and display a label indicating that the
    thoughts were saved. The label is automatically destroyed after 2 seconds.

  Parameters: 
      None

  Returns:
        None
  """
  thoughts = thoughts_textbox.get("1.0", tk.END).strip()
  if thoughts:
    date = datetime.now().strftime("%m/%d/%Y")
    affirmation = affirmation_text.get()
    log_string = f"{date}\n Affirmation: {affirmation}\n My thoughts: {thoughts}\n\n"
    with open("thoughts.txt", "a") as f:
      f.write(log_string)
    thoughts_textbox.delete("1.0", tk.END)
    saved_label = tk.Label(root, text="Thoughts saved!", font=("Helvetica", 9))
    saved_label.pack()
    root.after(2000, saved_label.destroy)


save_button = tk.Button(root,
                        text="Save Thoughts",
                        font=("Helvetica", 14),
                        bg=ACCENT_COLOR,
                        fg=SECONDARY_COLOR,
                        activebackground=ACCENT_COLOR,
                        activeforeground=SECONDARY_COLOR,
                        command=save_thoughts)
save_button.pack(pady=10)

# Start the main event loop
root.mainloop()
