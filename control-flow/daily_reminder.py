# This script reminds user of tasks based on priority and time sensitivity
import time
# --- Prompt for Task Description ---
task = input("Enter your task: ")

# --- Prompt for Task Priority ---
priority = input("Priority (high/medium/low): ")

# --- Prompt for Time-Bound Status ---
time_bound = input("Is it time-bound? (yes/no): ")

# --- Process the Task ---
match priority:
    case 'high':
        result = f"🚨 {task} is a high priority task"
    case 'medium':
        result = f"⚠️ {task} is a medium priority task"
    case 'low':
        result = f"📝 {task} is a low priority task"

delay_seconds = 2  # Delay in seconds
# --- Time Sensitivity Check ---
if time_bound == "yes":
    message = "that requires immediate attention today!"
    reminder = f"\nReminder: {task} is a high priority task that requires immediate attention today!"
    result += " " + message 
else:
    message = ". Consider completing it when you have free time."
    reminder = f"\nReminder: {task} is a low priority task. Consider completing it when you have free time." 
    result += " " + message 

# --- Output the Reminder ---
print("\n" + result)
time.sleep(delay_seconds)  # Simulate a delay before showing the reminder
print(reminder)