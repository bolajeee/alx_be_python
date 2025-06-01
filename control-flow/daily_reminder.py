# This script reminds user of tasks based on priority and time sensitivity
import time

# --- Prompt for Task Description ---
task = input("Enter your task: ")

# --- Prompt for Task Priority ---
priority = input("Priority (high/medium/low): ").lower()

# --- Prompt for Time-Bound Status ---
time_bound = input("Is it time-bound? (yes/no): ").lower()

# --- Process the Task ---
match priority:
    case 'high':
        result = f"🚨 {task} is a high priority task"
    case 'medium':
        result = f"⚠️ {task} is a medium priority task"
    case 'low':
        result = f"📝 {task} is a low priority task"
    case _:
        result = f"❗ {task} has an unknown priority"

# --- Time Sensitivity Check ---
if time_bound == "yes":
    result += " that requires immediate attention today!"
else:
    result += ". Consider completing it when you have free time."

# --- Build the Reminder ---
match priority:
    case 'high':
        reminder = f"\nReminder: {task} is a high priority task"
    case 'medium':
        reminder = f"\nReminder: {task} is a medium priority task. Please address it soon."
    case 'low':
        reminder = f"\nReminder: {task} is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"\nReminder: {task} has an undefined priority level."

# --- Add Time-Bound Urgency if Applicable ---
if time_bound == "yes":
    reminder += " It is time-sensitive and should be completed today."

# --- Output the Reminder ---
print("\n" + result)

# --- Simulate Delay ---
delay_seconds = 2  # Set delay in seconds
time.sleep(delay_seconds)

print(reminder)
