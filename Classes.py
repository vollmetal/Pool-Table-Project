import datetime as timer
import json


def file_manager(file_name, string_input = [], operation = "a"):
  seperator_start = "********START OF FILE********"
  seperator_end = "*********END OF FILE*********"
  temp_object = [string_input]
  if operation == "a":
    try:
      with open(file_name, "r") as print_file:
        raw_data = json.load(print_file)
        raw_data.append(string_input)
        temp_object = raw_data
    except:
      with open(file_name, "w") as print_file:
        json.dump(temp_object, print_file)
    
    with open(file_name, "w") as print_file:
      json.dump(temp_object, print_file)
        
  elif operation == "r":
    print(seperator_start)
    try:
      
      with open(file_name, "r") as print_file:
        raw_data = json.load(print_file)
        table_contents = raw_data
        print(f"File Name is {file_name}")

        table_seperator = "--------------------------"
        for index in range(1, len(table_contents)):
          for table in table_contents[index]:
            
            print(table_seperator)
            temp_table = PoolTable(index)
            temp_table.start_time = table_contents[index][table]["Start time"]
            temp_table.end_time = table_contents[index][table]["End time"]
            temp_table.time_played = table_contents[index][table]["Time played"]
            temp_table.cost = table_contents[index][table]["Total cost of the table"]
            print(f"Table number: {temp_table.table_number}")
            print(f"Start time {temp_table.start_time}")
            print(f"End time: {temp_table.end_time}")
            print(f'Time played: {temp_table.time_played["hours"]}:{temp_table.time_played["minutes"]}:{temp_table.time_played["seconds"]}')
          print(f"Cost of the table: {temp_table.cost}")
    except FileNotFoundError:
      print("File not found!")
    print(seperator_end)

class PoolTable:
  def __init__ (self, table_number, start_time = None, end_time = None):
    self.table_number = table_number
    self.is_occupied = False
    self.start_time = start_time
    self.end_time = end_time
    self.time_played = None
    self.price_per_hour = 30
    self.cost = 0

  def start_timer(self, date):
    self.start_time = date

  def end_timer(self, date):
    self.end_time = date

  def occupy_table(self, time):
    if self.is_occupied == False:
      self.is_occupied = True
      self.start_timer(time)
    else:
      print("This table is currently occupied")

  def convert_time(self, time):
    hours = 0
    minutes = 0
    seconds = time
    total_time_in_seconds = time
    if time > 60:
      minutes = int(seconds/60)
      seconds -= 60 * int(seconds/60)
      if minutes >= 60:
        hours = int(minutes/60)
        minutes -= 60 * int(minutes/60)
    return {"hours": hours, "minutes": minutes, "seconds": seconds, "total time": total_time_in_seconds}
      
  def table_finishes(self, time, file = None):
    if self.is_occupied == True:
      self.end_timer(time)
      self.is_occupied = False
      self.time_played = self.calculate_time(self.start_time, self.end_time)
      self.cost = self.calculate_cost()
      if file != None:
        temp_date_time = f"{self.start_time}"
        temp_end_date_time = f"{self.end_time}"
        file_manager(file, {f"Table {self.table_number}" : {"Start time": temp_date_time, "End time": temp_end_date_time, "Time played": self.time_played, "Total cost of the table": self.cost}})
      print(f"Table {self.table_number} saved scuccessfully!")
    else:
      print("The table has no one at it")

  def calculate_cost(self):
    return (self.price_per_hour * self.time_played["hours"]) + ((self.price_per_hour/60) * self.time_played["minutes"])

  def readable_datetime(self, date):
    self.year = date.year
    self.month = date.month

    return {"year": self.year, "month": self.month}
  
  def calculate_time(self, start_time, end_time):
    holder = end_time - start_time
    return self.convert_time(holder.seconds)

  def print_table_info(self):
    print(f"Table number: {self.table_number}")
    if self.is_occupied:
      print("This table is occupied")
    else:
      print("This table is not occupied")
    
    
    if self.start_time == None:
      print(f"Start time: None")
      print(f"This table costs: N/A")
    else:
      
      print(f"Start time: {self.start_time.month}-{self.start_time.day}-{self.start_time.year} {self.start_time.hour}:{self.start_time.minute}:{self.start_time.second}")
    if self.end_time == None:
      print(f"End time: None")
    else:
      print(f"End time: {self.end_time.month}-{self.end_time.day}-{self.end_time.year} {self.end_time.hour}:{self.end_time.minute}:{self.end_time.second}")
    if self.time_played == None and self.start_time == None:
      pass
    elif self.time_played == None:
      self.time_played = self.calculate_time(self.start_time, timer.datetime.now())
      print(f"Total time played: {self.time_played['hours']}:{self.time_played['minutes']}:{self.time_played['seconds']}")
      self.cost = self.calculate_cost()
      print(f"This table costs: ${self.cost}")
    elif self.time_played != None and self.start_time != None:
      self.cost = self.calculate_cost()
      print(f"This table costs: ${self.cost}")
      self.time_played = self.calculate_time(self.start_time, timer.datetime.now())
      print(f"Total time played: {self.time_played['hours']}:{self.time_played['minutes']}:{self.time_played['seconds']}")
    