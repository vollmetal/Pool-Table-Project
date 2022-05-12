import datetime as timer

class PoolTimer:
  def __init__ (self, start_time, end_time):
    self.start_time = start_time
    self.end_time = end_time
    self.time_played = 0

  
def file_manager(file_name, string_input = [], operation = "a"):
  seperator_start = "********START OF FILE********"
  seperator_end = "*********END OF FILE*********"
  
  if operation == "a":
    with open(file_name, "a") as print_file:
      for input in string_input:
        print_file.write(input)
        
  elif operation == "r":
    print(seperator_start)
    print(f"File Name is {file_name}")
    with open(file_name, "r") as print_file:
      file_contents = print_file.readlines()
      for line in file_contents:
        print(line)
    print(seperator_end)

class PoolTable:
  def __init__ (self, table_number, start_time = None, end_time = None):
    self.table_number = table_number
    self.is_occupied = False
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
      
  def table_finishes(self, time, file = None):
    if self.is_occupied == True:
      self.end_timer(time)
      self.is_occupied = False
      self.calculate_time_played()
      if file != None:
        file_manager(file, [f"The table number is: {self.table_number}\n", f"Start time: {self.start_time}\n", f"End time: {self.end_time}\n", f"Total time played: {self.time_played}\n", f"This table costs: ${self.cost}\n"])
          
    else:
      print("The table has no one at it")
  
  def calculate_time_played(self):
    self.time_played = self.end_time - self.start_time

  def print_table_info(self):
    if self.is_occupied:
      print("This table is occupied")
    else:
      print("This table is not occupied")
    print(f"This table costs: ${self.cost}")
    print(f"Table number: {self.table_number}")
    print(f"Start time: {self.start_time}")
    print(f"End time: {self.end_time}")
    print(f"Total time played: {self.time_played}")