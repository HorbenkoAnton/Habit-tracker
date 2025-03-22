from DataHandler import DataHandler

class HabitTracker:
    def __init__(self, data_handler):
        self.data_handler = data_handler
        self.data = self.data_handler.load_data()
        self.habits = self.data['habits']
        self.progress = self.data['progress']
    
    def save(self):
        self.data_handler.write_data(self.data)

    def add_habit(self,name, description):
        self.habits[name] = description
        for day in self.progress:
            self.progress[day][name] = False
        self.save()

    def remove_habit(self,name):
        del self.habits[name]
        for day in self.progress:
            del self.progress[day][name]
        self.save()

    def habit_status_switcher(self,date, habit_name):
        try:    
            self.progress[date]
            try:
                self.progress[date][habit_name]
                if self.progress[date][habit_name] == False:
                    self.progress[date][habit_name] = True
                else:
                    self.progress[date][habit_name] = False
                self.save()
            except KeyError:
                print("ERROR! Can't find habit to change")
        except KeyError:
            self.progress[date] = {}
            for habit in self.habits:
                if habit != habit_name:
                    self.progress[date][habit] = False
                else: 
                    self.progress[date][habit_name] = True
            self.save()
    

if __name__ == "__main__":
    data_handler = DataHandler("data.json")
    habit_tracker = HabitTracker(data_handler)
    #habit_tracker.habit_status_switcher('2025-03-18','Habit1')
    #habit_tracker.habit_status_switcher('2025-03-22','Habit1')
    #print(habit_tracker.habits)
    #print(data_handler.load_data())