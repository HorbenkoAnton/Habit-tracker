import json
from datetime import date
import os
from pathlib import Path


FILENAME = Path("data.json")

def clear_file(filename):
    with open(filename,"w") as file:
        data = {"habits": [],"days": []}
        json.dump(data,file,indent=4)


def exist_checker(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            json.dump({"habits": [],"days": []}, file) 


def add_day(filename,date):
    exist_checker(filename)
    with open(filename, "r") as file:
        data = json.load(file)
    for day in data["days"]:
        if day["date"] == str(date):
            print("Day with that date is already existing")
            #TODO make it exeption
            return
    habits_ids = [habit["id"] for habit in data["habits"]]
    new_day = {"date":str(date), "habits":{habit: False for habit in habits_ids} }
    
    
    data["days"].append(new_day)
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def add_habit(filename,name,description):
    exist_checker(filename)
    with open(filename,"r") as file: 
        data = json.load(file)
    new_id = max(habit["id"] for habit in data["habits"]) + 1 if data["habits"] else 1
    new_habit = {"id":new_id, "name":name,"description":description}

    data["habits"].append(new_habit)
    for day in data["days"]:
        day["habits"][str(new_id)] = False

    
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)


#loads all days
#if days is smaller then 7
#add days that isn't enough
def load_week(filename, day):
    with open(filename,"r") as file:
        data = json.load(file)
    count = 0
    while len(data["days"]) < 7:
        data["days"].append

def main():

    add_habit(FILENAME,"Meditation","10 mins of meditation")
    add_day(FILENAME,date.today())
    #clear_file(FILENAME)


if __name__ == "__main__":
    main()