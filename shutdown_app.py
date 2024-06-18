import time
import os
import sys

# Ask the user whether they want to shut down, hibernate, or sleep
while True:
    mode = input("Would you like to:\n1. shutdown\n2. hibernate\n3. sleep\n> ")
    if mode == "1" or mode.lower() == "shutdown":
        command = "shutdown"
        break
    elif mode == "2" or mode.lower() == "hibernate":
        command = "shutdown /h"
        break
    elif mode == "3" or mode.lower() == "sleep":
        command = "rundll32.exe powrprof.dll,SetSuspendState Sleep"
        break
    else:
        print("Invalid input. Please enter '1' or 'shutdown' for shut down, '2' or 'hibernate' for hibernate, '3' or 'sleep' for sleep.\n> ")

# Ask the user for the number of seconds, minutes, or hours to wait before executing the command
while True:
    delay = input("How long should I wait before executing the command? (e.g. 3600, 10m, 2h):\n> ")
    if delay.endswith("m"):
        try:
            minutes = int(delay[:-1])
            seconds = minutes * 60
            break
        except ValueError:
            print("Invalid input. Please enter a valid number of minutes.")
    elif delay.endswith("h"):
        try:
            hours = int(delay[:-1])
            seconds = hours * 3600
            break
        except ValueError:
            print("Invalid input. Please enter a valid number of hours.")
    else:
        try:
            seconds = int(delay)
            break
        except ValueError:
            print("Invalid input. Please enter a valid time in the format 'X', 'Xm', or 'Xh', where X is a number.")

# Wait the specified number of seconds, printing a countdown of the remaining time
print(f"Executing {command} in {seconds} seconds...")
while seconds > 0:
    # Overwrite the previous countdown by printing a newline, the current countdown, and moving the cursor back to the start of the line
    sys.stdout.write("\r")
    sys.stdout.write(f"{seconds} seconds remaining...")
    sys.stdout.flush()
    time.sleep(1)
    seconds -= 1

# Execute the command
os.system(command)
