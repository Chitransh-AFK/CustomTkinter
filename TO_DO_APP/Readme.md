To-Do List App with CustomTkinter
Overview

This project is a simple To-Do List application built using CustomTkinter. The app allows users to:

Add tasks dynamically.

Display tasks with checkboxes.

Show temporary notifications (snackbars) for user feedback.

Limit tasks to a maximum of 8 items.

Provide a clean dark-themed interface.

The app demonstrates Python GUI development with custom widgets, dynamic layouts, and animated notifications.

File Structure
app.py               # Main application code
README.md            # Project documentation

Features

Add Tasks – Type your task in the input box and click the + button to add it to the list.

Task Checkboxes – Each task is displayed with a checkbox to mark it as complete.

Task Limit – Maximum of 8 tasks to prevent clutter.

Snackbars – Animated popup notifications appear above the input box for:

Empty input warning

Task added confirmation

Task limit reached warning

Dark Theme UI – Modern dark colors for comfortable reading and aesthetics.

Dynamic Layout – Tasks are added dynamically without breaking the layout, all widgets align properly.

Screenshot

Example screenshot showing the dark-themed UI with tasks and snackbar notifications.

Key Components
1. Main Application Class (App)

Inherits from ctk.CTk.

Sets up the main window with:

Dark background (#1A1C22)

Window size 500x500

Title: "To Do Means To Do"

2. Header Label

Displays the app title with custom font and color.

Positioned at the top using pack() with padding.

3. Tasks Frame

Container for all task checkboxes.

Expands to fill available vertical space.

Aligns tasks neatly on the left side.

4. Entry and Button Container

Holds input field and + button at the bottom.

Provides horizontal expansion and spacing.

5. Adding Tasks (add_task method)

Validates input.

Adds a CTkCheckBox for each task.

Shows snackbar notifications for feedback.

Limits the number of tasks to 8.

6. Snackbar Notification (show_snackbar method)

Animated label appearing above the input field.

Slides up smoothly and auto-disappears.

Displays messages for task addition, errors, or limits.

Dependencies

Python 3.9+

CustomTkinter – modern Tkinter widgets

pip install customtkinter


Optional: Pillow if images are added for future enhancements

pip install pillow

Summary

This To-Do app demonstrates:

Dynamic widget creation.

Real-time feedback via animated snackbars.

Clean, responsive layout using CustomTkinter.

Modern dark-themed GUI design with proper spacing, alignment, and readability.
