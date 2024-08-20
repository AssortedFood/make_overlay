import ctypes
import tkinter as tk
from tkinter import ttk
from ctypes import wintypes
import win32api
import win32con
import win32gui

def set_window_properties(hwnd, transparency, enable=True):
    if enable:
        # Set window to always on top
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        # Set window to click-through
        ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        ex_style |= win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style)

        # Set window transparency
        win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0, 0, 0), transparency, win32con.LWA_ALPHA)
    else:
        # Restore default window properties
        ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        ex_style &= ~(win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style)

        # Remove always on top
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        # Restore default transparency
        win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0, 0, 0), 255, win32con.LWA_ALPHA)

def get_open_windows():
    def enum_windows_proc(hwnd, lParam):
        if win32gui.IsWindowVisible(hwnd):
            window_text = win32gui.GetWindowText(hwnd)
            if window_text:
                windows.append((hwnd, window_text))
        return True

    windows = []
    win32gui.EnumWindows(enum_windows_proc, None)
    return windows

def update_window_list():
    open_windows = get_open_windows()
    windows_dict.clear()
    for hwnd, text in open_windows:
        windows_dict[text] = hwnd
    window_combobox['values'] = list(windows_dict.keys())
    status_label.config(text="Window list updated")

def on_apply():
    selected_window = window_combobox.get()
    if selected_window:
        hwnd = windows_dict[selected_window]
        transparency = transparency_scale.get()
        set_window_properties(hwnd, transparency)
        status_label.config(text="Applied settings to: " + selected_window)

def on_reset():
    selected_window = window_combobox.get()
    if selected_window:
        hwnd = windows_dict[selected_window]
        set_window_properties(hwnd, 255, enable=False)
        status_label.config(text="Reset settings for: " + selected_window)

# Get the initial list of open windows
windows_dict = {}

# Create the GUI
root = tk.Tk()
root.title("Select Window")

tk.Label(root, text="Select a window:").pack(padx=10, pady=5)
window_combobox = ttk.Combobox(root, values=list(windows_dict.keys()), width=50)
window_combobox.pack(padx=10, pady=5)

tk.Label(root, text="Transparency (0-255):").pack(padx=10, pady=5)
transparency_scale = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL)
transparency_scale.set(180)  # Default value
transparency_scale.pack(padx=10, pady=5)

apply_button = tk.Button(root, text="Apply", command=on_apply)
apply_button.pack(padx=10, pady=5)

reset_button = tk.Button(root, text="Reset", command=on_reset)
reset_button.pack(padx=10, pady=5)

update_button = tk.Button(root, text="Update", command=update_window_list)
update_button.pack(padx=10, pady=5)

status_label = tk.Label(root, text="")
status_label.pack(padx=10, pady=5)

# Initialize the window list
update_window_list()

root.mainloop()