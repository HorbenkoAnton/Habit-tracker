from dataclasses import dataclass
from datetime import date

@dataclass
class Habit:
    name: str
    description: str
    state: bool

@dataclass
class Day:
    habit_day: date
    habits: list[Habit]


#something like that?
#I need to see if i can bind size(days) to 7
#Yeah so basicly i need to rewrite all my saving logic :)
@dataclass
class Wekk:
    days: list[Day]


def main():
    pass

if __name__ == "__main__":
    main()