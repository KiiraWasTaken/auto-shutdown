# Power Management Script Documentation

## Overview
This Python script allows users to choose a power management action (shutdown, hibernate, or sleep) and specify a delay before executing the chosen action. It provides a countdown display during the delay period.

## Usage
1. **Choosing Power Action:**
   - Users are prompted to select one of the following actions:
     - `shutdown`: Initiates a system shutdown.
     - `hibernate`: Puts the system into hibernation mode.
     - `sleep`: Puts the system into sleep mode.

2. **Setting Delay:**
   - Users specify the delay in seconds, minutes ('m'), or hours ('h'). Examples:
     - `3600`: Represents 3600 seconds (1 hour).
     - `10m`: Represents 10 minutes.
     - `2h`: Represents 2 hours.

3. **Countdown Display:**
   - After confirming the action and delay, the script displays a countdown in seconds until the action is executed.

4. **Execution:**
   - Once the countdown completes, the chosen power action is executed using system commands (`os.system()`).

## Instructions
- Ensure Python is installed on your system.
- Run the script by double clicking on the "execute.bat" file and follow the prompts.
- Choose the desired power action and specify the delay according to the provided examples.
