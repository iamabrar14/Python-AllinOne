day = input("Enter day: ")

match day.lower():
    case "saturday" | "sunday":
        print("weekend")
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("weekday")
    case _:
        print("Invalid day")
