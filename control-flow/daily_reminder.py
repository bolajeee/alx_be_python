# daily_reminder.py

# Prompt for task details
task = input("Enter your task for today: ")
priority = input("Enter the priority level (high, medium, low): ").lower()
time_bound = input("Is this task time-bound? (yes or no): ").lower()

# Generate reminder using match-case and conditionals
print("\n--- Daily Task Reminder ---")

match priority:
    case "high":
        reminder = f"🚨 High Priority Task: {task}"
    case "medium":
        reminder = f"⚠️ Medium Priority Task: {task}"
    case "low":
        reminder = f"📝 Low Priority Task: {task}"
    case _:
        reminder = f"📌 Task: {task} (unknown priority)"

# Modify reminder if time-bound
if time_bound == "yes":
    reminder += " — that requires immediate attention today!"

# Output the final reminder
print(reminder)
