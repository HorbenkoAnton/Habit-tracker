from headers import Habit
from headers import Day
from datetime import date
import pickle
import os
from pathlib import Path

FILENAME = Path("data.pkl")



def clear_file(filename):
    open(filename,"wb").close()
    
def save_day(filename ,date, habits):
    mode = "ab" if filename.exists() else "wb"
    with filename.open("ab") as file:
        today = Day(date,habits)
        pickle.dump(today,file)

def load_days(filename):
    with filename.open("rb") as file:
        days = []
        while True:
            try:
                day = pickle.load(file)
                days.append(day)
            except EOFError:
                return days

def change_habit_state(filename, date, habit_name):
    days = load_days(filename)
    clear_file(filename)
    for day in days:
        if day.habit_day == date:
            for habit in day.habits:
                if habit.name == habit_name:
                    habit.state = not habit.state
                    save_day(filename,day.habit_day,day.habits)
        else:
            save_day(filename,day.habit_day,day.habits)
    

def main():
    habit1 = Habit("1","1",True)
    habit2 = Habit("2","2",True)
    habit3 = Habit("3","3",True)
    #save_day(FILENAME,date.today(),[habit1,habit2])
    #clear_file(FILENAME)
    change_habit_state(FILENAME,date(2025,3,3),"1")
    days = load_days(FILENAME)
    for day in days:
        print(day)

if __name__ == "__main__":
    main()