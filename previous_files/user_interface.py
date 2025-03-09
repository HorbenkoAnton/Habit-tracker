import json_save
import os
from pathlib import Path
from tabulate import tabulate

FILENAME = Path("data.json")

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def display_ui(data):
    clear_console()
    dates = [day["date"] for day in data["days"]]
    table = []
    for habit in data["habits"]:
        row = [habit["name"]]
        for day in data["days"]:
            habit_status = "✓" if day["habits"][str(habit["id"])] else "𐄂"
            row.append(habit_status)
        table.append(row)
    
    headers = ["Habit"] + dates
    
    print(tabulate(table, headers=headers, tablefmt="grid", stralign="center"))




def main():
    data = json_save.load_data(FILENAME)
    display_ui(data)

if __name__ == "__main__":
    main()