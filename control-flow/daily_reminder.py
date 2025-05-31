# This script reminds user of tasks based on priority and time sensitivity

# --- Prompt for Task Description ---
task = input("Enter your task: ").strip()
if not task:
    print("Task cannot be empty. Please enter a valid task.")

# --- Prompt for Task Priority ---
priority = input("Priority (high/medium/low) ").lower()

# --- Prompt for Time-Bound Status ---
time_bound = input("Is it time-bound? (yes/no): ").lower()
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
