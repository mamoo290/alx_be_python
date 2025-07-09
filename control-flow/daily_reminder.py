task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# React to priority with match - assign base message
match priority:
    case "high" | "medium":
        message = f"Reminder: '{task}' is a {priority} priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# React to priority with match - assign base message
match priority:
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# React to priority with match - assign base message
match priority:
    case "high" | "medium":
        message = f"Reminder: '{task}' is a {priority} priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Task priority '{priority}' not recognized."

# Modify message with if based on time_bound
if time_bound == "yes" and priority in ["high", "medium", "low"]:
    message += " that requires immediate attention today!"
elif priority in ["high", "medium", "low"]:
    message += ". Consider completing it when you have free time."

print(message)
