# This script reminds user of tasks based on priority and time sensitivity

# --- Prompt for Task Description ---
task = ""
while not task.strip():
    task = input("Enter the task you want to be reminded of: ").strip()
    if not task:
        print("Task cannot be empty. Please enter a valid task.")

# --- Prompt for Task Priority ---
priority = ""
valid_priorities = ["high", "medium", "low"]
while priority not in valid_priorities:
    priority = input("Enter the priority of the task (high, medium, low): ").lower()
    if priority not in valid_priorities:
        print("Invalid input. Please enter 'high', 'medium', or 'low'.")

# --- Prompt for Time-Bound Status ---
time_bound = ""
while time_bound not in ["yes", "no"]:
    time_bound = input("Is the task time-bound? (yes/no): ").lower()
    if time_bound not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")

# --- Process the Task ---
match priority:
    case 'high':
        result = f"🚨 Reminder: {task} is a high priority task."
    case 'medium':
        result = f"⚠️ Reminder: {task} is a medium priority task."
    case 'low':
        result = f"📝 Reminder: {task} is a low priority task."

# --- Time Sensitivity Check ---
if time_bound == "yes":
    result += " This task is time-bound and requires immediate attention today!"

# --- Output the Reminder ---
print("\n" + result)
