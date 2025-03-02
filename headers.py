from dataclasses import dataclass
import datetime

#habit need to contain
# - name
# - description
# - status (yes\no)
@dataclass
class Habit:
    name: str
    description: str
    status: bool


#day need to contain
# - date
# - [habits]

@dataclass
class Day:
    habit_day: datetime.date = datetime.date.today
    habits: list[Habit]
