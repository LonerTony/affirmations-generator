# Affirmations Generator

This project is a simple affirmations generator that provides the user with a random, thought-provoking affirmation. The app has a simple interface where the user can view an affirmation and then record their thoughts using the journal feature. Thoughts are saved to a text file the user can view and refer to as a journal of their progress.

## Requirements
- Python 3.x
- `requests` module
- `json` module
- `tkinter` module
- `datetime` module
- `Pillow` module

## Usage
1. Click **New Affirmation** to generate a random affirmation.
1. Enter your thoughts about the affirmation in the provided text entry field.
1. Click **Save Thoughts** to save your thoughts to a text file. The text file is stored in the same location as the application. Thoughts are automatically saved in the following format.
    ```
   04/28/2023
     Affirmation: You got this
     My thoughts: Yes, I do!
   ```
   
## Documentation
The code is documented using docstrings to provide details on each function's parameters, behavior, and expected return values.

## Future Features
- A new iteration could allow the user to generate affirmations based on a subject. This may require a different API where thoughts are tagged or some additional language processing to read through affirmations that match the desired topic.
- It would also be helpful to have the thoughts journal display in another `tkinter` window or somwhere else in the app. The user could still have the option to view all thoughts in the text file for exporting or viewing elsewhere. 






Integrating affirmations into technology can help users shift their perspective and focus on the good in their lives especially in an environment connected to the internet where content isn’t entirely regulated. The primary users of this app would be individuals seeking to improve their mental health and daily well-being. This group could include professionals dealing with workplace stress, students facing academic pressures, or anyone navigating personal challenges. The universal appeal of positive affirmations means that the app could benefit a wide demographic, irrespective of age, occupation, or cultural background.
