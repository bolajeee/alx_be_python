# This script reminds user of tasks based off priority
task = input("Enter the task you want to be reminded of: ")
priority = input("Enter the priority of the task (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

match priority:
    case 'high':
        result = f"Reminder: {task} is a high priority task. Please complete it as soon as possible."
    case 'medium':
        result = f"Reminder: {task} is a medium priority task. Please complete it soon."
    case 'low':
        result = f"Reminder: {task} is a low priority task. You can complete it later."
    case _:
        result = "Error: Invalid priority. Please enter high, medium, or low."

if time_bound == "yes":
    result += " This task is time-bound, so please ensure it is completed on time."


print(result)