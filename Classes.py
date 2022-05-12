import datetime as timer
import math
import json

class PoolTimer:
  def __init__ (self, start_time = None, end_time = None):
    
    self.start_time = {}
    self.end_time = {}
    self.time_played = 0

  def change_times(self, start_time, end_time, operator):
    if start_time["hour"]:
      if operator == "add":
        new_timeset = {"hour": start_time["hour"] + end_time["hour"],"minute": start_time["minute"] + end_time["minute"],"second": start_time["second"] + end_time["second"]}
      
        if new_timeset["second"] >= 60:
          new_timeset["minute"] += (int(new_timeset["second"]/ 60))
          new_timeset["second"] -= 60 * int(new_timeset["second"]/60)
        if new_timeset["minute"] >= 60:
          new_timeset["hour"] += int(new_timeset["minute"]/ 60)
          new_timeset["minute"] -= 60 * (int(new_timeset["minute"]/ 60))
      elif operator == "subtract":
        new_timeset = {"hour": start_time["hour"] - end_time["hour"],"minute": start_time["minute"] - end_time["minute"],"second": start_time["second"] - end_time["second"]}
        if new_timeset["minute"] < 0 and new_timeset["hour"] >= int(math.ceil(-(new_timeset["minute"])/60)):
          new_timeset["hour"] -= int(math.ceil(-(new_timeset["minute"])/60))
          new_timeset["minute"] += 60 * int(math.ceil(-(new_timeset["minute"])/60))
        elif new_timeset["minute"] >= int(math.ceil(-(new_timeset["second"])/60)):
          print("This is negative")
            
        if new_timeset["second"] < 0 and new_timeset["minute"] >= int(math.ceil(-(new_timeset["second"])/60)):
          new_timeset["minute"] -= int(math.ceil(-(new_timeset["second"])/60))
          new_timeset["second"] += 60 * int(math.ceil(-(new_timeset["second"])/60))
        elif new_timeset["minute"] >= int(math.ceil(-(new_timeset["second"])/60)):
          print("This is good")
          
      return new_timeset
    

  def new_time_set(self, time_set, set_type = "all"):
    if set_type == "date":
      time = time_set
      month = time.month
      day = time.day
      year = time.year
      
      if day >= 30:
        month += (int(day % 30))
        day -= (30 * int(day % 30))
      if month >= 12:
        year += (int(month % 12))
        print(int(month % 12))
        month -= (12 * int(month % 12))
      return {"month": month, "day": day, "year": year}
    elif set_type == "time":
      time = time_set
      hour = time.hour
      minute = time.minute
      second = time.second
      if second >= 60:
        minute += (int(second % 60))
        second -= (60 * int(second % 60))
      if minute >= 60:
        hour += (int(minute % 60))
        minute -= (60 * int(minute % 60))
      return {"hour": hour, "minute": minute, "second": second}
    elif set_type == "all":
      time = time_set
      month = time.month
      day = time.day
      year = time.year
      print(f"{month % 12}")

      if day >= 30:
        month += (int(day % 30))
        day -= (30 * int(day % 30))
      if month >= 12:
        
        year += (int(month % 12))
        month -= (12 * int(month % 12))
      
      time = time_set
      hour = time.hour
      minute = time.minute
      second = time.second
      
      if second >= 60:
        minute += (int(second % 60))
        second -= (60 * int(second % 60))
      if minute >= 60:
        hour += (int(minute % 60))
        minute -= (60 * int(minute % 60))
      return {"month": month, "day": day, "year": year, "hour": hour, "minute": minute, "second": second}
    
    

  
def file_manager(file_name, string_input = [], operation = "a"):
  print(file_name.rsplit('.')[1])
  seperator_start = "********START OF FILE********"
  seperator_end = "*********END OF FILE*********"
  temp_object = {"table": string_input}
  if operation == "a":
    with open(file_name, "w") as print_file:
      json.dump(temp_object, print_file)
        
  elif operation == "r":
    print(seperator_start)
        
    with open(file_name, "r") as print_file:
      raw_data = json.load(print_file)
      table_contents = raw_data["table"]
      print(f"File Name is {file_name}")
      for content in table_contents:
        print(f"{content}: {table_contents[content]}")
    print(seperator_end)

class PoolTable:
  def __init__ (self, table_number, start_time = None, end_time = None):
    self.table_number = table_number
    self.is_occupied = False
    self.timer = PoolTimer;
    self.start_time = start_time
    self.end_time = end_time
    self.time_played = 0
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
    if time > 60:
      hours = 0
      minutes = 0
      seconds = time
      
      minutes = int(seconds/60)
      seconds -= 60 * int(seconds/60)
      if minutes >= 60:
        hours = int(minutes/60)
        minutes -= 60 * int(minutes/60)
      return {"hours": hours, "minutes": minutes, "seconds": seconds}
      
  def table_finishes(self, time, file = None):
    if self.is_occupied == True:
      self.end_timer(time)
      self.is_occupied = False
      self.time_played = self.calculate_time_played()
      if file != None:
        temp_date_time = f"{self.start_time}"
        temp_end_date_time = f"{self.end_time}"
        file_manager(file, {"table number": self.table_number, "Start time": temp_date_time, "End time": temp_end_date_time, "Time played": self.time_played, "Total cost of the table": self.cost})
          
    else:
      print("The table has no one at it")
  
  def calculate_time_played(self):
    holder = self.end_time - self.start_time
    return self.convert_time(holder.seconds)

  def print_table_info(self):
    if self.is_occupied:
      print("This table is occupied")
    else:
      print("This table is not occupied")
    print(f"This table costs: ${self.cost}")
    print(f"Table number: {self.table_number}")
    print(f"Start time: {self.start_time}")
    print(f"End time: {self.end_time}")
    print(f"Total time played: {self.time_played['hours']}:{self.time_played['minutes']}:{self.time_played['seconds']}")