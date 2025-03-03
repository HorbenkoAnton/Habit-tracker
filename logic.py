from headers import Habit
from headers import Day
from datetime import date
import pickle
import os
from pathlib import Path


FILENAME = Path("data.pkl")
#check if file exists
# - yes - append new data
# - no - create and write new data
def save_day(filename, habits):
    mode = "ab" if filename.exists() else "wb"
    with filename.open(mode) as file:
        today = Day(date.today(),habits)
        pickle.dump(today,file=file)
        pass



def load_day(filename):
    pass

def edit_day(filename, day):
    pass

def main():
    habit1 = Habit("1","1",True)
    habit2 = Habit("2","2",True)
    habit3 = Habit("3","3",True)
    save_day(FILENAME,habits = [habit1,habit2,habit3])

if __name__ == "__main__":
    main()