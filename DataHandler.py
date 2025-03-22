import json

class DataHandler:
    def __init__(self,filename):
        self.filename = filename

    def load_data(self):
        #TODO checks if file exists
        with open(self.filename, 'r') as file:  
            data = json.load(file)
        return data
    
    def write_data(self,data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    # def clear_data(self):
    #     with open(self.filename, 'w') as file:
    #         pass

if __name__ == "__main__":
      data_handler = DataHandler("data.json")
      data = data_handler.load_data()
      habits , days = data
      days = data[days]
      habits = data[habits]
      days["2025-03-17"]["Habit1"] = True
      data_handler.write_data(data)
      print(data_handler.load_data())