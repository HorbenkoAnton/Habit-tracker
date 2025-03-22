from tabulate import tabulate
from datetime import datetime, timedelta
from HabitTracker import HabitTracker
from DataHandler import DataHandler
import os

class UserInterface:
    def __init__(self, habit_tracker):
        self.habit_tracker = habit_tracker
        self.last_message = ""

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_table(self):
        today = datetime.today().date()
        week_dates = [(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]
        
        table = [[''] + week_dates]  # First row: dates
        
        for habit, description in self.habit_tracker.habits.items():
            row = [habit]  # Start row with habit name
            for date in week_dates:
                if date in self.habit_tracker.progress:
                    row.append('✔️' if self.habit_tracker.progress[date].get(habit, False) else '❌')
                else:
                    row.append('❌')
            table.append(row)

        print(tabulate(table, headers='firstrow', tablefmt='grid'))

    def display_commands(self):
        commands = [
            "Commands:",
            "1. add [habit_name] [description] - Add a new habit",
            "2. remove [habit_name] - Remove a habit",
            "3. switch [date] [habit_name] - Toggle habit status for a date",
            "4. info [habit_name] - Show habit description and all True dates",
            "5. exit - Exit the program"
        ]
        print("\n".join(commands))

    def run(self):
        while True:
            self.clear_console()
            self.display_table()
            self.display_commands()
            if self.last_message:
                print(f"\n{self.last_message}")

            command = input("Enter command: ").strip().split()

            if not command:
                self.last_message = "Invalid command. Please try again."
                continue

            action = command[0].lower()

            if action == 'add' and len(command) >= 3:
                habit_name = command[1]
                description = " ".join(command[2:])
                self.habit_tracker.add_habit(habit_name, description)
                self.last_message = f"Habit '{habit_name}' added."

            elif action == 'remove' and len(command) == 2:
                self.habit_tracker.remove_habit(command[1])
                self.last_message = f"Habit '{command[1]}' removed."

            elif action == 'switch' and len(command) == 3:
                self.habit_tracker.habit_status_switcher(command[1], command[2])
                self.last_message = f"Habit '{command[2]}' status switched on {command[1]}."

            elif action == 'info' and len(command) == 2:
                habit_name = command[1]
                if habit_name in self.habit_tracker.habits:
                    description = self.habit_tracker.habits[habit_name]
                    true_dates = [date for date, habits in self.habit_tracker.progress.items() if habits.get(habit_name)]
                    self.last_message = f"{habit_name}: {description}\nTrue on: {', '.join(true_dates) if true_dates else 'None'}"
                else:
                    self.last_message = f"Habit '{habit_name}' not found."

            elif action == 'exit':
                print("Exiting...")
                break

            else:
                self.last_message = "Invalid command. Please try again."

if __name__ == "__main__":
    data_handler = DataHandler("data.json")
    habit_tracker = HabitTracker(data_handler)
    ui = UserInterface(habit_tracker)
    ui.run()