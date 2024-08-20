# Window Selector and Transparency Tool

## Overview
This script provides a graphical user interface (GUI) that allows you to select an open window and adjust its properties such as transparency and click-through behaviour. The application is built using Python with the `tkinter` library for the GUI and the `win32` libraries for interacting with Windows system APIs.

## Features
- **Select an open window**: Choose any currently open window from a dropdown list.
- **Set transparency**: Adjust the transparency level of the selected window.
- **Enable click-through**: Make the window click-through, allowing clicks to pass through it.
- **Always on top**: Keep the selected window on top of all other windows.
- **Reset properties**: Restore the selected window to its default state.

## Requirements
- Python 3.x
- Required Python packages:
  - `ctypes`
  - `tkinter` (included with Python standard library)
  - `pywin32` (install with `pip install pywin32`)

## How to Run
1. **Install the required packages**:
   Open a terminal or command prompt and run:
   ```bash
   pip install pywin32
   ```

2. **Run the script**:
   Execute the script by running the following command in your terminal or command prompt:
   ```bash
   python <script_name>.py
   ```

3. **Use the GUI**:
   - Select a window from the dropdown list.
   - Adjust the transparency using the slider.
   - Click "Apply" to apply the settings.
   - Click "Reset" to restore the window's default settings.
   - Click "Update" to refresh the list of open windows.

## Notes
- The script is intended to run on Windows as it uses the Windows API to modify window properties.
- Ensure that the window you want to modify is visible and not minimised.