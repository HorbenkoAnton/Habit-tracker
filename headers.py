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


def main():
    pass

if __name__ == "__main__":
    main()