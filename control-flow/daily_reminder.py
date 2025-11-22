task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        print(f"Remainder: {task} is a high priority task")
    case "medium":
        print(f"{task} is a medium priority task")
    case "low":
        print(f"Note: {task} is a low priority task")
if time_bound == "yes":
    print(f"{task} requires immediate attention")
elif time_bound == "no":
    print("Consider completing it when you have free time.")