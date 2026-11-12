import tkinter as tk
import subprocess
import sys
from datetime import datetime

process = None


def start_detection():
    global process

    if process is None or process.poll() is not None:
        process = subprocess.Popen([sys.executable, "main.py"])

        status_label.config(
            text="● STATUS: DETECTION ACTIVE"
        )


def stop_detection():
    global process

    if process is not None and process.poll() is None:
        process.terminate()
        process = None

        status_label.config(
            text="● STATUS: DETECTION STOPPED"
        )


def exit_app():
    stop_detection()
    root.destroy()


root = tk.Tk()

root.title("Driver Drowsiness Detection System")
root.geometry("700x500")
root.resizable(False, False)


# Main Title
title = tk.Label(
    root,
    text="DRIVER DROWSINESS\nDETECTION SYSTEM",
    font=("Arial", 24, "bold"),
    pady=20
)

title.pack()


# Subtitle
subtitle = tk.Label(
    root,
    text="AI-Based Real-Time Driver Safety Monitoring",
    font=("Arial", 13)
)

subtitle.pack(pady=5)


# Information Box
info = tk.Label(
    root,
    text="Webcam • Face Detection • EAR Analysis • Alarm Alert",
    font=("Arial", 11),
    relief="solid",
    padx=20,
    pady=10
)

info.pack(pady=25)


# Status Label
status_label = tk.Label(
    root,
    text="● STATUS: READY",
    font=("Arial", 14, "bold"),
    pady=10
)

status_label.pack(pady=10)


# Buttons Frame
button_frame = tk.Frame(root)

button_frame.pack(pady=15)


start_button = tk.Button(
    button_frame,
    text="START DETECTION",
    font=("Arial", 13, "bold"),
    width=20,
    height=2,
    command=start_detection
)

start_button.grid(row=0, column=0, padx=10)


stop_button = tk.Button(
    button_frame,
    text="STOP DETECTION",
    font=("Arial", 13, "bold"),
    width=20,
    height=2,
    command=stop_detection
)

stop_button.grid(row=0, column=1, padx=10)


# Exit Button
exit_button = tk.Button(
    root,
    text="EXIT APPLICATION",
    font=("Arial", 11, "bold"),
    width=20,
    command=exit_app
)

exit_button.pack(pady=20)


def update_time():
    current_time = datetime.now().strftime("%d-%m-%Y   %I:%M:%S %p")
    time_label.config(text=current_time)
    root.after(1000, update_time)

#date and time
time_label = tk.Label(
    root,
    font=("Arial", 11, "bold")
)

time_label.pack(pady=5)

update_time()


# Footer
footer = tk.Label(
    root,
    text="Real-Time Driver Drowsiness & Distraction Alert System",
    font=("Arial", 9)
)

footer.pack(side="bottom", pady=15)


root.mainloop()