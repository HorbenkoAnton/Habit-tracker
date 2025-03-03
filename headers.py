from dataclasses import dataclass
from datetime import date
import datetime

@dataclass
class Habit:
    name: str
    description: str
    status: bool

@dataclass
class Day:
    habit_day: date
    habits: list[Habit]


def main():
    habit1 = Habit("1","1",True)
    habit2 = Habit("2","2",True)
    habit3 = Habit("3","3",True)
    today = Day(date.today(), [habit1,habit2,habit3])
    print(today)
    pass

if __name__ == "__main__":
    main()