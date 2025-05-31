# daily_reminder.py

# Function to validate yes/no input
def get_time_bound():
    while True:
        response = input("Is this task time-bound? (yes or no): ").strip().lower()
        if response in ("yes", "no"):
            return response
        print("Please enter 'yes' or 'no'.")

# Function to validate priority input
def get_priority():
    while True:
        level = input("Enter the priority level (high, medium, low): ").strip().lower()
        if level in ("high", "medium", "low"):
            return level
        print("Please enter 'high', 'medium', or 'low'.")

# Prompt for the task
task = ""
while not task.strip():
    task = input("Enter your task for today: ").strip()
    if not task:
        print("Task cannot be empty.")

# Prompt for valid priority and time-bound input
priority = get_priority()
time_bound = get_time_bound()

# Generate reminder
print("\n--- Daily Task Reminder ---")

match priority:
    case "high":
        reminder = f"🚨 High Priority Task: {task}"
    case "medium":
        reminder = f"⚠️ Medium Priority Task: {task}"
    case "low":
        reminder = f"📝 Low Priority Task: {task}"

if time_bound == "yes":
    reminder += " — that requires immediate attention today!"

print(reminder)
